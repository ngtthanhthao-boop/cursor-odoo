# Hướng dẫn Cài đặt Staff Manager Module

## Bước 1: Cài đặt Dependencies

### Sử dụng pip
```bash
pip install xlrd xlsxwriter
```

### Hoặc sử dụng requirements.txt
```bash
pip install -r requirements.txt
```

### Nếu dự án sử dụng virtual environment (.venv)
```bash
source .venv/bin/activate  # Linux/Mac
# hoặc
.venv\Scripts\activate  # Windows

pip install -r requirements.txt
```

## Bước 2: Copy Module vào Odoo

1. Copy thư mục `staff_manager` vào thư mục `custom_addons` của Odoo
```bash
cp -r staff_manager /opt/odoo18/custom_addons/
```

2. Đảm bảo quyền truy cập đúng
```bash
sudo chown -R odoo:odoo /opt/odoo18/custom_addons/staff_manager
sudo chmod -R 755 /opt/odoo18/custom_addons/staff_manager
```

## Bước 3: Cập nhật Odoo Config

Thêm đường dẫn `custom_addons` vào file config của Odoo (nếu chưa có):

```ini
[options]
addons_path = /opt/odoo18/odoo/addons,/opt/odoo18/custom_addons
```

## Bước 4: Cập nhật Danh sách Apps

1. Khởi động lại Odoo server
```bash
sudo systemctl restart odoo
# hoặc nếu chạy trực tiếp
./odoo-bin -c odoo.conf
```

2. Đăng nhập vào Odoo với quyền Administrator

3. Vào menu **Apps** (Ứng dụng)

4. Nhấn nút **Update Apps List** (Cập nhật danh sách ứng dụng)

5. Xác nhận cập nhật

## Bước 5: Cài đặt Module

1. Tìm kiếm "Staff Manager" trong danh sách Apps

2. Nhấn nút **Install** (Cài đặt)

3. Đợi quá trình cài đặt hoàn tất

## Bước 6: Kiểm tra

1. Sau khi cài đặt, menu **Staff Manager** sẽ xuất hiện trên thanh menu chính

2. Kiểm tra các submenu:
   - Nhân viên
   - Lịch sử cuộc gọi
   - Trạng thái hệ thống
   - Cấu hình > Import nhân viên

## Xử lý lỗi thường gặp

### Lỗi: "Module not found"
- Kiểm tra đường dẫn addons_path trong config
- Đảm bảo thư mục staff_manager tồn tại trong custom_addons
- Khởi động lại Odoo server

### Lỗi: "xlrd not installed"
- Cài đặt lại dependencies: `pip install xlrd xlsxwriter`
- Kiểm tra đúng virtual environment nếu có

### Lỗi: Permission denied
- Cấp quyền cho thư mục: `sudo chown -R odoo:odoo /path/to/staff_manager`
- Đảm bảo user odoo có quyền đọc/ghi

## Gỡ cài đặt

1. Vào menu **Apps**
2. Tìm "Staff Manager"
3. Nhấn **Uninstall**
4. Xác nhận gỡ cài đặt

**Lưu ý:** Dữ liệu sẽ bị xóa khi gỡ cài đặt module. Hãy backup trước khi gỡ.

## Nâng cấp

Để nâng cấp module lên phiên bản mới:

1. Backup dữ liệu
2. Copy phiên bản mới vào thư mục
3. Khởi động lại Odoo
4. Vào menu **Apps**
5. Tìm module và nhấn **Upgrade**

## Liên hệ hỗ trợ

Email: support@yourcompany.com
Website: https://www.yourcompany.com

