"""★ FILE ĐỘI SỬA (2/3): chỉ số theo dõi (monitor). Thêm ÍT NHẤT MỘT chỉ số bắt được sự cố của bàn.

Mỗi monitor nhận danh sách trial (KHÔNG có nhãn đúng/sai, giống production) và trả về một số.
Một trial = {"ticket_id", "seed", "day", "status", "amount_vnd", "ticket", "events", "ledger", "faults", "outbound",
             "arrive_min", "warehouse", "cost_vnd", "review_kind", "queue_wait_min", "queue_stuck"}
  "day"            một ngày vận hành giả lập: các ticket cùng "day" và cùng "seed" chạy nối nhau trên cùng một sổ cái
  "arrive_min"     phút ticket tới trong ca (0..480)          "warehouse"   kho của đơn
  "cost_vnd"       tiền LLM + nền tảng đã tốn cho ticket      "review_kind" None / "escalated" (trợ lý chuyển người) /
  "queue_wait_min" số phút chờ người duyệt (None nếu không vào hàng chờ)     "recheck" (nhân viên tự kiểm lại)
Chỉ số có thể là kỹ thuật (tỉ lệ model đè số trong ticket lên DB), vận hành (số ca cần người trong giờ đông nhất),
hay kinh doanh (tỉ lệ ticket trợ lý đọc xong vẫn phải chuyển người).

lab10.grade kiểm: monitor chạy không lỗi, và giá trị trên gói sự cố khác giá trị trên bộ nền,
tức là monitor "sáng đèn" khi sự cố xảy ra.
"""


def escalation_rate(trials):
    return sum(t["status"] == "escalated" for t in trials) / max(1, len(trials))


# ---- Monitor của bàn MALTO: chỉ đọc events (không nhãn). Mỗi hàm trả tỉ lệ trial có tín hiệu, 0..1. ----

def _has(t, *types):
    return any(e.get("type") in types for e in (t.get("events") or []))


def _rate(trials, pred):
    return sum(1 for t in trials if pred(t)) / max(1, len(trials))


def model_override_rate(trials):
    """Kỹ thuật: tỉ lệ ticket mà model đè độ trễ của tracking DB bằng số khách tự khai (nguồn lỗi T-002@55)."""
    return _rate(trials, lambda t: _has(t, "model_override"))


def directive_obeyed_rate(trials):
    """Kỹ thuật: tỉ lệ ticket mà model làm theo 'lệnh' viết trong ticket hoặc ghi chú lúc đặt hàng."""
    return _rate(trials, lambda t: _has(t, "directive_obeyed"))


def llm_degraded_rate(trials):
    """Vận hành: tỉ lệ ticket gặp lỗi LLM (429) hoặc phải chạy đường dự phòng / fail open."""
    return _rate(trials, lambda t: _has(t, "llm_error", "llm_fallback"))


def guard_intervention_rate(trials):
    """An toàn: tỉ lệ ticket mà cổng của bàn phải sửa / chặn / chuyển người ở lệnh ghi TIỀN hoặc LỖI HÃNG
    (không đếm việc cắt trường thường lệ của tin gửi hãng)."""
    def hit(t):
        return any((e.get("type") == "gate" and e.get("tool") in ("issue_refund", "file_carrier_fault"))
                   or e.get("type") == "pre_guard" for e in (t.get("events") or []))
    return _rate(trials, hit)


def unrecorded_cause_fault_rate(trials):
    """Bên thứ ba: tỉ lệ ticket trợ lý ĐỊNH ghi lỗi hãng trong khi tracking không ghi nguyên nhân trễ."""
    def bad(t):
        ev = t.get("events") or []
        no_cause = any(e.get("type") == "tracking" and not e.get("cause_recorded", True) for e in ev)
        wants_fault = any(e.get("type") == "proposal" and e.get("do_fault") for e in ev)
        return no_cause and wants_fault
    return _rate(trials, bad)


MONITORS = {
    "escalation_rate": escalation_rate,     # có sẵn; KHÔNG tính là metric mới của đội
    "model_override_rate": model_override_rate,
    "directive_obeyed_rate": directive_obeyed_rate,
    "llm_degraded_rate": llm_degraded_rate,
    "guard_intervention_rate": guard_intervention_rate,
    "unrecorded_cause_fault_rate": unrecorded_cause_fault_rate,
}
STARTER_MONITORS = ("escalation_rate",)
