# ⚡ Hướng dẫn Nhanh - Staff Manager

## 🚀 5 Phút Bắt đầu

### Bước 1: Cài đặt (2 phút)
```bash
# Cài dependencies
pip install xlrd xlsxwriter

# Restart Odoo
sudo systemctl restart odoo

# Hoặc nếu dùng .venv
source /opt/odoo18/.venv/bin/activate
pip install xlrd xlsxwriter
```

### Bước 2: Kích hoạt Module (1 phút)
1. Đăng nhập Odoo với quyền Administrator
2. Vào **Apps** (Ứng dụng)
3. Nhấn **Update Apps List** (Cập nhật danh sách)
4. Tìm "**Staff Manager**"
5. Nhấn **Install** (Cài đặt)

### Bước 3: Sử dụng ngay (2 phút)

#### 🎯 Tình huống 1: Import nhân viên từ Excel
```
1. Menu: Staff Manager > Cấu hình > Import nhân viên
2. Nhấn "Tải file mẫu"
3. Mở file, thêm nhân viên của bạn
4. Upload file, nhấn "Import"
5. ✅ Xong! Kiểm tra danh sách nhân viên
```

#### 🎯 Tình huống 2: Tạo nhân viên thủ công
```
1. Menu: Staff Manager > Nhân viên
2. Nhấn "Tạo"
3. Điền thông tin:
   - Mã NV: NV001
   - Tên: Nguyễn Văn A
   - SĐT: 0901234567
   - Phòng ban: Kinh doanh
   - Khu vực: Hà Nội
4. Lưu
5. ✅ Xong!
```

#### 🎯 Tình huống 3: Ghi nhận cuộc gọi
```
1. Menu: Staff Manager > Lịch sử cuộc gọi
2. Nhấn "Tạo"
3. Chọn nhân viên: [NV001] Nguyễn Văn A
4. Trạng thái: Đã trả lời
5. Thời lượng: 5.5 phút
6. Lưu
7. ✅ Thống kê nhân viên tự động cập nhật!
```

#### 🎯 Tình huống 4: Xem thống kê
```
1. Menu: Staff Manager > Lịch sử cuộc gọi
2. Nhấn icon "Pivot" hoặc "Graph"
3. Kéo thả để phân tích:
   - Phòng ban vs Trạng thái
   - Khu vực vs Thời lượng
4. ✅ Có ngay báo cáo trực quan!
```

#### 🎯 Tình huống 5: Quản lý hệ thống
```
1. Menu: Staff Manager > Trạng thái hệ thống
2. Tạo cấu hình:
   - Tên: Hệ thống chính
   - Max calls: 100
3. Nhấn button "Bật hệ thống"
4. ✅ Hệ thống đã sẵn sàng!
```

## 📊 Các View Hữu ích

### Tree View (Danh sách)
- Xem tổng quan tất cả bản ghi
- Màu sắc phân biệt trạng thái
- Sort nhanh theo cột

### Form View (Chi tiết)
- Xem/sửa đầy đủ thông tin
- Notebook tabs cho related data
- Button actions nhanh

### Pivot View (Thống kê)
- Phân tích đa chiều
- Kéo thả để group
- Export ra Excel

### Graph View (Biểu đồ)
- Bar chart, Pie chart, Line chart
- Trực quan hóa dữ liệu
- Thay đổi measure dễ dàng

## 🔍 Search & Filter Pro Tips

### Nhân viên
```
Tìm nhanh:
- Gõ "NV001" → Tìm theo mã
- Gõ "Nguyễn" → Tìm theo tên
- Gõ "0901" → Tìm theo SĐT

Filter:
- "Có cuộc gọi" → Nhân viên đã có call
- "Chưa có cuộc gọi" → Nhân viên chưa call

Group by:
- "Phòng ban" → Nhóm theo phòng
- "Khu vực" → Nhóm theo khu vực
```

