# -*- coding: utf-8 -*-
from odoo import models, fields, api
from odoo.exceptions import ValidationError
import logging

_logger = logging.getLogger(__name__)


class CallLog(models.Model):
    _name = 'staff.manager.call.log'
    _description = 'Lịch Sử Cuộc Gọi'
    _rec_name = 'call_time'
    _order = 'call_time desc'

    call_time = fields.Datetime(
        string='Thời gian gọi',
        required=True,
        index=True,
        default=fields.Datetime.now,
        help='Thời điểm thực hiện cuộc gọi'
    )
    staff_id = fields.Many2one(
        'staff.manager.staff',
        string='Nhân viên',
        ondelete='cascade',
        index=True,
        help='Nhân viên được gọi'
    )
    employee_code = fields.Char(
        string='Mã nhân viên',
        related='staff_id.employee_code',
        store=True,
        readonly=True,
        help='Mã nhân viên (tự động lấy từ nhân viên)'
    )
    phone = fields.Char(
        string='Số điện thoại',
        related='staff_id.phone',
        store=True,
        readonly=True,
        help='Số điện thoại (tự động lấy từ nhân viên)'
    )
    department = fields.Char(
        string='Phòng ban',
        related='staff_id.department',
        store=True,
        readonly=True,
        help='Phòng ban (tự động lấy từ nhân viên)'
    )
    area = fields.Char(
        string='Khu vực',
        related='staff_id.area',
        store=True,
        readonly=True,
        help='Khu vực (tự động lấy từ nhân viên)'
    )
    status = fields.Selection(
        [
            ('answered', 'Đã trả lời'),
            ('unanswered', 'Chưa trả lời'),
        ],
        string='Trạng thái',
        required=True,
        default='unanswered',
        index=True,
        help='Trạng thái cuộc gọi'
    )
    duration = fields.Float(
        string='Thời lượng (phút)',
        digits=(10, 2),
        help='Thời lượng cuộc gọi tính bằng phút'
    )
    response_key = fields.Char(
        string='Phím phản hồi',
        help='Phím được nhấn trong quá trình cuộc gọi'
    )
    record_url = fields.Char(
        string='URL ghi âm',
        help='Đường dẫn tới file ghi âm WAV'
    )
    notes = fields.Text(
        string='Ghi chú',
        help='Ghi chú bổ sung về cuộc gọi'
    )

    @api.constrains('duration')
    def _check_duration(self):
        """Kiểm tra thời lượng cuộc gọi"""
        for record in self:
            if record.duration and record.duration < 0:
                raise ValidationError('Thời lượng cuộc gọi không thể âm!')

    @api.onchange('status')
    def _onchange_status(self):
        """Tự động set duration = 0 nếu chưa trả lời"""
        if self.status == 'unanswered':
            self.duration = 0.0

    @api.model
    def create(self, vals):
        """Override create để log thông tin"""
        _logger.info(f"Tạo call log mới: {vals.get('call_time')} - Trạng thái: {vals.get('status')}")
        return super(CallLog, self).create(vals)

    def name_get(self):
        """Hiển thị thông tin cuộc gọi"""
        result = []
        for record in self:
            staff_name = record.staff_id.name if record.staff_id else 'N/A'
            name = f"{record.call_time} - {staff_name} ({record.status})"
            result.append((record.id, name))
        return result

