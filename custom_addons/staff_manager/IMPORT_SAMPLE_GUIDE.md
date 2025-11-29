# 📥 Hướng dẫn Sử dụng File Excel Mẫu

## 📋 File Mẫu Đã Tạo

Module đã bao gồm 2 file Excel mẫu trong thư mục module:

### 1. ✅ Staff_Import_Sample.xlsx
**File mẫu với dữ liệu ĐÚNG** - Dùng để import thành công

**Vị trí:** `/opt/odoo18/custom_addons/staff_manager/Staff_Import_Sample.xlsx`

**Nội dung:**
- 10 nhân viên mẫu với đầy đủ thông tin
- Tất cả dữ liệu đều hợp lệ
- Format đúng chuẩn

**Dữ liệu mẫu:**
| Mã NV | Họ tên | SĐT | Phòng ban | Khu vực |
|-------|--------|-----|-----------|---------|
| NV001 | Nguyễn Văn An | 0901234567 | Kinh doanh | Hà Nội |
| NV002 | Trần Thị Bình | 0912345678 | Kỹ thuật | TP.HCM |
| NV003 | Lê Văn Cường | 0923456789 | Marketing | Đà Nẵng |
| ... | ... | ... | ... | ... |
| NV010 | Đinh Thị Kim | 0990123456 | Kỹ thuật | Đà Nẵng |

### 2. ⚠️ Staff_Import_Sample_With_Errors.xlsx
**File mẫu với dữ liệu LỖI** - Dùng để test validation

**Vị trí:** `/opt/odoo18/custom_addons/staff_manager/Staff_Import_Sample_With_Errors.xlsx`

**Nội dung:**
- 8 bản ghi với các loại lỗi thường gặp
- Có ghi chú chi tiết từng lỗi
- Giúp test hệ thống validation

**Các lỗi mẫu:**
- ✗ SĐT sai format
- ✗ Thiếu thông tin bắt buộc
- ✗ Trùng mã nhân viên
- ✗ Thiếu mã nhân viên

## 🚀 Cách Sử dụng

### Cách 1: Tải từ Odoo (Khuyến nghị)

1. **Truy cập Odoo**
   ```
   http://localhost:8069
   ```

2. **Vào Import Wizard**
   - Menu: `Staff Manager > Cấu hình > Import nhân viên`

3. **Tải file mẫu**
   - Nhấn nút **"Tải file mẫu"**
   - File `Staff_Import_Template.xlsx` sẽ được download
   - File này có 3 dòng dữ liệu mẫu

4. **Chỉnh sửa và Import**
   - Mở file vừa download
   - Thêm/sửa nhân viên
   - Lưu file
   - Upload lại vào Odoo
   - Nhấn **"Import"**

### Cách 2: Copy từ Server

1. **Copy file từ server**
   ```bash
   # Copy file mẫu thành công
   cp /opt/odoo18/custom_addons/staff_manager/Staff_Import_Sample.xlsx ~/Downloads/
   
   # Hoặc copy file có lỗi để test
   cp /opt/odoo18/custom_addons/staff_manager/Staff_Import_Sample_With_Errors.xlsx ~/Downloads/
   ```

2. **Sử dụng file**
   - File sẽ có ở thư mục Downloads
   - Mở bằng Excel hoặc LibreOffice
   - Chỉnh sửa nếu cần
   - Upload vào Odoo

3. **Import vào Odoo**
   - Vào `Staff Manager > Cấu hình > Import nhân viên`
   - Upload file
   - Nhấn **"Import"**

## 📊 Cấu trúc File Excel

### Format chuẩn

| Cột | Tên cột | Bắt buộc | Định dạng | Ví dụ |
|-----|---------|----------|-----------|-------|
| A | Mã nhân viên | ✅ YES | Text | NV001 |
| B | Họ tên đầy đủ | ✅ YES | Text | Nguyễn Văn An |
| C | Số điện thoại | ❌ NO | 0xxxxxxxxx | 0901234567 |
| D | Phòng ban | ✅ YES | Text | Kinh doanh |
| E | Khu vực | ✅ YES | Text | Hà Nội |

### Quy tắc Validation

#### ✅ Mã nhân viên
- **Bắt buộc**: Không được để trống
- **Unique**: Không được trùng với mã đã có
- **Ví dụ đúng**: NV001, NV002, EMP001
- **Ví dụ sai**: (để trống), (trùng mã)

#### ✅ Họ tên đầy đủ
- **Bắt buộc**: Không được để trống
- **Ví dụ đúng**: Nguyễn Văn An, Trần Thị Bình
- **Ví dụ sai**: (để trống)

#### 📱 Số điện thoại
- **Không bắt buộc**: Có thể để trống
- **Format**: `0xxxxxxxxx` (10-11 số, bắt đầu bằng 0)
- **Ví dụ đúng**: 0901234567, 09123456789
- **Ví dụ sai**: 123, 901234567, abc123
- **Lưu ý**: Nếu bật "Bỏ qua validate số điện thoại", sẽ chấp nhận mọi format