### Lịch sử cuộc gọi
```
Filter nhanh:
- "Hôm nay" → Cuộc gọi hôm nay
- "7 ngày qua" → Tuần này
- "30 ngày qua" → Tháng này
- "Đã trả lời" → Chỉ answered
- "Chưa trả lời" → Chỉ unanswered

Group by:
- "Nhân viên" → Theo từng nhân viên
- "Trạng thái" → Answered vs Unanswered
- "Thời gian gọi" → Theo ngày/tuần/tháng
```

## 💡 Tips & Tricks

### 1. Import Excel Nhanh
- Luôn dùng file mẫu để tránh lỗi format
- Bật "Skip validation" nếu SĐT không theo chuẩn VN
- Bật "Update existing" để cập nhật thay vì tạo mới

### 2. Thống kê Hiệu quả
- Dùng Pivot view cho phân tích sâu
- Dùng Graph view cho báo cáo trực quan
- Save favorite filters để tái sử dụng

### 3. Quản lý Nhanh
- Dùng Archive thay vì Delete để giữ lịch sử
- Dùng Group by để tổ chức dữ liệu
- Dùng Search bar cho tìm kiếm nhanh

### 4. Workflow Tối ưu
```
Workflow đề xuất:
1. Import nhân viên từ Excel (1 lần)
2. Hệ thống tự động ghi call logs
3. Xem thống kê định kỳ (Pivot/Graph)
4. Export báo cáo khi cần
```

## 🎓 Video Tutorials (Sắp có)

- [ ] 01. Cài đặt và Setup
- [ ] 02. Import Nhân viên từ Excel
- [ ] 03. Quản lý Cuộc gọi
- [ ] 04. Thống kê và Báo cáo
- [ ] 05. Tips & Tricks

## 📱 Keyboard Shortcuts

- `Alt + C` → Tạo mới (Create)
- `Alt + E` → Sửa (Edit)
- `Alt + S` → Lưu (Save)
- `Alt + D` → Hủy (Discard)
- `Ctrl + K` → Search
- `← →` → Navigate giữa records

## ❓ FAQ - Câu hỏi Thường gặp

### Q: Làm sao import nhiều nhân viên cùng lúc?
**A:** Sử dụng tính năng Import Excel:
1. Tải file mẫu
2. Điền thông tin vào Excel
3. Upload và import

### Q: Số điện thoại không đúng định dạng?
**A:** SĐT phải theo format: `0xxxxxxxxx` (10-11 số, bắt đầu bằng 0)  
Hoặc bật "Skip validation" khi import

### Q: Thống kê không tự động cập nhật?
**A:** Refresh lại trang hoặc F5. Computed fields sẽ tự động tính toán.

### Q: Làm sao xóa nhân viên nhưng giữ lịch sử?
**A:** Dùng Archive (nút Archive ở form view) thay vì Delete

### Q: Export dữ liệu ra Excel?
**A:** Chọn records > Action > Export (tính năng mặc định của Odoo)

### Q: Phân quyền cho user?
**A:** Settings > Users > Chọn user > Thêm group "Staff Manager"

## 🆘 Cần Trợ giúp?

### Tài liệu
- 📖 README.md - Tổng quan đầy đủ
- 🔧 INSTALL.md - Hướng dẫn cài đặt
- 🧪 TESTING.md - Checklist kiểm tra
- 📋 SUMMARY.md - Tóm tắt module

### Liên hệ
- 📧 Email: support@yourcompany.com
- 🌐 Website: https://www.yourcompany.com
- 📞 Hotline: 1900-xxxx

## ⭐ Đánh giá Module

Nếu module hữu ích, đừng quên:
- ⭐ Rate 5 sao trên Odoo Apps Store
- 💬 Để lại review
- 🔗 Share với đồng nghiệp

---

## 🎯 Next Steps

Sau khi đã làm quen:
1. ✅ Đọc README.md để hiểu sâu hơn
2. ✅ Chạy qua TESTING.md checklist
3. ✅ Tùy chỉnh theo nhu cầu của bạn
4. ✅ Tích hợp với hệ thống hiện có

**Chúc bạn sử dụng hiệu quả! 🚀**

---
*Staff Manager v18.0.1.1.0 - © 2024 Your Company*

