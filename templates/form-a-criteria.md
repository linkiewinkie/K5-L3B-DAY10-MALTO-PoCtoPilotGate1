# Phiếu A · Phần của Lê Thế Anh

## Câu 1.2 · Mục tiêu nhìn từ hai người

- **Chị Oanh, kế toán đối soát:** Có thể đối chiếu hằng tuần từng khoản hoàn và lần ghi nhận trách nhiệm với đơn hàng, dữ liệu giao nhận, chính sách và chứng từ; truy được căn cứ cùng người hoặc hệ thống tạo bút toán để xử lý chênh lệch với hãng vận chuyển và shop.
- **Chị Hạnh, trưởng ca CSKH:** Nhận ticket được chuyển cấp kèm lý do và dữ liệu cần thiết; ưu tiên xử lý ca thiếu bằng chứng, không rõ trách nhiệm hoặc vượt hạn mức, bảo đảm ticket được tiếp nhận trong SLA 60 phút và khối lượng phù hợp năng lực ca trực.

## Câu 1.4 · Telemetry production

| Nội dung | Đề xuất |
|---|---|
| Bước / hành vi được đo | Theo dõi `file_carrier_fault` để phát hiện nguy cơ ghi lỗi hãng thiếu căn cứ. |
| Thước đo | Số lệnh ghi lỗi hãng bị người trực xác định là thiếu căn cứ, tính theo lần/ngày vận hành. |
| Dữ liệu | Nhật ký `file_carrier_fault`, parcel/tracking, policy và fault record. PIC vận hành Thế Anh rà soát cảnh báo, đối chiếu nguồn và ghi kết quả xác minh. |
| Cách tính | Đếm các lệnh không khớp nguyên nhân hoặc hãng theo dữ liệu nguồn đã đối chiếu. Thiếu hoặc mâu thuẫn dữ liệu được báo để người xác minh; không tự động kết luận hãng có lỗi. |
| Khung thời gian / ngưỡng báo động | Theo ngày vận hành. Báo ngay từng trường hợp nghi ngờ; nếu xác nhận một lần ghi oan, tạm dừng `file_carrier_fault` và báo NV-TUNG để thao tác công tắc theo runbook. Nếu `escalation_rate` vượt **35% trong một ca**, Thế Anh rà soát tải và năng lực ca trực. Mức 35% là ngưỡng cảnh báo nhóm đã thống nhất. |
| Điểm mù | Phụ thuộc vào log và độ chính xác của dữ liệu nguồn; không phát hiện sự cố chưa được ghi log hoặc dữ liệu tracking bị sai. |
