# 🧪 Hướng dẫn Kiểm tra Module Staff Manager

## Checklist Kiểm tra sau Cài đặt

### ✅ Bước 1: Kiểm tra Menu
- [ ] Menu "Staff Manager" xuất hiện trên thanh menu chính
- [ ] Submenu "Nhân viên" hoạt động
- [ ] Submenu "Lịch sử cuộc gọi" hoạt động  
- [ ] Submenu "Trạng thái hệ thống" hoạt động
- [ ] Submenu "Cấu hình > Import nhân viên" hoạt động

### ✅ Bước 2: Test Model Nhân Viên

#### 2.1 Tạo Nhân viên
1. Vào menu: **Staff Manager > Nhân viên**
2. Nhấn nút **Tạo**
3. Nhập thông tin:
   - Mã nhân viên: `NV001`
   - Họ tên: `Nguyễn Văn A`
   - Số điện thoại: `0901234567`
   - Phòng ban: `Kinh doanh`
   - Khu vực: `Hà Nội`
4. Nhấn **Lưu**
5. **Kết quả mong đợi:** Tạo thành công, hiển thị `[NV001] Nguyễn Văn A`

#### 2.2 Test Validation Số điện thoại
1. Tạo nhân viên mới
2. Nhập số điện thoại sai: `123456` hoặc `abcdefgh`
3. Nhấn Lưu
4. **Kết quả mong đợi:** Hiện lỗi "Số điện thoại không đúng định dạng Việt Nam!"

#### 2.3 Test Unique Constraint
1. Tạo nhân viên mới với mã đã tồn tại: `NV001`
2. Nhấn Lưu
3. **Kết quả mong đợi:** Hiện lỗi "Mã nhân viên phải là duy nhất!"

#### 2.4 Test Computed Fields
1. Mở nhân viên `NV001`
2. Kiểm tra:
   - Tổng số cuộc gọi: 0
   - Cuộc gọi đã trả lời: 0
   - Cuộc gọi chưa trả lời: 0
3. **Kết quả mong đợi:** Tất cả = 0 khi chưa có cuộc gọi

#### 2.5 Test Search & Filter
1. Tạo thêm 2-3 nhân viên
2. Test search theo:
   - [ ] Mã nhân viên
   - [ ] Tên
   - [ ] Số điện thoại
   - [ ] Phòng ban
   - [ ] Khu vực
3. Test filter:
   - [ ] "Có cuộc gọi"
   - [ ] "Chưa có cuộc gọi"
4. Test group by:
   - [ ] Phòng ban
   - [ ] Khu vực

### ✅ Bước 3: Test Model Lịch Sử Cuộc Gọi

#### 3.1 Tạo Cuộc gọi
1. Vào menu: **Staff Manager > Lịch sử cuộc gọi**
2. Nhấn nút **Tạo**
3. Nhập thông tin:
   - Thời gian gọi: (auto fill)
   - Nhân viên: Chọn `[NV001] Nguyễn Văn A`
   - Trạng thái: `Đã trả lời`
   - Thời lượng: `5.5` (5 phút 30 giây)
   - Phím phản hồi: `1`
4. Nhấn **Lưu**
5. **Kết quả mong đợi:** 
   - Tạo thành công
   - Mã nhân viên, SĐT, Phòng ban, Khu vực tự động điền
   - Dòng màu xanh (answered)

#### 3.2 Test Related Fields
1. Mở cuộc gọi vừa tạo
2. Kiểm tra:
   - [ ] Mã nhân viên = `NV001`
   - [ ] Số điện thoại = `0901234567`
   - [ ] Phòng ban = `Kinh doanh`
   - [ ] Khu vực = `Hà Nội`
3. **Kết quả mong đợi:** Tất cả tự động điền từ nhân viên

#### 3.3 Test Onchange Status
1. Tạo cuộc gọi mới
2. Chọn trạng thái: `Chưa trả lời`
3. **Kết quả mong đợi:** Thời lượng tự động = 0.0

#### 3.4 Test Duration Validation
1. Tạo cuộc gọi mới
2. Nhập thời lượng: `-5`
3. Nhấn Lưu
4. **Kết quả mong đợi:** Hiện lỗi "Thời lượng cuộc gọi không thể âm!"

#### 3.5 Test Computed Fields Update
1. Quay lại nhân viên `NV001`
2. Kiểm tra:
   - Tổng số cuộc gọi: 1
   - Cuộc gọi đã trả lời: 1
   - Cuộc gọi chưa trả lời: 0
