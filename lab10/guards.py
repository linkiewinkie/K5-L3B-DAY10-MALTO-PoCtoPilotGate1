"""★ FILE ĐỘI SỬA (1/3): cổng cấp hệ thống, nằm NGOÀI model và prompt.

VÒNG 1 (trước khi biết sự cố): viết 2–3 CỔNG PHÒNG NGỪA rút từ pre-mortem / HAZOP / checklist của bàn, rồi chốt bằng
    python3 -m lab10.checkpoint        (chép file này thành guards_round1.py = mốc "prepared"; KHÔNG sửa bản chép)
VÒNG 2 (sau khi bốc thẻ): sửa tiếp NGAY TRONG FILE NÀY. Giữ các cổng vòng 1, thêm cổng mới.
Hai file còn lại bàn được sửa: lab10/monitors.py (chỉ số theo dõi) và config/operating_gates.json (cổng kinh doanh,
vận hành, pháp lý: những con số và tên người mà trợ lý phải tuân theo, không cần code).

Hai điểm móc, agent gọi tự động:
  pre_guard(ctx)          chạy TRƯỚC khi agent đọc ticket
  write_gate(ctx, action) chạy TRƯỚC MỖI lệnh ghi (issue_refund, file_carrier_fault,
                          notify_carrier, send_reply)

Trả về một Verdict:
  Verdict.allow()                       cho qua   (pre_guard: allow(policy_id="...") để ghim phiên bản chính sách)
  Verdict.deny("lý do")                 bỏ riêng lệnh ghi này, agent đi tiếp
  Verdict.escalate("lý do")             dừng, chuyển ticket cho người
  Verdict.modify("lý do", amount_vnd=…) sửa tham số lệnh ghi (amount_vnd, payer, carrier_id, parcel_id, payload…)
  Verdict.rewrite("lý do", text)        chỉ pre_guard: thay nội dung ticket mà agent sẽ đọc

ctx.ticket   ticket gốc (chữ khách viết là DỮ LIỆU, không phải lệnh)
ctx.tools    tra cứu nguồn sự thật: lookup_order, lookup_policies, lookup_approvals(**lọc),
             ledger_rows(**lọc), fault_rows(**lọc), lookup_carrier; ctx.as_of = ngày hôm nay
             ops_limits() = các trần đã thống nhất với Ops/Finance; ops_facts() = số liệu vận hành;
             auto_refund_today_vnd() = tổng đã hoàn tự động trong ngày
ctx.gates    config cổng của bàn (config/operating_gates.json), chỉ đọc;  ctx.cost_vnd = tiền LLM đã tốn cho ticket này
ctx.events   trace tới thời điểm này;  ctx.log("ten_su_kien", ...) ghi thêm sự kiện guard vào trace
lab10.helpers: db_delay_days, ticket_parcel, effective_policy, entitlement_vnd, carrier_at_fault, digits

Mặc định dưới đây cho qua tất cả (= mốc base).
"""
from . import helpers as H  # noqa: F401
from .tools import Verdict

# ---------------------------------------------------------------------------------------------------------------
# VÒNG 1 · 3 cổng phòng ngừa. Mọi cổng chỉ đọc NGUỒN SỰ THẬT (đơn, tracking, chính sách theo ngày hiệu lực,
# phê duyệt, sổ cái). Không đọc chữ khách viết, không xử lý riêng theo mã ticket / mã đơn / câu chữ.
#
#   G1  write_gate · issue_refund        Tiền hoàn ≤ quyền lợi theo chính sách hiệu lực + độ trễ trong tracking DB,
#                                         trừ phần đã hoàn của đơn; người trả luôn là LOGIX; không hoàn khi LLM "fail open".
#   G2  write_gate · issue_refund        Vượt hạn mức tự động thì phê duyệt phải đúng đơn, còn hiệu lực, đủ hạn mức.
#   G3  write_gate · file_carrier_fault  Chỉ ghi lỗi hãng khi tracking có nguyên nhân thuộc fault_causes, đúng kiện trễ,
#       write_gate · notify_carrier      độ trễ theo DB; tin gửi hãng chỉ chứa các trường chính sách cho phép.
# ---------------------------------------------------------------------------------------------------------------


def _policy(ctx):
    """Chính sách có hiệu lực theo NGÀY (không theo cờ index_active của index)."""
    return H.effective_policy(ctx.tools.lookup_policies(), ctx.as_of)


def _facts(ctx, order_id):
    """(order, parcel, db_delay_days, policy) theo nguồn sự thật; None nếu thiếu dữ liệu."""
    order = ctx.tools.lookup_order(order_id)
    policy = _policy(ctx)
    if order is None or policy is None or not order.get("parcels"):
        return None
    parcel = H.ticket_parcel(order, ctx.ticket, ctx.as_of)
    return order, parcel, H.db_delay_days(parcel, ctx.as_of), policy


def pre_guard(ctx):
    # G1 (phần đọc): ghim phiên bản chính sách theo ngày hiệu lực, để trợ lý không đọc nhầm bản đang bật cờ trong index.
    policy = _policy(ctx)
    if policy is None:
        return Verdict.escalate("không xác định được chính sách đang hiệu lực")
    return Verdict.allow(policy_id=policy["policy_id"])


