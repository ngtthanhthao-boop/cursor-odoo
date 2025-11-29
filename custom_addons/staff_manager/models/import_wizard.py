# -*- coding: utf-8 -*-
import base64
import io
import re
from odoo import models, fields, api
from odoo.exceptions import UserError, ValidationError
import logging

try:
    import xlrd
except ImportError:
    xlrd = None

_logger = logging.getLogger(__name__)


class ImportWizard(models.TransientModel):
    _name = 'staff.manager.import.wizard'
    _description = 'Import Wizard cho Nhân Viên'

    file_data = fields.Binary(
        string='File Excel',
        required=True,
        help='Chọn file Excel để import dữ liệu nhân viên'
    )
    filename = fields.Char(
        string='Tên file',
        help='Tên file Excel'
    )
    update_existing = fields.Boolean(
        string='Cập nhật bản ghi có sẵn',
        default=False,
        help='Nếu chọn, sẽ cập nhật nhân viên có sẵn dựa trên mã nhân viên'
    )
    skip_validation = fields.Boolean(
        string='Bỏ qua validate số điện thoại',
        default=False,
        help='Nếu chọn, sẽ không kiểm tra định dạng số điện thoại'
    )
    import_log = fields.Text(
        string='Kết quả import',
        readonly=True,
        help='Log kết quả quá trình import'
    )

    def _validate_phone_number(self, phone):
        """Validate định dạng số điện thoại Việt Nam"""
        if not phone:
            return True
        phone_pattern = r'^0\d{9,10}$'
        return bool(re.match(phone_pattern, str(phone).strip()))

    def action_import_excel(self):
        """Import dữ liệu từ file Excel"""
        self.ensure_one()
        
        if not xlrd:
            raise UserError('Thư viện xlrd chưa được cài đặt!\nVui lòng cài đặt: pip install xlrd')

        if not self.file_data:
            raise UserError('Vui lòng chọn file Excel để import!')

        try:
            # Đọc file Excel
            file_content = base64.b64decode(self.file_data)
            workbook = xlrd.open_workbook(file_contents=file_content)
            sheet = workbook.sheet_by_index(0)

            # Khởi tạo counters
            created_count = 0
            updated_count = 0
            error_count = 0
            error_messages = []

            _logger.info(f"Bắt đầu import từ file: {self.filename}")
            _logger.info(f"Tổng số dòng: {sheet.nrows}")

            # Đọc từ dòng 2 (bỏ qua header)
            for row_idx in range(1, sheet.nrows):
                try:
                    # Đọc dữ liệu từng dòng
                    employee_code = str(sheet.cell_value(row_idx, 0)).strip()
                    name = str(sheet.cell_value(row_idx, 1)).strip()
                    phone = str(sheet.cell_value(row_idx, 2)).strip() if sheet.ncols > 2 else ''
                    department = str(sheet.cell_value(row_idx, 3)).strip() if sheet.ncols > 3 else ''
                    area = str(sheet.cell_value(row_idx, 4)).strip() if sheet.ncols > 4 else ''

                    # Validate dữ liệu bắt buộc
                    if not employee_code or not name or not department or not area:
                        error_messages.append(f"Dòng {row_idx + 1}: Thiếu thông tin bắt buộc")
                        error_count += 1
                        continue

                    # Validate số điện thoại
                    if phone and not self.skip_validation:
                        if not self._validate_phone_number(phone):
                            error_messages.append(
                                f"Dòng {row_idx + 1}: Số điện thoại không đúng định dạng: {phone}"
                            )
                            error_count += 1
                            continue

                    # Chuẩn bị dữ liệu
                    vals = {
                        'employee_code': employee_code,
                        'name': name,
                        'phone': phone,
                        'department': department,
                        'area': area,
                    }

                    # Kiểm tra nhân viên đã tồn tại chưa
                    existing_staff = self.env['staff.manager.staff'].search([
                        ('employee_code', '=', employee_code)
                    ], limit=1)

                    if existing_staff:
                        if self.update_existing:
                            existing_staff.write(vals)
                            updated_count += 1
                            _logger.info(f"Cập nhật nhân viên: {employee_code} - {name}")
                        else:
                            error_messages.append(
                                f"Dòng {row_idx + 1}: Mã nhân viên đã tồn tại: {employee_code}"
                            )
                            error_count += 1
                    else:
                        self.env['staff.manager.staff'].create(vals)
                        created_count += 1
                        _logger.info(f"Tạo mới nhân viên: {employee_code} - {name}")

                except Exception as e:
                    error_messages.append(f"Dòng {row_idx + 1}: Lỗi - {str(e)}")
                    error_count += 1
                    _logger.error(f"Lỗi khi import dòng {row_idx + 1}: {str(e)}")

            # Tạo log kết quả
            log_message = f"""
=== KẾT QUẢ IMPORT ===
File: {self.filename}
Tổng số dòng xử lý: {sheet.nrows - 1}

✓ Tạo mới: {created_count} bản ghi
✓ Cập nhật: {updated_count} bản ghi
✗ Lỗi: {error_count} bản ghi

"""
            if error_messages:
                log_message += "\n=== CHI TIẾT LỖI ===\n"
                log_message += "\n".join(error_messages[:50])  # Giới hạn 50 lỗi đầu tiên
                if len(error_messages) > 50:
                    log_message += f"\n... và {len(error_messages) - 50} lỗi khác"

            self.import_log = log_message
            _logger.info(f"Hoàn thành import: {created_count} tạo mới, {updated_count} cập nhật, {error_count} lỗi")

            # Hiển thị notification
            return {
                'type': 'ir.actions.client',
                'tag': 'display_notification',
                'params': {
                    'title': 'Import hoàn tất',
                    'message': f'Tạo mới: {created_count} | Cập nhật: {updated_count} | Lỗi: {error_count}',
                    'type': 'success' if error_count == 0 else 'warning',
                    'sticky': True,
                },
                'context': self.env.context,
            }

        except Exception as e:
            error_msg = f'Lỗi khi đọc file Excel: {str(e)}'
            _logger.error(error_msg)
            raise UserError(error_msg)

    def action_download_template(self):
        """Download file Excel mẫu"""
        try:
            import xlsxwriter
        except ImportError:
            raise UserError('Thư viện xlsxwriter chưa được cài đặt!\nVui lòng cài đặt: pip install xlsxwriter')

        # Tạo file Excel mẫu
        output = io.BytesIO()
        workbook = xlsxwriter.Workbook(output, {'in_memory': True})
        worksheet = workbook.add_worksheet('Staff Template')

        # Format cho header
        header_format = workbook.add_format({
            'bold': True,
            'bg_color': '#4472C4',
            'font_color': 'white',
            'border': 1,
            'align': 'center',
            'valign': 'vcenter'
        })

        # Header columns
        headers = ['Mã nhân viên', 'Họ tên đầy đủ', 'Số điện thoại', 'Phòng ban', 'Khu vực']
        for col, header in enumerate(headers):
            worksheet.write(0, col, header, header_format)

        # Dữ liệu mẫu
        sample_data = [
            ['NV001', 'Nguyễn Văn A', '0901234567', 'Kinh doanh', 'Hà Nội'],
            ['NV002', 'Trần Thị B', '0912345678', 'Kỹ thuật', 'TP.HCM'],
            ['NV003', 'Lê Văn C', '0923456789', 'Marketing', 'Đà Nẵng'],
        ]

        for row_idx, row_data in enumerate(sample_data, start=1):
            for col_idx, value in enumerate(row_data):
                worksheet.write(row_idx, col_idx, value)

        # Điều chỉnh độ rộng cột
        worksheet.set_column(0, 0, 15)  # Mã nhân viên
        worksheet.set_column(1, 1, 25)  # Họ tên
        worksheet.set_column(2, 2, 15)  # Số điện thoại
        worksheet.set_column(3, 3, 20)  # Phòng ban
        worksheet.set_column(4, 4, 15)  # Khu vực

        workbook.close()
        output.seek(0)

        # Tạo attachment và download
        attachment = self.env['ir.attachment'].create({
            'name': 'Staff_Import_Template.xlsx',
            'type': 'binary',
            'datas': base64.b64encode(output.read()),
            'mimetype': 'application/vnd.openxmlformats-officedocument.spreadsheetml.sheet'
        })

        return {
            'type': 'ir.actions.act_url',
            'url': f'/web/content/{attachment.id}?download=true',
            'target': 'new',
        }