3. **Kết quả mong đợi:** Thống kê tự động cập nhật

#### 3.6 Test Views
1. **Tree View:**
   - [ ] Màu xanh cho "Đã trả lời"
   - [ ] Màu đỏ cho "Chưa trả lời"

2. **Pivot View:**
   - [ ] Chuyển sang Pivot view
   - [ ] Group theo Phòng ban (row) và Trạng thái (col)
   - [ ] Hiển thị thống kê đúng

3. **Graph View:**
   - [ ] Chuyển sang Graph view
   - [ ] Hiển thị biểu đồ cột theo trạng thái

#### 3.7 Test Filters
1. Tạo thêm cuộc gọi với ngày khác nhau
2. Test filter:
   - [ ] "Hôm nay"
   - [ ] "7 ngày qua"
   - [ ] "30 ngày qua"
3. Test group by:
   - [ ] Nhân viên
   - [ ] Trạng thái
   - [ ] Thời gian gọi (day)

### ✅ Bước 4: Test Model Trạng Thái Hệ Thống

#### 4.1 Tạo Cấu hình
1. Vào menu: **Staff Manager > Trạng thái hệ thống**
2. Nhấn nút **Tạo**
3. Nhập:
   - Tên cấu hình: `Hệ thống chính`
   - Trạng thái: `Tắt`
   - Số cuộc gọi tối đa: `100`
   - File nội dung: `Nội dung test`
4. Nhấn **Lưu**
5. **Kết quả mong đợi:** Tạo thành công, dòng màu xám (off)

#### 4.2 Test Button Actions
1. Mở cấu hình vừa tạo
2. Nhấn nút **Bật hệ thống**
3. **Kết quả mong đợi:**
   - Hiển thị notification "Đã bật hệ thống"
   - Trạng thái chuyển sang "Bật"
   - Dòng chuyển màu xanh
4. Nhấn nút **Tắt hệ thống**
5. **Kết quả mong đợi:**
   - Hiển thị notification "Đã tắt hệ thống"
   - Trạng thái chuyển sang "Tắt"

#### 4.3 Test Auto Update Fields
1. Mở cấu hình
2. Sửa "Số cuộc gọi tối đa": `200`
3. Nhấn Lưu
4. **Kết quả mong đợi:**
   - "Cập nhật lần cuối" = thời gian hiện tại
   - "Người cập nhật" = user hiện tại

#### 4.4 Test Validation
1. Tạo cấu hình mới
2. Nhập số cuộc gọi tối đa: `-10`
3. Nhấn Lưu
4. **Kết quả mong đợi:** Hiện lỗi "Số cuộc gọi tối đa không thể âm!"

5. Nhập số cuộc gọi tối đa: `20000`
6. Nhấn Lưu
7. **Kết quả mong đợi:** Hiện lỗi "Số cuộc gọi tối đa không thể vượt quá 10,000!"

### ✅ Bước 5: Test Import Wizard

#### 5.1 Tải File Mẫu
1. Vào menu: **Staff Manager > Cấu hình > Import nhân viên**
2. Nhấn nút **Tải file mẫu**
3. **Kết quả mong đợi:** Download file `Staff_Import_Template.xlsx`
4. Mở file, kiểm tra:
   - [ ] Header: Mã nhân viên, Họ tên, SĐT, Phòng ban, Khu vực
   - [ ] 3 dòng dữ liệu mẫu

#### 5.2 Test Import Thành công
1. Chuẩn bị file Excel với 3 nhân viên mới:
   ```
   NV101 | Trần Văn B | 0912345678 | Marketing | TP.HCM
   NV102 | Lê Thị C | 0923456789 | Kỹ thuật | Đà Nẵng
   NV103 | Phạm Văn D | 0934567890 | Hành chính | Hà Nội
   ```
2. Import file
3. **Kết quả mong đợi:**
   - Notification: "Tạo mới: 3 | Cập nhật: 0 | Lỗi: 0"
   - Log chi tiết: 3 tạo mới, 0 lỗi
4. Kiểm tra danh sách nhân viên: 3 bản ghi mới xuất hiện

#### 5.3 Test Import với Update
1. Sửa file Excel: thay tên `Trần Văn B` → `Trần Văn B Updated`
2. Chọn tùy chọn: **Cập nhật bản ghi có sẵn**
3. Import file
4. **Kết quả mong đợi:**
   - Tạo mới: 0 | Cập nhật: 1 | Lỗi: 0
   - Nhân viên NV101 có tên mới

