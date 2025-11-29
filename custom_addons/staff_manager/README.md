# Staff Manager - Module Quản Lý Nhân Viên và Cuộc Gọi

## Tổng quan
Module Staff Manager cho phép quản lý thông tin nhân viên và theo dõi lịch sử cuộc gọi một cách hiệu quả.

## Tính năng chính

### 1. Quản lý Nhân viên
- Lưu trữ thông tin nhân viên: mã nhân viên, họ tên, số điện thoại, phòng ban, khu vực
- Tự động validate số điện thoại theo định dạng Việt Nam (0xxxxxxxxx)
- Thống kê tự động số cuộc gọi (tổng, đã trả lời, chưa trả lời)
- Tìm kiếm và lọc nhân viên theo phòng ban, khu vực

### 2. Lịch sử Cuộc gọi
- Ghi nhận chi tiết từng cuộc gọi: thời gian, trạng thái, thời lượng
- Lưu trữ phím phản hồi và URL ghi âm
- Tự động liên kết với thông tin nhân viên
- Thống kê và báo cáo cuộc gọi theo nhiều tiêu chí
- Hỗ trợ xem dạng Pivot và Graph

### 3. Trạng thái Hệ thống
- Quản lý cấu hình hệ thống (bật/tắt)
- Thiết lập số cuộc gọi tối đa
- Quản lý file nội dung
- Theo dõi lịch sử cập nhật

### 4. Import dữ liệu
- Import nhân viên từ file Excel
- Hỗ trợ cập nhật hoặc tạo mới
- Tùy chọn bỏ qua validate số điện thoại
- Báo cáo chi tiết kết quả import
- Tải file Excel mẫu

## Cài đặt

### Yêu cầu
- Odoo 18.0
- Python packages: xlrd, xlsxwriter

### Cài đặt dependencies
```bash
pip install xlrd xlsxwriter
```

### Cài đặt module
1. Copy thư mục `staff_manager` vào `custom_addons`
2. Cập nhật danh sách apps trong Odoo
3. Tìm và cài đặt module "Staff Manager"

## Cấu trúc dữ liệu

### Model: staff.manager.staff (Nhân Viên)
- `employee_code`: Mã nhân viên (duy nhất)
- `name`: Họ tên đầy đủ
- `phone`: Số điện thoại
- `department`: Phòng ban
- `area`: Khu vực
- `total_calls`: Tổng số cuộc gọi (computed)
- `answered_calls`: Cuộc gọi đã trả lời (computed)
- `unanswered_calls`: Cuộc gọi chưa trả lời (computed)

### Model: staff.manager.call.log (Lịch Sử Cuộc Gọi)
- `call_time`: Thời gian gọi
- `staff_id`: Nhân viên (many2one)
- `status`: Trạng thái (answered/unanswered)
- `duration`: Thời lượng (phút)
- `response_key`: Phím phản hồi
- `record_url`: URL ghi âm

### Model: staff.manager.system.status (Trạng Thái Hệ Thống)
- `name`: Tên cấu hình
- `status`: Trạng thái (on/off)
- `max_calls`: Số cuộc gọi tối đa
- `content_file`: File nội dung

### Model: staff.manager.import.wizard (Import Wizard)
- `file_data`: File Excel
- `update_existing`: Cập nhật bản ghi có sẵn
- `skip_validation`: Bỏ qua validate số điện thoại

## Hướng dẫn sử dụng

### Import nhân viên từ Excel
1. Vào menu: Staff Manager > Cấu hình > Import nhân viên
2. Tải file mẫu hoặc chuẩn bị file Excel với cấu trúc:
   - Cột A: Mã nhân viên
   - Cột B: Họ tên đầy đủ
   - Cột C: Số điện thoại
   - Cột D: Phòng ban
   - Cột E: Khu vực
3. Chọn file và các tùy chọn import
4. Nhấn "Import" để thực hiện

### Quản lý cuộc gọi
1. Vào menu: Staff Manager > Lịch sử cuộc gọi
2. Tạo mới hoặc xem danh sách cuộc gọi
3. Sử dụng bộ lọc: Hôm nay, 7 ngày qua, 30 ngày qua
4. Xem thống kê qua Pivot hoặc Graph view

### Cấu hình hệ thống
1. Vào menu: Staff Manager > Trạng thái hệ thống
2. Tạo hoặc chỉnh sửa cấu hình
3. Sử dụng nút "Bật/Tắt hệ thống" để điều khiển

## Bảo mật
- User thường: Có quyền đọc, ghi, tạo nhân viên và cuộc gọi
- System Administrator: Có toàn quyền trên tất cả models

## Tác giả
Your Company

## Giấy phép
LGPL-3

## Hỗ trợ
Để được hỗ trợ, vui lòng liên hệ: support@yourcompany.com

## Changelog

### Version 18.0.1.1.0
- Phát hành ban đầu
- Quản lý nhân viên
- Lịch sử cuộc gọi
- Import từ Excel
- Quản lý trạng thái hệ thống

