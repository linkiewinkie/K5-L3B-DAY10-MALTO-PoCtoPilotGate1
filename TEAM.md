# Team

## Thông tin nhóm

- Tên nhóm (`TenNhom`, không dấu, không khoảng trắng): `MALTO`
- Lớp: `L3B`
- Repo của bàn: `K5-L3B-DAY10-MALTO-PoCtoPilotGate1`
- Thẻ sự cố đã bốc (S1–S8):

## Thành viên

Họ tên đầy đủ và MSSV của **mọi** thành viên; bàn 3 người thì để trống dòng 4. Vai: Kỹ sư cổng · Sản phẩm và kinh doanh · Vận hành và pháp lý (README mục 3, phút 0–15).

| STT | Họ và tên | MSSV | Vai | Trưởng nhóm |
| --: | --------- | ---- | --- | :---------: |
|   1 | Nguyễn Xuân Khánh Linh | 2A202603801 | Sản phẩm và kinh doanh | Có |
|   2 | Đậu Hoàng Minh | 2A202604011 | Kỹ sư cổng | |
|   3 | Đặng Minh Thu | 2A202604009 | Kỹ sư cổng (Đo kiểm) | |
|   4 | Lê Thế Anh | | Vận hành và pháp lý | |

Ghi `members` trong `submission/submission.json` theo dạng `"HoVaTen-MSSV"`, khớp bảng trên.

**Ghi chú danh tính Git.** Ba commit `59e1438` (Initial commit), `1da0c82` (Merge upstream student repository updates) và `d385325` (Sign acceptance criteria) mang tên tác giả `NguyenXuanKhanhLinh` và email cá nhân. Đây là commit của Nguyễn Xuân Khánh Linh, MSSV `2A202603801`. Bàn giữ nguyên lịch sử, không viết lại, để không đổi mã và giờ của commit ký tiêu chí. Từ sau các commit này, danh tính Git dùng `2A202603801` / `2A202603801@example.com`.

## Cá nhân

Mỗi thành viên tự viết một mục bên dưới (chép mẫu, đổi tiêu đề thành họ tên không dấu và MSSV, ví dụ `## NguyenVanAn-20241234`).

## HoVaTen-MSSV

### Phần việc phụ trách

Vai trong bàn; câu nào của đề, mục nào của phiếu A/B/C, file nào (`lab10/guards.py`, `config/operating_gates.json`, …).

### Đóng góp cụ thể

...

### Bằng chứng

Mã commit, mã lần chạy (`runs/<mã>`), dòng trong phiếu.

### Exit ticket

Một điều học được, một điều còn chưa chắc.

## DauHoangMinh-2A202604011

### Phần việc phụ trách

Kỹ sư cổng, phần **Code**. Phiếu A câu 1.3 (A2, cột Offline). Phiếu B câu 2.2 (B2), câu 2.6 (B7.1), câu 2.8 (B7.3, cùng Đo kiểm).
Phiếu C câu 3.1 (C2), lá kỹ thuật C6, C7, C8 (vòng 2). File: `lab10/guards.py`, `lab10/monitors.py`.

### Đóng góp cụ thể

- Đọc luồng xử lý `lab10/agent.py`, lập bản đồ các bước và các lệnh ghi, liệt kê điểm yếu (model đè độ trễ DB, chọn chính sách theo cờ `index_active`, làm theo chỉ thị trong ghi chú, lấy phê duyệt theo khách, fail open khi LLM 429, ghi lặp, đổ lỗi hãng khi thiếu nguyên nhân, gửi dữ liệu người nhận cho hãng); gửi Đo kiểm vị trí trường cần xem trong trace.
- A2 câu 1.3: thước đo offline cho bước chọn độ trễ (tử số, mẫu số, xử lý ca thiếu dữ liệu, điểm mù).
- B2: soát `T-002@55`; bước sai đầu tiên là `model_override` (DB 2 ngày, ticket 5 ngày) → hoàn sai 20.000đ và ghi lỗi oan cho VNX / TX-VNX-03; xếp cả hai là lỗi chìm.
- Đối chiếu 22 ticket bộ nền: số tiền đúng theo nhãn trùng với `entitlement_vnd` tính từ tracking và chính sách hiệu lực, lỗi hãng đúng trùng với `carrier_at_fault` → làm căn cứ cho cổng không làm hỏng ca đúng.
- B7.1: viết 3 cổng vòng 1 trong `lab10/guards.py`: G1 tiền ≤ quyền lợi theo nguồn sự thật (ghim chính sách theo ngày, trừ phần đã hoàn, payer LOGIX, chặn fail open); G2 phê duyệt đúng đơn, đúng ticket, còn hạn, đủ hạn mức; G3 chỉ ghi lỗi hãng khi tracking có nguyên nhân, đúng kiện, và tin gửi hãng chỉ giữ trường chính sách cho phép.
- B7.3: hai ticket thử (`--adhoc`) cho tính chất "tiền, lỗi hãng, tin gửi hãng chỉ phụ thuộc nguồn sự thật".
- Thêm 5 monitor không cần nhãn trong `lab10/monitors.py` để dùng cho C8.
- Soạn nháp tham khảo cho cả nhóm (Phiếu A, Phiếu B, `acceptance_criteria.json`, `operating_gates.json`).

### Bằng chứng

- Commit: `07aa912` (cổng vòng 1 và monitor), `01d4d26` (siết cổng phê duyệt, điền phần Code của Phiếu A, B), `1542582` (merge `dev` vào `main` sau commit ký `d385325`).
- `python3 -m unittest discover -s tests` → `Ran 13 tests … OK` (gồm `test_team_guards_do_not_break_base`).
- `python3 -m lab10.trace --suite base --stage after --ticket T-002 --seed 55` → `denied`, sổ cái trống, không lỗi hãng, ĐẠT.
- Mã lần chạy `base · after`: ___ (Đo kiểm gửi sau khi chạy).
- Phiếu A mục A2 (cột Offline); Phiếu B mục B2, B7.1, B7.3.

### Dùng AI

Dùng Claude (Claude Code) để đọc code agent, gợi ý và viết nháp cổng trong `guards.py`, monitor trong `monitors.py`, nháp các ô phiếu A/B và nháp config cho nhóm. Mình đã chạy test, trace và kiểm lại từng cổng; các ngưỡng và quyết định do cả nhóm chốt.

### Exit ticket

- Học được: cổng an toàn nên dựa vào nguồn sự thật (tracking, chính sách theo ngày, sổ cái) thay vì sửa model, và phải đặt ở lệnh ghi đầu tiên không đảo ngược được (ghi tiền đi trước ghi lỗi hãng).
- Còn chưa chắc: cổng G1 giả định tracking DB đúng; nếu điểm phát quét sót `delivered_date` thì cổng không thấy, cần đo lại khi pilot thật.
