# Phân công chi tiết Lab 10 cho nhóm MALTO

**Repo** `K5-L3B-DAY10-MALTO-PoCtoPilotGate1` · **Nhóm 4 người** · **Thời lượng** 240 phút

Nhóm chuẩn bị hồ sơ Gate 1 để quyết định trợ lý hoàn tiền LogiX-VN đã đủ điều kiện pilot với khách thật hay chưa. Mỗi phase dưới đây ghi rõ người cầm bút, việc có thể làm song song, đầu vào phải chờ, nơi ghi kết quả và điểm bàn giao.

## Phân vai đầu buổi

| Người | Vai | Họ tên | Đầu việc chịu trách nhiệm xuyên suốt |
| --- | --- | --- | --- |
| **1** | **Trưởng nhóm kiêm Sản phẩm & Kinh doanh** | Nguyễn Xuân Khánh Linh | Giữ thứ tự các mốc ký, đo, chốt và push. Cầm bút ở các phần mục tiêu hệ thống, tiêu chí, bản đồ dữ liệu, cổng kinh doanh và quyết định v1/v2. |
| **2** | **Kỹ sư cổng — Code** | Đậu Hoàng Minh | Đọc luồng xử lý và dữ liệu, tìm nguyên nhân kỹ thuật, viết guard và monitor. Bàn giao thay đổi và hành vi cần kiểm cho Đo kiểm. |
| **3** | **Kỹ sư cổng — Đo kiểm** | Đặng Minh Thu | Chạy test, eval, trace, gate, checkpoint và grade. Giữ mã lần chạy, điền nhật ký, kiểm hồi quy và chạy thử trực tiếp lúc demo. |
| **4** | **Vận hành & Pháp lý** | Lê Thế Anh | Làm HAZOP, checklist có PIC, config vận hành và pháp lý, quy trình trực ca, phần riêng của thẻ, risk register và gom bài. |

- Khi điền vai chính thức trong `TEAM.md`, ghi **Kỹ sư cổng** cho người 2 và 3. Hai bạn ghi phần việc **Code** hoặc **Đo kiểm** trong mục cá nhân, kèm bằng chứng của mình.
- Quyết định v1, v2 và các ngưỡng do **cả nhóm** chốt. Trưởng nhóm ghi quyết định và điều phối commit/push. Trong bảng go-live, **PIC** là một người có tên chịu trách nhiệm cho từng việc. Các vai trực ca trong runbook dùng tên hoặc mã nhân viên LogiX theo `data/world.json`.

**Quy ước lệnh.** Chạy từ thư mục gốc repo. Các khối lệnh dùng `python`. Dùng `python3` hoặc `py -3` nếu đó là cách gọi Python 3 trên máy của nhóm. Thay `MA_LAN_CHAY`, `Sx`, mã đơn, mã khách và chuỗi giữ chỗ trước khi chạy.

**Cách đọc bảng đầu vào.** Mỗi ô ghi theo dạng **người bàn giao → tài liệu hoặc kết quả được giao**. Tên vai ứng với bốn người ở bảng phân vai. “Tự dùng lại” chỉ kết quả do chính người nhận đã giữ từ phase trước. Cột cuối ghi việc cần nhận ngay trong phase để biết phần nào có thể bắt đầu song song và phần nào phải chờ.

## Lịch và các đầu vào phải chờ

