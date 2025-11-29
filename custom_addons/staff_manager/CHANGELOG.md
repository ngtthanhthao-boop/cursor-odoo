# Changelog - Staff Manager Module

Tất cả những thay đổi quan trọng của module này sẽ được ghi lại trong file này.

## [18.0.1.1.0] - 2024-11-29

### Phát hành ban đầu

#### Tính năng mới
- ✅ **Quản lý Nhân viên**
  - Tạo, sửa, xóa thông tin nhân viên
  - Mã nhân viên duy nhất (unique constraint)
  - Validate số điện thoại theo chuẩn Việt Nam (0xxxxxxxxx)
  - Thống kê tự động: tổng cuộc gọi, đã trả lời, chưa trả lời
  - Tìm kiếm theo: mã NV, tên, SĐT, phòng ban, khu vực
  - Lọc theo: có cuộc gọi, chưa có cuộc gọi, hoạt động
  - Nhóm theo: phòng ban, khu vực

- ✅ **Lịch sử Cuộc gọi**
  - Ghi nhận chi tiết cuộc gọi: thời gian, trạng thái, thời lượng
  - Trạng thái: Đã trả lời / Chưa trả lời
  - Lưu trữ phím phản hồi (response_key)
  - Lưu trữ URL file ghi âm (WAV)
  - Tự động liên kết thông tin nhân viên (mã NV, SĐT, phòng ban, khu vực)
  - Lọc theo: trạng thái, hôm nay, 7 ngày, 30 ngày
  - Nhóm theo: nhân viên, trạng thái, phòng ban, khu vực, thời gian
  - Hỗ trợ Pivot View và Graph View cho thống kê
  - Màu sắc tự động: xanh (answered), đỏ (unanswered)

- ✅ **Trạng thái Hệ thống**
  - Quản lý cấu hình hệ thống
  - Trạng thái: Bật/Tắt
  - Thiết lập số cuộc gọi tối đa (1-10,000)
  - Quản lý file nội dung (text)
  - Button action: Bật/Tắt hệ thống
  - Theo dõi: thời gian cập nhật, người cập nhật
  - Validation: số cuộc gọi tối đa không âm và không vượt quá 10,000

- ✅ **Import từ Excel**
  - Import hàng loạt nhân viên từ file Excel
  - Hỗ trợ định dạng .xls và .xlsx
  - Tùy chọn: Cập nhật bản ghi có sẵn (theo mã nhân viên)
  - Tùy chọn: Bỏ qua validate số điện thoại
  - Báo cáo chi tiết: số bản ghi tạo mới, cập nhật, lỗi
  - Chi tiết lỗi: dòng nào, lỗi gì
  - Tải file Excel mẫu với dữ liệu demo
  - Logging đầy đủ quá trình import

#### Models
- `staff.manager.staff` - Nhân viên
- `staff.manager.call.log` - Lịch sử cuộc gọi
- `staff.manager.system.status` - Trạng thái hệ thống
- `staff.manager.import.wizard` - Import wizard (transient)

#### Views
- Tree, Form, Search views cho tất cả models
- Pivot và Graph views cho Call Log
- Wizard form cho Import
- Menu structure hoàn chỉnh

#### Security
- Access rights cho User và System Administrator
- User: đọc, ghi, tạo (không xóa system status)
- Admin: toàn quyền

#### External Dependencies
- xlrd: Đọc file Excel (.xls)
- xlsxwriter: Tạo file Excel mẫu (.xlsx)

#### Logging
- Sử dụng Python logging thay vì print
- Log các action quan trọng: create, update, import
- Log level: INFO cho thành công, ERROR cho lỗi

#### Validation
- Mã nhân viên: required, unique
- Họ tên: required
- Phòng ban, khu vực: required
- Số điện thoại: format 0xxxxxxxxx (10-11 số)
- Thời lượng cuộc gọi: không âm
- Số cuộc gọi tối đa: 0-10,000

#### UI/UX Improvements
- Icon module chuyên nghiệp
- Màu sắc phân biệt trạng thái
- Button actions với notification
- Help text đầy đủ cho các trường
- Empty state messages
- Alert và hướng dẫn trong wizard

### Tài liệu
- ✅ README.md: Tổng quan và hướng dẫn sử dụng
- ✅ INSTALL.md: Hướng dẫn cài đặt chi tiết
- ✅ CHANGELOG.md: Lịch sử thay đổi
- ✅ index.html: Mô tả module (App Store)
- ✅ requirements.txt: Dependencies

## Kế hoạch phát triển

### [18.0.1.2.0] - Sắp tới
- 📋 Export dữ liệu ra Excel
- 📋 Email notification cho cuộc gọi quan trọng
- 📋 Dashboard thống kê tổng quan
- 📋 Báo cáo cuộc gọi theo tuần/tháng
- 📋 Tích hợp với calendar
- 📋 SMS notification

### [18.0.2.0.0] - Tương lai
- 📋 API integration cho hệ thống gọi tự động
- 📋 Phân quyền chi tiết hơn
- 📋 Multi-company support
- 📋 Scheduled actions tự động
- 📋 Advanced analytics

## Hỗ trợ

Nếu bạn gặp vấn đề hoặc có đề xuất cải tiến, vui lòng liên hệ:
- Email: support@yourcompany.com
- Website: https://www.yourcompany.com

## Giấy phép

LGPL-3

