# Team

## Thông tin nhóm

- Tên nhóm (`TenNhom`, không dấu, không khoảng trắng): `MALTO`
- Lớp: `L3B`
- Repo của bàn: `K5-L3B-DAY10-MALTO-PoCtoPilotGate1`
- Thẻ sự cố đã bốc (S1–S8): `S6`

## Thành viên

Họ tên đầy đủ và MSSV của **mọi** thành viên; bàn 3 người thì để trống dòng 4. Vai: Kỹ sư cổng · Sản phẩm và kinh doanh · Vận hành và pháp lý (README mục 3, phút 0–15).

| STT | Họ và tên              | MSSV        | Vai                       | Trưởng nhóm |
| --: | ------------------------- | ----------- | ------------------------- | :------------: |
|   1 | Nguyễn Xuân Khánh Linh | 2A202603801 | Sản phẩm và kinh doanh |      Có      |
|   2 | Đậu Hoàng Minh         | 2A202604011 | Kỹ sư cổng             |                |
|   3 | Đặng Minh Thu           | 2A202604009 | Kỹ sư cổng (Đo kiểm) |                |
|   4 | Lê Thế Anh              | 2A202603983 | Vận hành và pháp lý  |                |

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

- Vòng 1: soát `T-002@55` (B2), viết 3 cổng G1 (tiền theo tracking), G2 (phê duyệt hợp lệ), G3 (lỗi hãng đúng kiện, không gửi dữ liệu cá nhân) và 5 monitor; thước đo A2 câu 1.3; hai ticket thử B7.3.
- Vòng 2 (thẻ S6): tìm hai nguyên nhân còn hở, viết G4 (không đoán kiện, chuyển người trước khi hoàn) và G5 (trần 2 lỗi/hãng/ngày), thêm 2 monitor; điền C2 Phần 2–3 và C8.
- Soạn slide và kịch bản demo cho cả bàn.

### Bằng chứng

- Commit: `07aa912`, `01d4d26` (vòng 1); `ef46ba3`, `b9e7398` (vòng 2).
- Bộ nền: `R-base-before-20261119-152918-0f89e1` → `R-base-after-20261119-152941-0f89e1` (hoàn sai 20.000đ → 0, lỗi oan 1 → 0).
- Thẻ S6: `R-S6-prepared-20261119-164029-983686` → `R-S6-after-20261119-170022-89a89a` (lỗi oan 20 → 0); grade `R-S6-grade-20261119-170023-89a89a` PASS-VISIBLE.

### Dùng AI

Dùng Claude (Claude Code) để đọc code agent, gợi ý và viết nháp cổng G1–G5 trong `guards.py`, monitor trong `monitors.py`, nháp các ô Phiếu A/B/C, nháp config cho nhóm, xử lý xung đột khi merge, và soạn slide cùng kịch bản demo. Mình đã chạy test, trace, ticket tự viết và kiểm lại từng cổng; các ngưỡng, config và quyết định v1/v2 do cả nhóm chốt.

## LeTheAnh-2A202603983

### Phần việc phụ trách

Vai Vận hành và pháp lý.

- Phiếu A: câu 1.2 và 1.4.
- Phiếu B: B4, B5, B7.5 và B7.6; cấu hình `operations` và `legal`.
- Phiếu C: C3.2, C4, C5 câu 3.3, C9–C11 cho thẻ S6.
- Điền `submission/submission.json`.

### Đóng góp cụ thể

- Viết mục tiêu từ góc nhìn của chị Oanh và chị Hạnh; đề xuất tín hiệu theo dõi nguy cơ ghi lỗi oan cho hãng.
- Phân tích HAZOP, lập checklist go-live và soạn runbook vận hành, pháp lý.
- Điền cấu hình người phụ trách, người duyệt, năng lực ca trực, điều kiện dừng và giới hạn dữ liệu gửi bên thứ ba.
- Phân tích tác động của sự cố S6 đối với hãng và tài xế; viết HAZOP, giả định môi trường, risk register và cập nhật runbook sau sự cố.
- Điền thông tin nhóm, thẻ S6, quyết định v1/v2 và ba dòng bắt buộc trong `submission/submission.json`.

### Bằng chứng

- Commit `fc2a48f`: Phiếu B và cấu hình vận hành/pháp lý.
- Commit `55f2294`: bản nháp phần vận hành/pháp lý của Phiếu C.
- Commit `8db8bb3`: cập nhật C9–C11 và `submission/submission.json`.
- Kết quả S6 và hồi quy được tham chiếu từ Phiếu C do Đo kiểm ghi; mình không tự chạy các lần đo chính thức đó.

### Dùng AI

Dùng Codex để hỗ trợ đọc và giải thích yêu cầu, soạn nháp Phiếu A/B/C,
cập nhật cấu hình, xử lý Git và kiểm tra thành phần bài nộp.
Các số liệu và quyết định của nhóm được đối chiếu với tài liệu, báo cáo và
ý kiến của các thành viên.

### Exit ticket

- Điều học được: [viết điều bạn thực sự hiểu được sau bài lab].
- Điều còn chưa chắc: [viết điều bạn còn muốn hỏi hoặc kiểm tra thêm].

### Exit ticket

- Học được: cổng an toàn nên dựa vào nguồn sự thật (tracking, chính sách theo ngày, sổ cái) thay vì sửa model, và phải đặt ở lệnh ghi đầu tiên không đảo ngược được (ghi tiền đi trước ghi lỗi hãng). Khi đầu vào không đủ để biết ai có lỗi (thẻ S6), hành động an toàn là trả quyền cho người, không đoán.
- Còn chưa chắc: các cổng G1, G3, G4 giả định tracking ghi đúng ngày giao, hãng và nguyên nhân của từng kiện; G5 chỉ đếm trong một ngày mô phỏng, chưa theo cửa sổ 7 ngày của hợp đồng. Cả hai cần đo lại khi pilot thật.
