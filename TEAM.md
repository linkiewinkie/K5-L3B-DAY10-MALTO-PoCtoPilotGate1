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

### Exit ticket

- Học được: cổng an toàn nên dựa vào nguồn sự thật (tracking, chính sách theo ngày, sổ cái) thay vì sửa model, và phải đặt ở lệnh ghi đầu tiên không đảo ngược được (ghi tiền đi trước ghi lỗi hãng). Khi đầu vào không đủ để biết ai có lỗi (thẻ S6), hành động an toàn là trả quyền cho người, không đoán.
- Còn chưa chắc: các cổng G1, G3, G4 giả định tracking ghi đúng ngày giao, hãng và nguyên nhân của từng kiện; G5 chỉ đếm trong một ngày mô phỏng, chưa theo cửa sổ 7 ngày của hợp đồng. Cả hai cần đo lại khi pilot thật.


## DangMinhThu-2A202604009

### Phần việc phụ trách

Kỹ sư cổng, phần **Đo kiểm**. Phiếu A: giữ cột Offline của câu 1.3 (A2) khớp với trace thật, giải thích cách đọc `pass_rate`, `pass_k` (pass^k), `pass@k`. Phiếu B: B0, B1 (câu 2.1), B2 (lấy trace `T-002@55`), B7.1 (cột mã lần chạy), B7.2 (câu 2.7), B7.3 (câu 2.8, cùng Code), các ô mã chạy và hash chốt ở B8. Phiếu C: C0, mã lần chạy ở C1, C2 Phần 1 và các ô mã lần chạy ở C7. Lệnh: `eval`, `gate`, `trace`, `checkpoint`, `grade`, `check_submission --collect`. Không sửa `lab10/guards.py`, `lab10/monitors.py` hay config.

### Đóng góp cụ thể

- Vòng 1: chạy baseline và đọc số (hoàn sai 20.000đ, 1 lỗi hãng oan, đều do `T-002@55`; kho HCM, hãng VNX xấu nhất); viết lý lẽ tự chặn hay người duyệt (khuyến nghị kết hợp) ở B1; chạy lại hai ticket hiểm của B7.3 và thêm một ca đổi đơn, khách, câu chữ để kiểm quy tắc áp dụng được ngoài bộ nền; chạy `checkpoint`, rồi `eval` ở mốc `prepared` và `gate` (mọi ngưỡng đã ký đạt).
- Phát hiện và sửa lỗi môi trường: máy đặt `core.autocrlf=true` nên Git đổi file tiêu chí sang CRLF, hash lệch bản đã ký (`gate` báo "tiêu chí ĐÃ BỊ SỬA"); đặt `autocrlf=false` riêng cho repo, khôi phục file về LF, chạy lại baseline.
- Vòng 2 (thẻ S6): chạy `grade --incident S6` trước khi sửa; dò `S6-01`, `S6-20`, `S6-42` ở hai mốc base và prepared để tìm ba kiểu lỗi (ghi lỗi nhầm kiện, tự đoán khi hai hãng cùng trễ, ghi quá trần lỗi trong ngày); đo lại sau mỗi thay đổi của Minh (G4, G5 rồi G5a) và kiểm hồi quy bộ nền; ghi nhận giá phải trả sau G5a (chuyển người 25% → 41,7%, chi phí 5.228đ → 6.862đ, ROI 0,91 → 0,46, sát ngưỡng 0,4).
- Gom bài bằng `check_submission --collect` tới khi `ĐỦ THÀNH PHẦN`.

### Bằng chứng

- Commit trên nhánh `minhthu`: `8d238ff`, `f885af4` (chốt vòng 1), `14ae9fa`, `b651707`, `2655f56`, `e5e8517` (gom bài).
- Vòng 1, bộ nền: base `R-base-before-20261119-152918-0f89e1` (pass_rate 0,9909; hoàn sai 20.000đ; lỗi oan 1) → prepared `R-base-prepared-20261119-162628-983686` (1,0; 0đ; 0). Hash chốt `a4e3fa99`. Dòng B0 1–4, B1.
- Vòng 2, thẻ S6: grade ban đầu `R-S6-grade-20261119-164029-983686` (FAIL: pass_rate 0,3333 → 0,6667, lỗi oan 40 → 20); after `R-S6-after-20261119-170022-89a89a`, bộ nền `R-base-after-20261119-170023-89a89a`, grade `R-S6-grade-20261119-170023-89a89a` PASS-VISIBLE. Phiếu C: C0, C1, C2 Phần 1, C7.
- Nhật ký đầy đủ: `runs/journal.jsonl` (đã gom vào `submission/runs/`).

### Dùng AI

Dùng Claude (Claude Code) để đọc output và chẩn đoán lỗi hash do CRLF, soạn nháp các ô Phiếu A/B/C của phần Đo kiểm, xử lý xung đột. Số liệu trong phiếu lấy trực tiếp từ output lệnh và `runs/journal.jsonl`. AI không viết cổng xử lý riêng theo mã ticket; các ngưỡng, config và quyết định v1, v2 do cả nhóm chốt.

### Exit ticket

- Học được: một con số trong quyết định chỉ có giá trị khi trỏ được về một mã lần chạy chạy trên đúng code và config hiện tại, nên phải ghi `--note` cho mỗi lần đo; và "hết lỗi" chưa đủ, phải đọc cả giá phải trả (chuyển người, chi phí, ROI) vì cổng G5a làm S6 sạch nhưng ROI sát ngưỡng đã ký. Một lỗi nhỏ về môi trường (CRLF) cũng đủ làm hash tiêu chí lệch và `gate` cảnh báo sai.
- Còn chưa chắc: bài kiểm tra ẩn dùng đơn, khách, ngày khác nên `pass_rate` 1,0 trên bộ nền và bộ S6 chưa chứng minh cổng tổng quát; G5 chỉ đếm trong một ngày mô phỏng, chưa theo cửa sổ 7 ngày; và ROI 0,46 có thể xuống dưới 0,4 nếu tỉ lệ ticket cần chuyển người tăng ở pilot thật.
