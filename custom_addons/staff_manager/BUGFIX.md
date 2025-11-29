# 🐛 Bug Fixes - Staff Manager Module

## Bug #1: Invalid view type 'tree' (FIXED) ✅

### 📋 Mô tả lỗi
```
odoo.tools.convert.ParseError: while parsing /opt/odoo18/custom_addons/staff_manager/views/staff_views.xml:4
Invalid view type: 'tree'.
You might have used an invalid starting tag in the architecture.
Allowed types are: list, form, graph, pivot, calendar, kanban, search, qweb, activity
```

### 🔍 Nguyên nhân
Trong **Odoo 18**, view type `tree` đã bị **deprecated** và thay thế bằng `list`.

### ✅ Cách sửa
Thay đổi tất cả các XML views:

**TRƯỚC (SAI):**
```xml
<tree string="Nhân Viên">
    <field name="employee_code"/>
    ...
</tree>
```

**SAU (ĐÚNG):**
```xml
<list string="Nhân Viên">
    <field name="employee_code"/>
    ...
</list>
```

### 📝 Các file đã sửa

1. **views/staff_views.xml**
   - Dòng 8: `<tree>` → `<list>`
   - Dòng 18: `</tree>` → `</list>`
   - Dòng 66: `<tree>` → `<list>` (trong One2many)
   - Dòng 72: `</tree>` → `</list>`
   - Dòng 98: `view_mode="tree,form"` → `view_mode="list,form"`

2. **views/call_log_views.xml**
   - Dòng 8: `<tree>` → `<list>`
   - Dòng 18: `</tree>` → `</list>`
   - Dòng 141: `view_mode="tree,form,pivot,graph"` → `view_mode="list,form,pivot,graph"`

3. **views/system_status_views.xml**
   - Dòng 8: `<tree>` → `<list>`
   - Dòng 15: `</tree>` → `</list>`
   - Dòng 84: `view_mode="tree,form"` → `view_mode="list,form"`

### 🔧 Thực hiện
```bash
# 1. Sửa các file XML (đã thực hiện)
# 2. Restart Odoo
sudo systemctl restart odoo18

# 3. Update Apps List trong Odoo UI
# 4. Install module "Staff Manager"
```

### ✅ Kết quả
- Module cài đặt thành công
- Tất cả views hoạt động bình thường
- Không còn lỗi ParseError

### 📚 Tham khảo
- [Odoo 18 Migration Guide](https://www.odoo.com/documentation/18.0/developer/howtos/upgrade_18.html)
- Odoo 18 đã thay đổi nhiều điểm so với các phiên bản trước:
  - `tree` → `list`
  - `attrs` → `invisible`, `readonly`, `required` (attributes)
  - Nhiều thay đổi khác về API

### 💡 Bài học
Khi develop module cho Odoo 18:
1. **LUÔN dùng `list` thay vì `tree`** cho list views
2. Kiểm tra tài liệu migration guide của Odoo 18
3. Test kỹ trước khi deploy
4. Đọc error logs kỹ càng

---

## Lịch sử Bug Fixes

| # | Ngày | Lỗi | Trạng thái |
|---|------|-----|------------|
| 1 | 2024-11-29 | Invalid view type 'tree' | ✅ FIXED |

---

**Staff Manager v18.0.1.1.0**  
*Last Updated: 2024-11-29 15:08*