#### ✅ Phòng ban
- **Bắt buộc**: Không được để trống
- **Ví dụ đúng**: Kinh doanh, Kỹ thuật, Marketing
- **Ví dụ sai**: (để trống)

#### ✅ Khu vực
- **Bắt buộc**: Không được để trống
- **Ví dụ đúng**: Hà Nội, TP.HCM, Đà Nẵng
- **Ví dụ sai**: (để trống)

## 🧪 Test Validation

### Test với file có lỗi

1. **Upload file:** `Staff_Import_Sample_With_Errors.xlsx`

2. **Kết quả mong đợi:**
   ```
   ✓ Tạo mới: 2 bản ghi (NV001, NV006)
   ✗ Lỗi: 6 bản ghi
   
   Chi tiết lỗi:
   - Dòng 3: Số điện thoại không đúng định dạng: 123
   - Dòng 4: Thiếu thông tin bắt buộc (Họ tên)
   - Dòng 5: Thiếu thông tin bắt buộc (Phòng ban)
   - Dòng 6: Thiếu thông tin bắt buộc (Khu vực)
   - Dòng 7: Mã nhân viên đã tồn tại: NV001
   - Dòng 9: Thiếu thông tin bắt buộc (Mã nhân viên)
   ```

3. **Kiểm tra:**
   - Chỉ 2 nhân viên hợp lệ được import
   - Log hiển thị chi tiết các lỗi
   - Các bản ghi lỗi không bị import

### Test với file đúng

1. **Upload file:** `Staff_Import_Sample.xlsx`

2. **Kết quả mong đợi:**
   ```
   ✓ Tạo mới: 10 bản ghi
   ✓ Cập nhật: 0 bản ghi
   ✗ Lỗi: 0 bản ghi
   ```

3. **Kiểm tra:**
   - Tất cả 10 nhân viên được import thành công
   - Kiểm tra menu: `Staff Manager > Nhân viên`
   - Xem danh sách nhân viên đã import

## 💡 Tips & Tricks

### 1. Tạo file Excel từ Template

**Từ Odoo:**
- Download template từ Import Wizard
- Chỉnh sửa và import

**Từ Server:**
```bash
# Copy file mẫu
cp Staff_Import_Sample.xlsx My_Staff_Import.xlsx

# Chỉnh sửa với LibreOffice hoặc Excel
libreoffice My_Staff_Import.xlsx
```

### 2. Import hàng loạt

- Chuẩn bị file với 100-1000 nhân viên
- Đảm bảo format đúng
- Import một lần, hệ thống sẽ xử lý tự động
- Xem log để biết kết quả

### 3. Cập nhật nhân viên có sẵn

- Bật tùy chọn: **"Cập nhật bản ghi có sẵn"**
- Import file với mã nhân viên đã tồn tại
- Hệ thống sẽ cập nhật thông tin mới

### 4. Bỏ qua validate SĐT

- Bật tùy chọn: **"Bỏ qua validate số điện thoại"**
- Import được các SĐT không đúng format VN
- Hữu ích khi có SĐT quốc tế

## 📝 Ví dụ Thực tế

### Scenario 1: Import 50 nhân viên mới

```bash
# 1. Chuẩn bị file Excel với 50 nhân viên
# 2. Kiểm tra format:
#    - Mã NV: NV001 đến NV050
#    - Tất cả đầy đủ thông tin
#    - SĐT đúng format
# 3. Upload vào Odoo
# 4. Import
# 5. Kết quả: 50 nhân viên mới
```

### Scenario 2: Cập nhật thông tin nhân viên

```bash
# 1. Export danh sách nhân viên hiện tại (từ Odoo)
# 2. Sửa thông tin trong Excel (VD: thay đổi phòng ban)
# 3. Bật "Cập nhật bản ghi có sẵn"
# 4. Import lại
# 5. Kết quả: Thông tin được cập nhật
```

## 🆘 Troubleshooting

### Lỗi: "File không đúng format"
- **Nguyên nhân**: File không phải Excel (.xls, .xlsx)
- **Giải pháp**: Lưu lại file dưới định dạng Excel

### Lỗi: "Cột bị thiếu"
- **Nguyên nhân**: Thiếu cột trong header
- **Giải pháp**: Đảm bảo có đầy đủ 5 cột (A-E)

### Lỗi: "Không đọc được file"
- **Nguyên nhân**: File bị lỗi hoặc định dạng không đúng
- **Giải pháp**: 
  1. Mở lại file bằng Excel
  2. Lưu lại dưới định dạng .xlsx
  3. Thử import lại

### Import chậm
- **Nguyên nhân**: File quá lớn (>1000 dòng)
- **Giải pháp**: 
  - Chia nhỏ file
  - Import từng batch
  - Kiên nhẫn đợi (hệ thống xử lý từng dòng)

## 📚 Tham khảo

- **QUICKSTART.md** - Hướng dẫn nhanh 5 phút
- **README.md** - Tài liệu đầy đủ
- **TESTING.md** - Checklist kiểm tra

---

**Staff Manager v18.0.1.1.0**  
*Import Sample Files Guide*