#### 5.4 Test Validation Errors
1. Chuẩn bị file Excel với lỗi:
   ```
   NV104 | Nguyễn Văn E | 123 | IT | HN          (SĐT sai)
   NV105 |             | 0945678901 | IT | HN    (Thiếu tên)
         | Lê Văn F    | 0956789012 | IT | HN    (Thiếu mã)
   ```
2. Import file (không skip validation)
3. **Kết quả mong đợi:**
   - Lỗi: 3
   - Log chi tiết từng lỗi:
     - Dòng 2: SĐT không đúng định dạng
     - Dòng 3: Thiếu tên
     - Dòng 4: Thiếu mã nhân viên

#### 5.5 Test Skip Validation
1. Chuẩn bị file với SĐT sai: `NV106 | Test | 123 | IT | HN`
2. Chọn: **Bỏ qua validate số điện thoại**
3. Import
4. **Kết quả mong đợi:** Import thành công dù SĐT sai format

### ✅ Bước 6: Test Integration

#### 6.1 Workflow Đầy đủ
1. Import 5 nhân viên từ Excel
2. Tạo 10 cuộc gọi cho các nhân viên
3. Kiểm tra:
   - [ ] Thống kê nhân viên cập nhật đúng
   - [ ] Pivot view hiển thị đúng
   - [ ] Graph view hiển thị đúng
4. Archive 1 nhân viên
5. Kiểm tra:
   - [ ] Nhân viên không hiển thị trong danh sách mặc định
   - [ ] Cuộc gọi vẫn tồn tại
6. Bật hệ thống
7. Kiểm tra notification

### ✅ Bước 7: Test Performance

#### 7.1 Bulk Import
1. Chuẩn bị file Excel với 100 nhân viên
2. Import file
3. **Kết quả mong đợi:** 
   - Import thành công trong < 30 giây
   - Log đầy đủ
   - Không có memory error

#### 7.2 Large Dataset
1. Tạo 1000 cuộc gọi (có thể dùng script Python)
2. Mở Pivot view
3. **Kết quả mong đợi:**
   - Load trong < 5 giây
   - Không có performance issue

### ✅ Bước 8: Test Security

#### 8.1 User Rights
1. Login với user thường (không phải admin)
2. Kiểm tra quyền:
   - [ ] Tạo/sửa nhân viên: OK
   - [ ] Tạo/sửa cuộc gọi: OK
   - [ ] Tạo/sửa system status: OK
   - [ ] Xóa system status: KHÔNG (should fail)

#### 8.2 Admin Rights
1. Login với System Administrator
2. Kiểm tra quyền:
   - [ ] Toàn quyền trên tất cả models

## 🐛 Các Lỗi Thường Gặp

### Lỗi 1: Module không xuất hiện
**Nguyên nhân:** Chưa update apps list  
**Giải pháp:** Apps > Update Apps List

### Lỗi 2: "xlrd not installed"
**Nguyên nhân:** Thiếu dependencies  
**Giải pháp:** `pip install xlrd xlsxwriter`

### Lỗi 3: Import file lỗi encoding
**Nguyên nhân:** File Excel không đúng format  
**Giải pháp:** Dùng file mẫu từ module

### Lỗi 4: Computed fields không update
**Nguyên nhân:** Thiếu depends hoặc store=True  
**Giải pháp:** Đã fix trong code

## ✅ Checklist Hoàn chỉnh

- [ ] Tất cả menu hoạt động
- [ ] CRUD nhân viên OK
- [ ] CRUD cuộc gọi OK
- [ ] CRUD system status OK
- [ ] Import Excel OK
- [ ] Tải file mẫu OK
- [ ] Validation OK
- [ ] Computed fields OK
- [ ] Related fields OK
- [ ] Filters & Search OK
- [ ] Pivot & Graph views OK
- [ ] Button actions OK
- [ ] Notifications OK
- [ ] Security OK
- [ ] Performance OK
- [ ] Không có lỗi Python
- [ ] Không có lỗi XML

## 📊 Kết quả Mong đợi

✅ **100% test cases pass**  
✅ **Không có lỗi trong log**  
✅ **UI/UX mượt mà**  
✅ **Performance tốt**  

---
**Happy Testing! 🎉**