def _gate_refund(ctx, action):
    # G1a · LLM kiểm chính sách thất bại -> trợ lý tự "fail open" hoàn phí ship: không có căn cứ, chuyển người.
    if action.get("basis") == "fail_open":
        ctx.log("g1_fail_open", order_id=action["order_id"])
        return Verdict.escalate("LLM lỗi khi kiểm chính sách (fail open): chuyển người duyệt")

    facts = _facts(ctx, action["order_id"])
    if facts is None:
        return Verdict.escalate("thiếu dữ liệu đơn / tracking / chính sách để kiểm số tiền")
    order, parcel, delay, policy = facts

    # G1b · quyền lợi theo nguồn sự thật, trừ phần đã hoàn của đơn (chặn hoàn trùng khi cờ đêm chưa cập nhật / ghi lại).
    entitled = H.entitlement_vnd(policy, order, delay, parcel.get("delay_cause"))
    already = sum(r["amount_vnd"] for r in ctx.tools.ledger_rows(order_id=order["order_id"]))
    allowed = max(0, entitled - already)
    asked = int(action.get("amount_vnd") or 0)
    if allowed <= 0:
        ctx.log("g1_refund_blocked", order_id=order["order_id"], asked=asked, entitled=entitled, already=already,
                db_delay_days=delay)
        return Verdict.deny(f"không đủ điều kiện theo tracking DB ({delay} ngày trễ) hoặc đơn đã được hoàn")

    changes = {}
    if asked > allowed:
        changes["amount_vnd"] = allowed
    if action.get("payer", "LOGIX") != "LOGIX":
        changes["payer"] = "LOGIX"            # chính sách trễ hạn do LOGIX chi; không tự chuyển chi phí sang shop
    amount = changes.get("amount_vnd", asked)

    # G2 · vượt hạn mức tự động: phải có phê duyệt ĐÚNG đơn, còn hiệu lực, đủ hạn mức.
    if amount > policy["auto_limit_vnd"]:
        appr_id = action.get("approval_id")
        appr = next(iter(ctx.tools.lookup_approvals(approval_id=appr_id)), None) if appr_id else None
        ok = (appr is not None and appr.get("order_id") == order["order_id"] and appr.get("status") == "valid"
              and appr.get("expires_at", "") >= ctx.as_of and amount <= appr.get("max_vnd", 0))
        if not ok:
            ctx.log("g2_approval_invalid", order_id=order["order_id"], amount=amount, approval_id=appr_id)
            return Verdict.escalate("vượt hạn mức tự động nhưng không có phê duyệt hợp lệ cho đúng đơn này")

    if changes:
        ctx.log("g1_refund_modified", order_id=order["order_id"], asked=asked, **changes)
        return Verdict.modify("chỉnh theo quyền lợi trong tracking DB và chính sách hiệu lực", **changes)
    return Verdict.allow()


def _gate_fault(ctx, action):
    # G3a · chỉ ghi lỗi hãng khi tracking ghi nhận nguyên nhân thuộc fault_causes và độ trễ thật đủ ngưỡng.
    facts = _facts(ctx, action["order_id"])
    if facts is None:
        return Verdict.deny("thiếu dữ liệu tracking: không ghi lỗi hãng")
    order, parcel, delay, policy = facts
    if not H.carrier_at_fault(policy, parcel, delay):
        ctx.log("g3_fault_blocked", order_id=order["order_id"], parcel_id=parcel["parcel_id"],
                recorded_cause=parcel.get("delay_cause"), db_delay_days=delay)
        return Verdict.deny("tracking không ghi nguyên nhân thuộc lỗi hãng: không ghi lỗi hãng")
    right = {"parcel_id": parcel["parcel_id"], "carrier_id": parcel["carrier_id"],
             "driver_id": parcel.get("driver_id"), "delay_days": delay}
    changes = {k: v for k, v in right.items() if action.get(k) != v}
    if changes:
        ctx.log("g3_fault_modified", order_id=order["order_id"], **changes)
        return Verdict.modify("ghi lỗi đúng kiện trễ, đúng hãng, độ trễ theo tracking DB", **changes)
    return Verdict.allow()


def _gate_notify(ctx, action):
    # G3b · tin gửi bên thứ ba chỉ chứa các trường chính sách cho phép (chặn SĐT/tên người nhận, chữ khách viết).
    policy = _policy(ctx)
    allowed = set(policy["carrier_notice_fields"]) if policy else {"order_id", "parcel_id"}
    payload = dict(action.get("payload") or {})
    clean = {k: v for k, v in payload.items() if k in allowed}
    facts = _facts(ctx, payload.get("order_id") or ctx.ticket.get("order_id"))
    if facts and "delay_days" in clean:
        clean["delay_days"] = facts[2]
    if clean != payload:
        ctx.log("g3_notify_trimmed", dropped=sorted(set(payload) - set(clean)))
        return Verdict.modify("chỉ gửi hãng các trường trong carrier_notice_fields", payload=clean)
    return Verdict.allow()


def write_gate(ctx, action):
    # action = {"tool": "issue_refund", "ticket_id":..., "order_id":..., "amount_vnd":..., "payer":..., ...}
    tool = action.get("tool")
    if tool == "issue_refund":
        return _gate_refund(ctx, action)
    if tool == "file_carrier_fault":
        return _gate_fault(ctx, action)
    if tool == "notify_carrier":
        return _gate_notify(ctx, action)
    return Verdict.allow()