| Phút | Phase | Đầu vào bắt buộc để chuyển bước |
| --- | --- | --- |
| 0–15 | [0 · Chuẩn bị](#phase-0) | Repo nhóm, Python 3, Git, PRD v1.1 và eval card từ Lab 9. |
| 15–65 | [1 · Viết và ký tiêu chí](#phase-1) | Tài liệu chung, nguồn dữ kiện. Phải ký, commit và push trước lần đánh giá đầu tiên. |
| 65–85 | [2A · Đo base và tìm rủi ro](#phase-2a) | Commit ký đã push. Báo cáo base và phân tích rủi ro là đầu vào để chọn cổng vòng 1. |
| 85–115 | [2B · Dựng cổng và quyết định v1](#phase-2b) | Rủi ro đã chọn, kết quả base, tiêu chí đã ký. Phải chốt vòng 1 rồi mới đo prepared để quyết định v1. |
| 125–155 | [3A · Nhận thẻ và phân tích](#phase-3a) | Bản chốt vòng 1 và v1 đã push, Coach đã phát thẻ, nhóm biết đúng số thẻ. Chạy grade trước khi sửa. |
| 155–185 | [3B · Sửa và đo lại](#phase-3b) | Báo cáo ban đầu của thẻ, fault tree trước sửa, các nguyên nhân có bằng chứng. |
| 185–200 | [4 · Quyết định v2 và gom bài](#phase-4) | Report ba mốc trên bản sửa, tiêu chí đã ký và v1 đã chốt. |
| 200–240 | [5 · Demo và nộp](#phase-5) | Quyết định v2, report ba mốc, ticket thử và hồ sơ gom đầy đủ. |

<a id="phase-0"></a>

## Phase 0 · Chuẩn bị | Phút 0–15

### Đầu vào của từng người

| Người nhận | Đầu vào lúc bắt đầu và người bàn giao | Bàn giao trong phase và việc dùng đầu vào |
| --- | --- | --- |
| **Trưởng nhóm** | **Lab Coach / LMS →** đề và hướng dẫn Lab 10. **Người giữ bài Day 9 →** link PRD v1.1 và eval card để chọn làm bản chung. | **Từng thành viên →** họ tên, MSSV và vai đã thống nhất để điền `TEAM.md`. **Đo kiểm →** tình trạng repo và test khởi động. **Vận hành & Pháp lý →** vị trí các dữ kiện dùng cho Phiếu A. |
| **Code** | **Trưởng nhóm →** link repo Lab 10 để mở guard, helper và guide. | **Trưởng nhóm →** bộ tài liệu Day 9 chung để đối chiếu luồng xử lý. Code có thể đọc codebase ngay khi vào được repo. |
| **Đo kiểm** | **Trưởng nhóm →** link repo MALTO và quyền truy cập cần thiết. **Lab Coach / README →** URL repo mẫu để đặt `upstream`. | Có thể kiểm Python, Git và chạy test công khai ngay khi vào được repo. **Trưởng nhóm →** xác nhận quyền sau khi xử lý nếu Git báo lỗi truy cập. |
| **Vận hành & Pháp lý** | **Trưởng nhóm →** link repo Lab 10 để mở `data/world.json` và mẫu phiếu. | **Trưởng nhóm →** PRD và eval card đã chọn để chuẩn bị Phase 1. Có thể tra `staff`, `ops_limits` và `ops_facts` trước. |

**Cặp tài liệu đề xuất cho MALTO** dùng hai file đã có trong repo Day 9 của Nguyễn Xuân Khánh Linh.

- **PRD v1.1.** Đọc §3 để viết mục tiêu hệ thống ở A1 câu 1.1. Với câu 1.2, đọc §2 và §6 rồi đối chiếu vai trò kế toán đối soát và trưởng ca CSKH trong `data/world.json` của Lab 10. [Mở PRD v1.1](https://github.com/linkiewinkie/K5-L3B-Day9-Nguyen-Xuan-Khanh-Linh-Evaluation-and-Failure-Analysis/blob/main/docs/PRD_v1.1.md)
- **Eval card.** Đọc phần metric và giới hạn của bộ thử để tham khảo cách thiết kế phép đo. Bộ nền và ngưỡng chấp nhận của Lab 10 được xác định theo đề và dữ kiện Lab 10. [Mở eval card](https://github.com/linkiewinkie/K5-L3B-Day9-Nguyen-Xuan-Khanh-Linh-Evaluation-and-Failure-Analysis/blob/main/docs/eval_card.md)

| Vai | Việc cần làm | Bàn giao |
| --- | --- | --- |
| **Trưởng nhóm / Sản phẩm** | Chốt người theo bảng trên. Chọn **một** PRD v1.1 và **một** eval card làm bản tham chiếu chung. Kiểm tên repo và chế độ Public. Điền tên nhóm, lớp, repo, họ tên, MSSV, vai và đánh dấu trưởng nhóm trong `TEAM.md`. | Gửi cả nhóm link repo, tài liệu Lab 9 đã chọn và tên người phụ trách từng vai. |
| **Code** | Đọc đầu `lab10/guards.py`, `lab10/helpers.py` và Phụ lục C của guide. Xác định chỗ trợ lý đọc ticket, chuẩn bị lệnh ghi và ghi tác động. Đọc cấu trúc guard để sang Phase 1 chọn được một bước cụ thể. | Gửi Đo kiểm vị trí các bước và trường dữ liệu cần xem ở trace. |
| **Đo kiểm** | Kiểm Python 3 và Git. Kiểm `origin`, gắn `upstream` nếu thiếu. Soát danh tính Git theo MSSV và email giả theo đề. Chạy bộ test công khai. | Báo `Ran 13 tests … OK` hoặc gửi lệnh và lỗi cụ thể cho Trưởng nhóm để xử lý. |
| **Vận hành & Pháp lý** | Mở `data/world.json`, đánh dấu `staff`, `ops_limits` và `ops_facts`. Xác định chỗ lấy chức danh, ngân sách, số liệu hàng chờ, tải cao điểm và chi phí làm tay. | Gửi Trưởng nhóm vị trí các trường nguồn để chọn ngưỡng ở Phiếu A. Giữ danh sách vai LogiX để điền runbook ở B7.5. |

```powershell
git remote -v
python --version
python -m unittest discover -s tests
```

Nếu đầu ra mới có `origin`, thêm `upstream` một lần rồi kiểm lại.

```powershell
git remote add upstream https://github.com/VinUni-AI20k/K5_L3_Day10_PoC-to-Pilot_Gate1_student.git
git remote -v
```

**Cổng chuyển bước** Mọi người có quyền truy cập repo, biết phần mình sẽ viết, dùng chung PRD và eval card. Bộ test khởi động ở đây là `unittest`. Lần đánh giá trợ lý bằng `lab10.eval` bắt đầu sau khi ký ở Phase 1. [Cài đặt](../README.md#2-cài-đặt-dưới-5-phút)

<a id="phase-1"></a>

## Phase 1 · Viết và ký tiêu chí | Phút 15–65 · Phiếu A

### Đầu vào của từng người

| Người nhận | Đầu vào từ Phase 0 và người bàn giao | Bàn giao trong Phase 1 và việc dùng đầu vào |
| --- | --- | --- |
| **Trưởng nhóm** | **Vận hành & Pháp lý →** vị trí `ops_facts`, `ops_limits` và `staff`. **Tự dùng lại →** bộ PRD/eval card đã chọn. | **Đo kiểm →** cột đo offline ở A2 và cách đọc chỉ số. **Vận hành & Pháp lý →** mục tiêu hai vai LogiX, telemetry và căn cứ ngưỡng. Có thể soạn A1 và A4 trước. Dùng các đầu vào này để chốt cùng cả nhóm rồi ký. |
| **Code** | **Trưởng nhóm →** PRD và eval card chung. **Tự dùng lại →** luồng xử lý và vị trí tạo tác động đã tra ở Phase 0. | Có thể chọn bước cần đo ngay. **Đo kiểm →** phản hồi nếu tên trường hoặc cách phân biệt ca đúng/sai còn mơ hồ, để cùng chốt cột offline ở A2. |
| **Đo kiểm** | **Trưởng nhóm →** eval card và repo chung. **Code →** vị trí luồng xử lý và các trường trace đã rà ở Phase 0. | **Code →** bước cụ thể, trường cần quan sát và nguồn sự thật để hoàn thiện tử số, mẫu số của A2. Có thể đọc eval card và rà cách diễn giải A3 trước. |
| **Vận hành & Pháp lý** | **Trưởng nhóm →** PRD v1.1 chung. **Tự dùng lại →** dữ kiện về người duyệt và đối soát trong `staff`. | Có thể viết câu 1.2 và đề xuất tín hiệu ở câu 1.4 ngay. **Code →** vị trí sự kiện hoặc thao tác ghi nếu cần kiểm tín hiệu dự kiến có thể quan sát được. |

### Trưởng nhóm / Sản phẩm

1. **A1, câu 1.1.** Viết một mục tiêu cấp hệ thống cho trợ lý. Gắn với kết quả của quy trình hoàn tiền hoặc đối soát.
2. **A3, câu 1.5.** Cùng nhóm đọc khoảng tin cậy từ số minh họa trong đề. Khoanh một kết luận và giải thích trong một câu.
3. **A4, câu 1.6.** Viết từng tiêu chí theo mẫu “Nếu chỉ số vượt hoặc tụt dưới ngưỡng thì nhóm sẽ làm gì”. Dùng dữ kiện vận hành và lý do của nhóm để chọn ngưỡng. Soát ai được lợi hoặc chịu thiệt, ý nghĩa ở ngày đầu và khi pilot đã mở rộng. Ghi hai câu về hành động bị cấm và ngưỡng chuyển người duyệt ngay trên phiếu. Hẹn ngày xem lại cùng người tham dự.
4. Điền `team` đúng tên repo, `signed_by` và các nhóm trong `config/acceptance_criteria.json`.

   | Nhóm | Các trường cần rà |
   | --- | --- |
   | `required` | `pass_rate_min`, `pass_k_min`, `wrongful_refund_vnd_max`, `wrongful_carrier_faults_max`, `pii_leaks_max` |
   | `nice_to_have` | `escalation_rate_max` là chỉ số nên có |
   | `business_ops` | `cost_per_ticket_vnd_max`, `roi_min`, `queue_stuck_max` |
   | Hành động | `stop_condition` và đủ bốn dòng `decision_rule` cho Tiếp tục, Thu hẹp, Cải tiến thêm, Dừng |

### Code · Chọn bước cần đo ở A2

- **A2, câu 1.3.** Đề xuất đúng **một bước** của trợ lý. Chỉ ra hành vi cần đo, sự kiện hoặc trường thể hiện hành vi, nguồn sự thật dùng để so sánh và điểm mù. Gửi đề xuất cho Đo kiểm để chốt cột offline.

### Đo kiểm · Hoàn thiện cách tính ở A2

- Nhận bước và trường dữ liệu từ Code. Hoàn thiện cột offline của A2 gồm đơn vị, nguồn dữ liệu, người gán nhãn, tử số, mẫu số và cách xử lý ca thiếu dữ liệu. Soát công thức để hai người đọc cùng dữ liệu có thể tính ra cùng kết quả. Giúp cả nhóm kiểm cách đọc khoảng tin cậy ở A3.
- Giải thích cách đọc chỉ số khi cả nhóm chốt ngưỡng. `pass_rate` tính trên mọi lượt chạy. `pass_k` là tỷ lệ ticket đúng **cả 5/5 lần chạy**. `pass@k` là tỷ lệ ticket đúng ít nhất một lần trong k lượt.

### Vận hành & Pháp lý

1. **A1, câu 1.2.** Viết một mục tiêu cho chị Oanh, kế toán đối soát với hãng và shop, và một mục tiêu cho chị Hạnh, trưởng ca CSKH chịu hàng chờ duyệt.
2. **A2, câu 1.4.** Đề xuất telemetry để phát hiện tác hại cho bên ngoài LogiX. Ghi tín hiệu quan sát được khi vận hành không có nhãn đúng/sai, nguồn dữ liệu, cách tính, khung thời gian, ngưỡng báo động và điểm mù.
3. Gửi Trưởng nhóm căn cứ cho ngưỡng hàng chờ, tác hại với bên thứ ba và điều kiện dừng.

### Bàn giao bắt buộc | Phút 60–65

Trưởng nhóm đọc lại ngưỡng và hành động cùng cả bàn. Sau khi thống nhất, chạy theo thứ tự dưới đây. Nếu một bước lỗi, xử lý bước đó trước khi sang bước tiếp theo.

```powershell
python -m lab10.criteria sign
git add config/acceptance_criteria.json config/acceptance_criteria.lock
git commit -m "Sign acceptance criteria"
git push -u origin main
```

- [ ] Máy in **ĐÃ KÝ.** và push thành công.
- [ ] A5 có giờ ký, mã commit và trạng thái push.
- [ ] Đo kiểm đã nhận xác nhận push và mới bắt đầu đo.
- [ ] Cả nhóm giữ nguyên JSON và file khóa kể từ lúc ký.

[Phiếu A](../templates/form-a-criteria.md) · [Đề câu 1.1–1.6](../problem-set.md)

<a id="phase-2a"></a>

## Phase 2A · Đo base và tìm rủi ro | Phút 65–85 · Phiếu B

### Đầu vào của từng người

| Người nhận | Đầu vào từ Phase 1 và người bàn giao | Bàn giao trong Phase 2A và việc dùng đầu vào |
| --- | --- | --- |
| **Trưởng nhóm** | **Đo kiểm →** cách đọc chỉ số trong A2–A3. **Vận hành & Pháp lý →** mục tiêu bên liên quan và telemetry. **Tự dùng lại →** ngưỡng đã ký ở A4–A5. | **Đo kiểm →** mã và report base để đọc chi phí, ROI và phân khúc. **Code →** lỗi B2. **Vận hành & Pháp lý →** HAZOP và checklist để chọn rủi ro ở B6. Bắt đầu B3 trong lúc chờ kết quả base. |
| **Code** | **Trưởng nhóm →** ranh giới đầu ra đã chốt trong A4. **Đo kiểm →** định nghĩa phép đo A2 đã thống nhất. | **Đo kiểm →** trace `T-002@55` và bút toán liên quan để hoàn thành B2. Trong lúc chờ, có thể đọc trước luồng đọc dữ liệu và ghi kết quả. |
| **Đo kiểm** | **Trưởng nhóm →** mã commit ký, `config/acceptance_criteria.lock` và xác nhận đã push lên `origin/main`. | Chỉ bắt đầu `eval` sau xác nhận push. Sau đó lấy mã base cho B0–B1 và thu trace B2. |
| **Vận hành & Pháp lý** | **Trưởng nhóm →** điều kiện dừng và ranh giới đầu ra đã chốt ở A4. **Tự dùng lại →** mục tiêu của hai vai LogiX và nguồn telemetry từ Phiếu A. | **Đo kiểm →** mã/report base cho checklist chất lượng. **Code →** bằng chứng B2 cho phần rủi ro liên quan. **Trưởng nhóm →** nguồn dữ liệu và số chi phí cho B5. Có thể phác B4–B5 trong lúc chờ. |

Giữ code và config ở trạng thái ban đầu trong khối này.

### Đo kiểm · B0–B1 và thu trace cho B2

- **B0–B1, câu 2.1.** Chạy bộ nền ở mốc `base`. Dùng mã máy in ra để so với tiêu chí. Ghi kết quả đạt/chưa đạt, khoảng tin cậy 95% của `pass_rate`, `pass_k`, tiền hoàn sai, lỗi hãng oan, lộ dữ liệu và tỷ lệ chuyển người. Đọc phần kinh doanh–vận hành và theo kho–hãng. Ghi một lý do ủng hộ, một lý do phản đối việc để máy tự chặn bản phát hành, rồi đề xuất tự chặn, người duyệt hoặc kết hợp.
- **B2, câu 2.2.** Chạy trace `T-002@55` và chuyển dòng trace, bút toán liên quan cho Code. Gửi mã base và các chỉ số đáng lo cho Trưởng nhóm và Vận hành.

```powershell
python -m lab10.eval --suite base --stage base --note "baseline"
python -m lab10.gate --run runs/MA_LAN_CHAY/report.json
python -m lab10.trace --suite base --ticket T-002 --seed 55
```

### Code · Phân tích B2

- Nhận trace `T-002@55` từ Đo kiểm. Tìm bước sai đầu tiên, dữ kiện trợ lý đã dùng và lệnh ghi bị ảnh hưởng. Điền B2 gồm bằng chứng, ai chịu hại, mức hệ trọng, loại lỗi, nguồn và hướng xử lý.
- Bàn giao một điều kiện phòng ngừa có thể kiểm được cho buổi pre-mortem, kèm nguồn dữ liệu dùng kiểm và ví dụ ca hợp lệ cần giữ.

### Trưởng nhóm / Sản phẩm

- **B3, câu 2.3.** Lập bản đồ từ người dùng, việc cần làm và đầu ra đến dữ liệu trợ lý đọc. Với mỗi trường quan trọng, ghi nguồn sự thật hay bản sao, ai cập nhật, khi nào có thể thiếu hoặc lệch.
- Mô tả **một drift cụ thể trong ba tháng tới**. Nêu cái gì đổi, ngày nào, trường dữ liệu nào cho thấy, ngưỡng đã ký nào bị ảnh hưởng, đây là đầu vào đổi hay quan hệ đầu vào–đầu ra đổi, và chỉ số nào phát hiện.
- **Sau khi nhận report base**, xác nhận chi phí xử lý mỗi ticket, ROI, trần tiền và phân khúc kho/hãng đáng lo để đem vào B6.

### Vận hành & Pháp lý

- **B4, câu 2.4.** Làm HAZOP trên một tool ghi. Có **ít nhất ba dòng kỹ thuật**, trong đó có một nhánh chưa thấy trên trace, và **ít nhất hai dòng ngoài kỹ thuật**. Mỗi dòng ghi trường hoặc thành phần, từ gợi ý, sự sai lệch cụ thể, hậu quả cho ai và cổng có thể đặt ở đâu.
- **B5, câu 2.4.** Điền 9 nhóm việc go-live. Từng dòng có trạng thái, bằng chứng hoặc lý do không áp dụng và một PIC có tên. Xin mã lần chạy từ Đo kiểm cho mục chất lượng và dữ kiện từ Trưởng nhóm cho mục chi phí. Ghi nhận dòng còn thiếu bằng chứng để cập nhật sau sự cố.

### Cả nhóm · B6, câu 2.5

1. Dành khoảng 8–10 phút cho pre-mortem. Giả sử pilot đã phải tắt sau ba tháng. Mỗi người viết hai lý do, đọc lần lượt, gộp trùng rồi xếp theo **kỹ thuật, kinh doanh, con người và vận hành, pháp lý**. Bổ sung cho lăng kính còn trống.
2. Chọn 2–3 lý do để đưa thành cổng phòng ngừa. Với mỗi lý do, ghi tác hại, bằng chứng hoặc trường dùng kiểm, hành động cần kiểm soát và người nhận việc. Giữ các rủi ro còn lại để xem xét trong risk register.

**Bàn giao sang 2B** Mã base, B2–B6 và danh sách rủi ro ưu tiên. Người viết guard nhận nguồn dữ liệu và hành động phải kiểm soát. Người điền config nhận dữ kiện ngân sách, tải và phạm vi. [Phiếu B](../templates/form-b-evaluation-gates.md)

<a id="phase-2b"></a>

## Phase 2B · Dựng cổng và quyết định v1 | Phút 85–115 · Phiếu B

### Đầu vào của từng người

| Người nhận | Đầu vào từ Phase 2A và người bàn giao | Bàn giao trong Phase 2B và việc dùng đầu vào |
| --- | --- | --- |
| **Trưởng nhóm** | **Đo kiểm →** report base gồm chi phí, ROI, trần tiền và số theo kho/hãng. **Vận hành & Pháp lý →** rủi ro ngân sách và tải duyệt từ B4–B6. | **Vận hành & Pháp lý →** phương án người trực và xử lý ticket ngoài phạm vi để soát cổng kinh doanh. **Đo kiểm →** kết quả thử và mã `base · prepared` sau chốt để điền B8. |
| **Code** | **Trưởng nhóm →** rủi ro B6 đã phân cho cổng kỹ thuật và nguồn sự thật ở B3. **Vận hành & Pháp lý →** các dòng HAZOP liên quan. **Tự dùng lại →** phân tích lỗi B2. | Có thể viết guard ngay khi rõ rủi ro. **Đo kiểm →** kết quả hai ticket B7.3 hoặc ca bộ nền mới hỏng để sửa trước checkpoint. |
| **Đo kiểm** | **Trưởng nhóm →** rủi ro ưu tiên ở B6. **Code →** lỗi và hành vi cần kiểm từ B2. **Tự dùng lại →** mã/report base để so hồi quy. | **Vận hành & Pháp lý →** tình huống thực tế để soạn ticket thử. **Code →** guard và hành vi mong đợi. **Trưởng nhóm →** config `business`. **Vận hành & Pháp lý →** config `operations/legal`. Có thể soạn ticket trước. Nhận đủ guard và config để đo bản sẽ chốt. |
| **Vận hành & Pháp lý** | **Đo kiểm →** hàng chờ, tỷ lệ chuyển người và chi phí base. **Trưởng nhóm →** phạm vi và rủi ro ưu tiên cần đưa vào cổng từ B6. **Tự dùng lại →** HAZOP và checklist B4–B5. | **Trưởng nhóm →** phạm vi/trần dự kiến ở B7.4 để khớp runbook. **Đo kiểm →** số đo trên bản thử và prepared để kiểm tải, chi phí, thời gian chờ và tóm tắt rủi ro vận hành cho B8. |

### Code · B7.1, câu 2.6

1. Viết **2–3 cổng phòng ngừa** trong `lab10/guards.py`. Đặt ở `pre_guard(ctx)` hoặc `write_gate(ctx, action)` tùy điều kiện cần kiểm trước lúc trợ lý đọc ticket hay trước lúc ghi. Trong B7.1, nối mỗi cổng với một lý do từ B6 hoặc dòng HAZOP, nguồn dữ liệu, hành vi cho qua/chặn/chuyển người và ca hợp lệ cần giữ.
2. Bàn giao cho Đo kiểm cổng đã sẵn sàng, tính chất cần thử và ca hợp lệ cần giữ. Nhận lại ca lỗi hoặc ca mới hỏng để sửa trước checkpoint. Viết quy tắc áp dụng được khi đổi đơn, khách, ngày hoặc câu chữ.

### Đo kiểm · B0 và B7.2–B7.3, câu 2.7–2.8

1. Viết **hai bước cụ thể** tránh chỉnh quá khớp bộ nền ở B7.2. Gắn với bộ nền, ticket hành vi, gói sự cố chưa phát và test ẩn.
2. Cùng Vận hành & Pháp lý phát biểu một tính chất cần giữ và soạn **hai ticket mới** để kiểm tính chất đó. Có thể soạn theo rủi ro đã chốt trong lúc Code làm guard. Khi nhận bản guard sẵn sàng, chạy `--adhoc`, lưu đầu vào, hành vi mong đợi, kết quả thật và kết luận. Giữ ticket để phản biện lúc demo.
3. Chạy bộ test công khai và đánh giá bộ nền ở mốc `after` với cổng hiện tại. So từng ca với base, chuyển danh sách ca mới hỏng cho Code hoặc vai phụ trách config. Ghi B0 với mã lần chạy, khoảng tin cậy và thay đổi được thử. B0 cần ít nhất ba lần chạy, gồm base, thử cổng và prepared sau chốt.

```powershell
python -m lab10.eval --suite base --stage after --note "cong vong 1: mo ta thay doi"
python -m lab10.trace --suite base --stage after --adhoc "NOI_DUNG_TICKET" --order MA_DON --customer MA_KHACH
python -m unittest discover -s tests
```

### Trưởng nhóm / Sản phẩm · B7.4, câu 2.9

- Điền `business.daily_refund_cap_vnd`, `cost_budget_per_ticket_vnd`, `pilot_scope` và `roi_min`. B7.4 có giá trị thực tế và một lý do có số cho từng lựa chọn, dựa trên `ops_limits` hoặc `ops_facts`.
- Gửi Vận hành phương án phạm vi và số liệu chi phí để viết runbook. Nếu phạm vi có đổi, ghi kho hoặc tỷ lệ còn chạy và đường xử lý ticket ngoài phạm vi.
- Nhận từ Đo kiểm kết quả sau khi bật cổng. Dùng số đo để chuẩn bị nội dung B8 cùng cả nhóm.

### Vận hành & Pháp lý · B7.5–B7.6, câu 2.10

- Điền `operations` gồm PIC, người duyệt, số người trực, công suất duyệt mỗi giờ, giới hạn chờ, điều kiện dừng và kênh báo tin. Điền `legal` gồm trường dữ liệu cá nhân phải chặn khi gửi bên thứ ba và yêu cầu có nguyên nhân trong tracking trước khi ghi lỗi hãng.
- **Runbook phần 1.** Ghi người chịu trách nhiệm, người duyệt, người giữ công tắc, người nhận khiếu nại, quyền và kênh liên lạc. Đối chiếu tên/mã với `staff`.
- **Runbook phần 2.** Với các tín hiệu hàng chờ, chi phí, hoàn tiền và pháp lý, ghi nguồn số liệu, ngưỡng vàng/đỏ, hành động và người quyết.
- **Runbook phần 3.** Ghi điều kiện dừng một phần hoặc dừng hẳn, ai bấm và tối đa bao lâu sau tín hiệu đỏ, đường xử lý ticket đang chờ và điều kiện bật lại.
- **Giờ cao điểm.** Soạn trước khi biết thẻ. Ghi tải dự kiến, ai trực, mấy người, khi nào gọi thêm, khi nào thu hẹp hoặc tắt, và tác động lên chi phí/ROI khi có số đo. Đây là phần bắt buộc với S4.
- Góp một tình huống thực tế liên quan đến tác hại hoặc người duyệt khi cùng Đo kiểm soạn ticket B7.3.

### Chốt vòng 1 và ra v1 | Phút 105–115

1. **Code** xác nhận bản guard đã sẵn sàng để chốt. **Đo kiểm** xác nhận đã nhận guard từ Code và config từ Trưởng nhóm, Vận hành, kiểm kết quả thử, rồi chạy ba lệnh dưới đây. Mã dùng ở lệnh `gate` là mã của lượt **base · prepared**.

   ```powershell
   python -m lab10.checkpoint
   python -m lab10.eval --suite base --stage prepared
   python -m lab10.gate --run runs/MA_LAN_CHAY/report.json
   ```

2. **Đo kiểm** chuyển mã chạy và hash chốt. **Code** giải thích các lỗi kỹ thuật còn lại. **Vận hành & Pháp lý** đọc hàng chờ, giới hạn vận hành và pháp lý. **Trưởng nhóm** đọc chi phí, trần tiền, ROI và kho/hãng xấu nhất.
3. **Cả nhóm** chốt v1. Trưởng nhóm điền B8 gồm mã base và prepared, ba bằng chứng có số và mã chạy, dòng `decision_rule` tương ứng, giới hạn còn vướng, bằng chứng còn thiếu và ngày quyết định lại nếu phù hợp. Ghi PIC ký.
4. **Trưởng nhóm** commit và push theo lệnh cuối B8. Xác nhận `lab10/guards_round1.py`, `config/operating_gates.round1.json` và `config/round1.lock` có trên repo. Giữ nguyên ba file chốt và cột v1. Các bổ sung vòng 2 vào B3/B6/B7.6 chỉ thực hiện theo chỉ dẫn Phiếu C và đánh dấu rõ phần thêm sau sự cố.

**Bàn giao sang vòng 2** Commit v1 đã push, dấu chốt vòng 1, mã base/prepared của bộ nền, bộ 2 ticket thử. Mốc 115–125 là giờ nghỉ. Chờ Coach báo phát thẻ ở phút 125. [B8 và lệnh commit](../templates/form-b-evaluation-gates.md#b8)

<a id="phase-3a"></a>

## Phase 3A · Nhận thẻ và phân tích | Phút 125–155 · Phiếu C

### Đầu vào của từng người

| Người nhận | Đầu vào từ Phase 2B và người bàn giao | Bàn giao trong Phase 3A và việc dùng đầu vào |
| --- | --- | --- |
| **Trưởng nhóm** | **Đo kiểm →** hash chốt và report base/prepared của bộ nền dùng cho v1. **Vận hành & Pháp lý →** các giới hạn vận hành còn đáng lo. **Tự dùng lại →** commit v1 và pre-mortem B6. | **Lab Coach / người đại diện cặp bàn →** thông báo phát và số thẻ. **Đo kiểm →** report ban đầu của bộ thẻ. **Code →** nguyên nhân kỹ thuật. **Vận hành & Pháp lý →** nguyên nhân ngoài code và giả định môi trường. Dùng các bằng chứng để hoàn tất C5–C6. |
| **Code** | **Trưởng nhóm →** commit vòng 1 đã push. **Đo kiểm →** hash chốt và ca bộ nền còn hỏng, nếu có. **Tự dùng lại →** mô tả guard B7.1. | **Trưởng nhóm →** đúng số thẻ. **Đo kiểm →** chênh lệch `base · prepared` và trace có mã `ticket@seed`. Sau lượt grade ban đầu, dùng trace để điền nguồn lỗi C2 và đề xuất lá kỹ thuật cho C6. |
| **Đo kiểm** | **Trưởng nhóm →** xác nhận commit vòng 1/v1 đã push. **Tự dùng lại →** bản chốt, hash và mốc prepared bộ nền để đối chiếu. | **Trưởng nhóm →** số thẻ đã xác nhận sau khi Coach phát. Chạy grade trước sửa, rồi **Code →** ca nghi ngờ để chọn thêm trace cần dò. |
| **Vận hành & Pháp lý** | **Trưởng nhóm →** quyết định v1 và phạm vi dùng để ra v1. **Đo kiểm →** phần vận hành trong report prepared bộ nền. **Tự dùng lại →** B4–B5 và runbook 1–3. | **Trưởng nhóm →** số thẻ. **Đo kiểm →** report ban đầu của bộ thẻ, hàng chờ và trace liên quan. Dùng để làm C3–C5 và cung cấp lá ngoài kỹ thuật cho C6. |

Chỉ mở thẻ nhóm được giao.

### Phút 125–135 · Lấy số liệu trước khi sửa

1. **Trưởng nhóm** xác nhận số thẻ, ghi vào `TEAM.md` và dòng `Thẻ đã bốc:` ở đầu Phiếu C. **Đo kiểm** kéo dữ liệu và chạy grade với số thật trước khi thay đổi guard, monitor hoặc config vòng 2.
2. **Đo kiểm** gửi mã grade, mã base và prepared của **bộ thẻ** cho cả nhóm, ghi phần mã và số đo vào C0–C1. Các mã này khác bộ nền đã dùng để ra v1.
3. **Code** đọc chênh lệch base–prepared để xác định cổng vòng 1 đã chặn được gì và chọn nhóm ca cần dò. **Vận hành & Pháp lý** đọc vượt trần, hàng chờ và bên thứ ba bị ảnh hưởng. **Trưởng nhóm** điều phối đối chiếu B6 để cả nhóm ghi tác hại nào lọt qua, vì sao và thuộc lăng kính nào.

```powershell
git pull --no-rebase --no-edit --allow-unrelated-histories -X ours upstream main
python -m lab10.grade --incident Sx
```

### Phút 135–155 · Khoanh nguyên nhân có bằng chứng

| Vai | Nhiệm vụ | Nhận từ ai và bàn giao gì |
| --- | --- | --- |
| **Đo kiểm** | **C2, câu 3.1.** Dò ít nhất hai ticket hỏng theo kiểu khác nhau. Ghi `ticket@seed`, dòng trace, bên chịu hại, đơn vị đo và mức tác hại ở base của thẻ. | Nhận danh sách ca nghi ngờ từ report và Code. Gửi trace có bằng chứng cho Code và Vận hành. |
| **Code** | **C2 và C6.** Nối từng lỗi với bước, trường dữ liệu hoặc thao tác ghi. Điền ít nhất hai lỗi có nguồn khác nhau và ít nhất một lỗi chìm. Đề xuất các lá kỹ thuật cho fault tree. | Nhận trace từ Đo kiểm. Giao cho Trưởng nhóm nguyên nhân kỹ thuật có bằng chứng và vị trí có thể đặt cổng. |
| **Vận hành & Pháp lý** | **C3–C4, câu 3.1.** Làm phần riêng theo đúng thẻ và ít nhất ba dòng HAZOP của thẻ. S4 làm C1 và bổ sung mục giờ cao điểm ở B7.6 theo mẫu, không điền C3. **C5, câu 3.3.** Viết một giả định thiết kế có thể sai ngoài thực tế. | Nhận trace từ Đo kiểm và số liệu vận hành từ report. Giao nhánh về quy trình, người duyệt hoặc bên thứ ba cùng bằng chứng tương ứng. |
| **Trưởng nhóm / Sản phẩm** | **C5, câu 3.2.** Viết một yêu cầu có thể kiểm bằng code hoặc một con số trong report. Nêu điều kiện, hành vi cần bảo đảm và tác hại nếu vi phạm. Dẫn cả nhóm làm C6. | Nhận bằng chứng từ Đo kiểm, nhánh kỹ thuật từ Code và nhánh ngoài kỹ thuật từ Vận hành. Bàn giao yêu cầu kiểm chứng được để chọn cách sửa và đo lại. |

```powershell
python -m lab10.trace --suite Sx --stage base --ticket MA_TICKET --seed 11
python -m lab10.trace --suite Sx --stage prepared --ticket MA_TICKET --seed 11
```

Chạy với mã và seed của ca cần phân tích. Dùng cùng mã và seed ở hai mốc khi cần chứng minh cổng vòng 1 đã thay đổi hành vi của ca đó.

**C6, câu 3.4 · Cả nhóm.** Vẽ fault tree **trước khi sửa**. Đặt tác hại cụ thể ở đỉnh. Có ít nhất hai nhánh thuộc hai tầng khác nhau. Mỗi lá trỏ tới `ticket@seed`, trường dữ liệu hoặc một dòng report. Chốt nguyên nhân nào giao cho code, nguyên nhân nào giao cho config hoặc quy trình.

**Bàn giao sang 3B** Mã prepared ban đầu của thẻ, C2–C6 và danh sách nguyên nhân có người phụ trách. [Phiếu C](../templates/form-c-incident.md) · [Nhận thẻ](../incidents/README.md)

<a id="phase-3b"></a>

## Phase 3B · Sửa đúng nguyên nhân và đo lại | Phút 155–185 · Phiếu C

### Đầu vào của từng người

| Người nhận | Đầu vào từ Phase 3A và người bàn giao | Bàn giao trong Phase 3B và việc dùng đầu vào |
| --- | --- | --- |
| **Trưởng nhóm** | **Đo kiểm →** report trước sửa của thẻ, số vượt trần và số theo kho/hãng. **Code và Vận hành & Pháp lý →** lá kỹ thuật và lá vận hành/kinh doanh có bằng chứng. **Tự dùng lại →** C5–C6 đã tổng hợp. | **Vận hành & Pháp lý →** khả năng duyệt và luồng ticket ngoài phạm vi để chốt `business`. **Đo kiểm →** độ phủ, chi phí và ROI sau thay đổi để quyết định giữ hay chỉnh. |
| **Code** | **Trưởng nhóm →** yêu cầu C5 và nhánh kỹ thuật đã giao trong C6. **Đo kiểm →** ca hỏng, trace và số liệu trước sửa. **Vận hành & Pháp lý →** giả định môi trường hoặc yêu cầu pháp lý liên quan đến cổng. | Có thể bắt đầu guard/monitor từ bằng chứng đã có. **Đo kiểm →** trace mới, ca hồi quy và kết quả monitor để chỉnh nếu cần. **Trưởng nhóm hoặc Vận hành & Pháp lý →** giới hạn mới nếu thay config ảnh hưởng cách kiểm guard. |
| **Đo kiểm** | **Trưởng nhóm →** yêu cầu được kiểm và nhánh ưu tiên ở C5–C6. **Code →** bước sai, ca cần chạy lại và hành vi mong đợi. **Tự dùng lại →** mã/report ban đầu của thẻ và bộ nền làm mốc so sánh. | **Code →** guard, monitor và thay đổi cần đo. **Trưởng nhóm →** giá trị `business`. **Vận hành & Pháp lý →** giá trị `operations/legal`. Mỗi lần đo ghi bản đang dùng. Chạy grade cuối sau khi đã nhận đúng bản của cả ba người. |
| **Vận hành & Pháp lý** | **Trưởng nhóm →** yêu cầu C5 và nhánh người/tiền/quy trình được giao ở C6. **Đo kiểm →** tải hàng chờ, số lỗi pháp lý và tác hại trước sửa. **Tự dùng lại →** HAZOP của thẻ và giả định môi trường. | **Trưởng nhóm →** phạm vi/giới hạn kinh doanh mới. **Code →** cổng đã thêm và nhánh còn hở. **Đo kiểm →** số sau sửa cùng mã chạy. Có thể soạn thay đổi vận hành trước rồi dùng các đầu vào này để chốt C9–C11. |

### Code · C7–C8

- Sửa `lab10/guards.py` nếu nguyên nhân nằm ở luồng kỹ thuật. Giữ tiêu chí và các file chốt vòng 1 nguyên vẹn. Ghi từng sửa đổi vào C7, nối đến lá fault tree và giải thích “giảm khả năng” hay “ngăn” dưới điều kiện nào.
- Viết **ít nhất một monitor mới** trong `lab10/monitors.py` và đăng ký trong `MONITORS`. Monitor nhận các lượt chạy không có nhãn và trả về một số. C8 ghi thước đo, dữ liệu, cách tính, vì sao tín hiệu phản ánh sự cố và điểm mù nếu có. `escalation_rate` mặc định không tính là monitor mới.
- Bàn giao guard và monitor cho Đo kiểm, kèm hành vi mong đợi, tín hiệu monitor và ca cần kiểm lại. Khi Đo kiểm báo ca mới hỏng, dùng trace để khoanh nhánh code hoặc báo người phụ trách config.

### Đo kiểm · C0 và bằng chứng C7–C9

- Nhận thay đổi guard và monitor từ Code, config từ Trưởng nhóm và Vận hành. Ghi rõ thay đổi trong `--note`, lưu mã và kết luận vào C0. Chạy bộ thẻ sau sửa, kiểm lại bộ nền, rồi chạy grade để lấy báo cáo so sánh.
- Đọc ít nhất **integrity, criteria, visible, regression và monitor**. Kiểm ca mới hỏng theo `ticket@seed` và độ phủ dương, vì `visible` và `regression` cần độ phủ lớn hơn 0. Test ẩn do team chấm chạy sau buổi. Kiểm phần theo kho/hãng và gửi nhóm mọi dòng vượt trần hoặc ngưỡng chưa đạt.

```powershell
python -m lab10.eval --suite Sx --stage after --note "mo ta mot thay doi"
python -m lab10.eval --suite base --stage after --note "kiem hoi quy bo nen"
python -m lab10.grade --incident Sx
```

### Trưởng nhóm / Sản phẩm · C7

- Nếu nhánh nguyên nhân nằm ở tiền, chi phí hoặc phạm vi, sửa phần `business` trong config. Ghi giá trị trước/sau, lý do và dữ kiện hỗ trợ.
- Đọc độ phủ, chi phí mỗi ticket, ROI, trần hoàn tự động và phân khúc xấu nhất. Khi giảm phạm vi, xác định ticket ngoài phạm vi được làm tay theo cơ chế lab. Kiểm chi phí và độ phủ sau mỗi thay đổi có liên quan.
- Gửi phương án cuối cho Vận hành để cập nhật runbook và cho Đo kiểm để đo chính xác cấu hình nhóm muốn bảo vệ ở v2.

### Vận hành & Pháp lý · C7, C9–C11

- Nếu nhánh nguyên nhân nằm ở người hoặc quy trình, điều chỉnh phần `operations` hoặc `legal` tương ứng. Có thể xem xét tự động chuyển người, số người trực, kiểm mẫu, ghi chú giải thích hoặc giới hạn gửi dữ liệu, tùy bằng chứng. Giải thích tác động lên hàng chờ và chi phí.
- Bàn giao giá trị trước/sau cho Đo kiểm và nhận lại số hàng chờ, chi phí, lỗi pháp lý để cập nhật C9–C11.
- **C9.** Vẽ lại fault tree sau sửa, chỉ cổng nằm ở nhánh và tầng nào, nhánh nào vẫn hở. Ghi mã lần chạy sau sửa.
- **C10.** Thêm ít nhất một dòng risk register dựa vào nhánh còn hở hoặc mục checklist chưa có bằng chứng. Ghi rủi ro, người chịu trách nhiệm và phần theo dõi theo mẫu.
- **C11.** Cập nhật các dòng checklist có thay đổi và giữ PIC có tên. Ở runbook phần 4, ghi tín hiệu lẽ ra báo sớm, ngưỡng cũ/mới, thay đổi về người, phạm vi hoặc quy trình, và ai báo cho bên bị ảnh hưởng trong bao lâu. Ở phần 5, viết ba kịch bản tuần đầu khi lượng ticket tăng đột biến, nhà cung cấp LLM bị lỗi, hoặc người duyệt báo không tin một quyết định. Mỗi kịch bản có tín hiệu, điều kiện, người quyết và phản ứng, dựa trên bản config cuối.

**Bàn giao sang v2** Report của thẻ có `base · prepared · after`, mã ba mốc, kết quả kiểm bộ nền, monitor mới, các dòng vượt trần còn lại và nhánh chưa được xử lý. Nếu một dòng còn đỏ, khoanh nguyên nhân cụ thể để nhóm cân nhắc sửa tiếp trong thời gian còn lại hoặc phản ánh vào quyết định. [Checkpoint sự cố](../CHECKPOINTS.md)

<a id="phase-4"></a>

## Phase 4 · Quyết định v2 và gom bài | Phút 185–200

### Đầu vào của từng người

| Người nhận | Đầu vào từ các phase trước và người bàn giao | Bàn giao trong Phase 4 và việc dùng đầu vào |
| --- | --- | --- |
| **Trưởng nhóm** | **Đo kiểm →** report và mã `base · prepared · after` của bộ thẻ từ Phase 3B. **Code →** mô tả guard/monitor C7–C8. **Vận hành & Pháp lý →** nhánh còn hở, giới hạn vận hành và các mục C9–C11 đã có. **Tự dùng lại →** tiêu chí Phase 1 và v1 ở Phase 2B. | **Code →** căn cứ cho câu giảm hay ngăn. **Vận hành & Pháp lý →** phương án trực/luồng ticket và rủi ro còn lại. Dùng report đã kiểm để cả nhóm chốt v2, hoàn tất C12 và chuyển ba dòng bắt buộc cho người gom. |
| **Code** | **Đo kiểm →** kết quả after, ca mới hỏng hoặc kết quả monitor từ Phase 3B. **Tự dùng lại →** bản guard, monitor và các lá kỹ thuật tương ứng. | **Vận hành & Pháp lý →** nhánh còn hở mới nhất ở C9 nếu liên quan đến guard. Dùng kết quả đã đo để soát C7–C8 và giao Trưởng nhóm lời giải thích có bằng chứng. |
| **Đo kiểm** | **Code →** phiên bản guard/monitor cuối từ Phase 3B. **Trưởng nhóm và Vận hành & Pháp lý →** phiên bản config cuối. **Tự dùng lại →** report ba mốc và mã chạy sinh trên bản đó. | Có thể gửi số liệu cho cả nhóm ngay. **Trưởng nhóm →** phương án cuối nếu có điều chỉnh sau khi xem report. Nếu code/config đổi, đo lại và giao mã mới trước khi dùng report để chốt và gom. |
| **Vận hành & Pháp lý** | **Đo kiểm →** report cuối và mã chạy. **Code →** mô tả guard/monitor đã đo. **Trưởng nhóm →** commit ký, v1 và dữ liệu thành viên trong `TEAM.md`. **Tự dùng lại →** số thẻ và C9–C11. | Có thể nhập tên, thành viên, số thẻ và v1 trước. **Trưởng nhóm →** C12 đã chốt, quyết định v2 và ba dòng để chép vào JSON. Khi nhận đủ, chạy `--collect` và gửi các mục thiếu cho đúng người phụ trách. |

1. **Đo kiểm** gửi Trưởng nhóm mã ba mốc của thẻ, chỉ số chưa đạt trên bộ nền hoặc thẻ, kết quả monitor, ca mới hỏng nếu có và dòng “được phép cân nhắc Tiếp tục” hoặc “không đủ căn cứ”.
2. **Code** dùng report của Đo kiểm để soát C7–C8 và gửi Trưởng nhóm bằng chứng cho câu “giảm hay ngăn”. Chỉ ra điều kiện cổng đã kiểm được, nhánh còn hở và tín hiệu monitor có thể quan sát.
3. **Vận hành & Pháp lý** gửi rủi ro còn lại, ảnh hưởng bên thứ ba, nhu cầu người trực và đường xử lý ticket. Hoàn tất C11 với đúng phương án nhóm đang đề xuất.
4. **Cả nhóm** chốt v2. **Trưởng nhóm** điền C12, viết rõ giữ hay đổi so với v1, chỉ số và mã chạy hỗ trợ, kho/hãng xấu nhất, ba bằng chứng, dòng `decision_rule` tương ứng, PIC và ngày quyết định lại nếu áp dụng. Chỉ chọn **Tiếp tục** khi không còn vượt trần và các ngưỡng đã ký dùng để quyết định đều đạt.

| Nếu chọn | C12 cần nói rõ |
| --- | --- |
| **Tiếp tục** | Ngưỡng đã ký nào đạt và bằng chứng nào cho thấy phạm vi hiện tại đủ điều kiện. |
| **Thu hẹp** | Bỏ kho hoặc phần nào, còn bao nhiêu phần trăm, mấy người trực, ticket bị cắt đi đâu và số liệu nào hỗ trợ. |
| **Cải tiến thêm** | Giả thuyết cụ thể gắn với nhánh fault tree, việc cần thử và hạn đánh giá lại. |
| **Dừng** | Số liệu dẫn đến việc dừng và bài học cần ghi lại. |

**Ba dòng C12 cần được chép nguyên vào JSON.** Trưởng nhóm viết cùng hai vai còn lại.

| Trường trong `three_lines` | Nội dung nhóm phải trả lời |
| --- | --- |
| `environment_assumption` | Thiết kế dựa vào giả định môi trường nào có thể sai ngoài thực tế? |
| `reduce_or_prevent` | Biện pháp giảm khả năng hay ngăn được tác hại, và vì sao? |
| `measure_in_pilot` | Với dữ liệu mô phỏng của lab, điều gì cần đo lại khi pilot thật trước Gate 2? |

**Vận hành & Pháp lý** điền `submission/submission.json` với tên repo trong `team`, thành viên dạng `HoVaTen-MSSV` khớp `TEAM.md`, số thẻ, v1, v2 và ba dòng trên. Chạy `python -m lab10.check_submission --collect`. Nếu có `[THIẾU]`, chuyển đúng người đang phụ trách mục đó để sửa và chạy lại. Sửa phiếu tại `templates/` để lệnh gom chép lại.

**Bàn giao sang demo** C12 và JSON thống nhất, có report ba mốc và lệnh gom in **ĐỦ THÀNH PHẦN**. Đây là kiểm tra thành phần hồ sơ. Quyết định v2 vẫn phải được bảo vệ bằng tiêu chí và số liệu. [Hướng dẫn gom bài](../submission/README.md) · [Rubric](../RUBRIC.md)

<a id="phase-5"></a>

## Phase 5 · Demo, phản biện, nộp | Phút 200–240

### Đầu vào của từng người

| Người nhận | Đầu vào từ các phase trước và người bàn giao | Bàn giao trong Phase 5 và việc dùng đầu vào |
| --- | --- | --- |
| **Trưởng nhóm** | **Đo kiểm →** report ba mốc và mã chạy cuối từ Phase 4. **Code →** cổng nào giảm hay ngăn tác hại. **Vận hành & Pháp lý →** kết quả gom và rủi ro còn lại. **Tự dùng lại →** C12 và v2. | **Đo kiểm →** mã mới nếu demo phải chạy lại. **Vận hành & Pháp lý →** xác nhận gom đủ bản cuối. **Từng thành viên →** mục cá nhân đã điền trong `TEAM.md`. Dùng mã mới để sửa C12 nếu cần và đợi xác nhận hồ sơ cuối trước khi push. |
| **Code** | **Đo kiểm →** số từ report Phase 4 và trace minh họa đã lưu ở Phase 3. **Trưởng nhóm →** quyết định v2 trong C12. **Tự dùng lại →** mô tả guard/monitor vòng 2. | **Đo kiểm →** trace chạy trực tiếp nếu có ticket phản biện. Dùng trace để giải thích vì sao cổng cho qua, chặn hoặc chuyển người. Xác nhận code cuối cho Đo kiểm và người gom. |
| **Đo kiểm** | **Trưởng nhóm →** phương án v2. **Code →** hành vi mong đợi của cổng hiện tại. **Tự dùng lại →** hai ticket B7.3 từ Phase 2B và report ba mốc từ Phase 4. | **Bàn phản biện →** ticket hoặc con số muốn thử nếu có. **Trưởng nhóm và Vận hành & Pháp lý →** xác nhận giá trị config v2 cần khôi phục nếu bị đổi. Chạy lại grade khi cần và gửi mã mới cho Trưởng nhóm và người gom. |
| **Vận hành & Pháp lý** | **Trưởng nhóm →** C12 đã chốt. **Đo kiểm →** report cuối. **Tự dùng lại →** JSON, runbook và kết quả gom Phase 4. | **Code →** xác nhận code v2. **Đo kiểm →** report/mã mới nếu có chạy lại. **Trưởng nhóm →** C12 đã cập nhật nếu mã đổi. **Từng thành viên →** mục cá nhân `TEAM.md`. Gom lại, kiểm đủ và báo Trưởng nhóm sẵn sàng push. |

### Demo | Phút 200–230

- **Đo kiểm** mở report, chỉ ba mốc và đọc chỉ số thay đổi. Giữ sẵn lệnh `trace --adhoc`, mã đơn và mã khách của hai ticket B7.3 để chạy khi phản biện.
- **Code** giải thích cổng vòng 1 đã chặn gì trước khi biết thẻ, bản sửa tác động vào nhánh nào và vì sao ticket chạy thử qua hoặc bị chặn.
- **Vận hành & Pháp lý** giải thích vị trí sửa ở quy trình, số người, dữ liệu bên thứ ba hoặc ngưỡng dừng. Chuẩn bị giải thích nếu bàn phản biện đổi một con số như số người trực.
- **Trưởng nhóm** chốt phần trình bày bằng v2, con số quyết định nhất, tác hại còn lại và điều cần đo trong pilot thật. Kết thúc phần demo của bàn trong khoảng 5 phút.

### Nộp | Phút 230–240 và hạn LMS

1. **Code** xác nhận `guards.py` và `monitors.py` đúng bản v2. **Đo kiểm** khôi phục mọi config đổi thử trong demo về bản v2, đối chiếu cùng người phụ trách config. Nếu có đổi, chạy lại `python -m lab10.grade --incident Sx`. Đo kiểm cập nhật C0 và gửi mã mới cho Trưởng nhóm cập nhật C12 trước khi gom.
2. **Mỗi thành viên** tự viết mục `## HoVaTen-MSSV` trong `TEAM.md` gồm phần việc, đóng góp, bằng chứng và exit ticket. Nếu dùng AI, ghi mình đã dùng cho phần việc nào.
3. **Vận hành & Pháp lý** rà A1–A5, B0–B8, C0–C12 theo yêu cầu thẻ. Kiểm dấu thẻ, v1/v2 và thành viên. Gom lại đến khi thấy **ĐỦ THÀNH PHẦN**. Kiểm có `submission/runs/journal.jsonl`, `grade-report.json`, `grade-report.md`, report ba mốc và `submission/manifest.json`.
4. **Trưởng nhóm** xem danh sách file staged, commit và push trước phút 240. Xác nhận repo Public và các file cần nộp đã xuất hiện trên GitHub. Gửi link repo cho Coach theo hướng dẫn.

   ```powershell
   git add -u
   git add submission templates TEAM.md
   git diff --cached --name-only
   git commit -m "LAB 10: bai nop"
   git push -u origin main
   ```

5. **Mỗi thành viên** tự nộp link repo trên LMS bằng tài khoản cá nhân. Hạn **trước 23:59 GMT+7 cùng ngày** đối với lab sáng, **trước 11:59 GMT+7 hôm sau** đối với lab chiều/tối. Nếu lỗi push hay kéo thẻ, báo Coach trong buổi. Sau buổi, gửi mô tả lỗi kèm ảnh lệnh và output trước hạn.

[Quy định nộp](../SUBMISSION.md) · [Luật và sử dụng AI](../RULES.md)

## Người xử lý khi một mốc bị kẹt

| Tình huống | Người xử lý | Việc cần làm |
| --- | --- | --- |
| Chưa push được commit ký | Trưởng nhóm | Kiểm quyền ghi và remote, xử lý hoặc báo Coach. Đo kiểm chờ push thành công mới chạy eval. |
| Chưa thấy thẻ khi kéo | Đo kiểm | Kiểm remote `upstream` và thông báo phát thẻ của Coach. Báo Coach nếu vẫn thiếu sau khi đã kéo đúng lệnh. |
| Report báo hồi quy | Đo kiểm lấy trace, Code phân tích | Dò cùng `ticket@seed` ở base và after, tìm nhánh làm hỏng ca trước đó đúng rồi kiểm lại. Nếu lỗi do phạm vi hoặc cổng số, đưa cho người phụ trách config tương ứng. |
| Monitor chưa sáng đèn | Code sửa, Đo kiểm chạy lại | Kiểm đã đăng ký trong `MONITORS`, chạy được trên dữ liệu không nhãn và phản ánh tín hiệu khác giữa gói sự cố với bộ nền. |
| Hàng chờ, chi phí hoặc trần đỏ | Vận hành hoặc Trưởng nhóm theo chỉ số | Ghi rõ số đo, ngưỡng và bộ ticket nào vượt. Kiểm tác động của phương án điều chỉnh lên độ phủ, thời gian chờ và chi phí. Dùng kết quả cuối để chốt v2. |
| Lệnh gom báo thiếu hoặc report cũ | Vận hành & Pháp lý | Chuyển dòng `[THIẾU]` cho chủ mục. Nếu report không khớp code/config cuối, nhờ Đo kiểm chạy grade rồi gom lại. |

## Mẫu bàn giao để cả nhóm dùng khi chạy lab

Dán từng dòng vào kênh nhóm khi hoàn tất mốc. Người nhận xác nhận đã có đúng đầu vào rồi bắt đầu phần việc tiếp theo.

```text
Trưởng nhóm → Đo kiểm | Commit ký ___ | giờ ký ___ | đã push origin/main ___ | bắt đầu eval base
Đo kiểm → Code + Trưởng nhóm + Vận hành | Mã base ___ | ngưỡng chưa đạt ___ | ticket@seed ___ | kho/hãng đáng lo ___
Code → Đo kiểm | Guard vòng 1 ___ | hành vi mong đợi ___ | ca hợp lệ cần giữ ___
Trưởng nhóm → Đo kiểm | Config business ___ | phạm vi pilot ___
Vận hành → Đo kiểm | Config operations/legal ___ | người trực ___ | giới hạn chờ ___
Đo kiểm → Trưởng nhóm | Hash chốt ___ | mã base · prepared bộ nền ___
Trưởng nhóm → Cả nhóm | v1 ___ | commit đã push ___ | số thẻ khi Coach phát ___
Đo kiểm → Cả nhóm | Grade đầu tiên của thẻ ___ | base ___ | prepared ___ | tác hại trước sửa ___
Code → Đo kiểm | Guard / monitor sau sửa ___ | lá fault tree ___ | chỉ số cần đo lại ___
Đo kiểm → Trưởng nhóm + Vận hành | Report cuối | base ___ | prepared ___ | after ___ | vượt trần còn lại ___
Trưởng nhóm → Vận hành | v2 ___ | C12 ___ | ba dòng để chép vào JSON ___
Vận hành → Trưởng nhóm | Kết quả --collect ___ | hồ sơ đã sẵn sàng push ___
Trưởng nhóm → Cả nhóm | Commit cuối ___ | link repo ___ | từng người tự nộp LMS
```
