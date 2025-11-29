# -*- coding: utf-8 -*-
import re
from odoo import models, fields, api
from odoo.exceptions import ValidationError
import logging

_logger = logging.getLogger(__name__)


class Staff(models.Model):
    _name = 'staff.manager.staff'
    _description = 'Nhân Viên'
    _rec_name = 'name'
    _order = 'employee_code'

    employee_code = fields.Char(
        string='Mã nhân viên',
        required=True,
        index=True,
        copy=False,
        help='Mã nhân viên duy nhất'
    )
    name = fields.Char(
        string='Họ tên đầy đủ',
        required=True,
        index=True,
        help='Họ và tên đầy đủ của nhân viên'
    )
    phone = fields.Char(
        string='Số điện thoại',
        help='Số điện thoại định dạng Việt Nam (0xxxxxxxxx)'
    )
    department = fields.Char(
        string='Phòng ban',
        required=True,
        index=True,
        help='Phòng ban làm việc'
    )
    area = fields.Char(
        string='Khu vực',
        required=True,
        index=True,
        help='Khu vực làm việc'
    )
    total_calls = fields.Integer(
        string='Tổng số cuộc gọi',
        compute='_compute_call_statistics',
        store=True,
        help='Tổng số cuộc gọi của nhân viên'
    )
    answered_calls = fields.Integer(
        string='Cuộc gọi đã trả lời',
        compute='_compute_call_statistics',
        store=True,
        help='Số cuộc gọi đã được trả lời'
    )
    unanswered_calls = fields.Integer(
        string='Cuộc gọi chưa trả lời',
        compute='_compute_call_statistics',
        store=True,
        help='Số cuộc gọi chưa được trả lời'
    )
    call_log_ids = fields.One2many(
        'staff.manager.call.log',
        'staff_id',
        string='Lịch sử cuộc gọi'
    )
    active = fields.Boolean(
        string='Hoạt động',
        default=True,
        help='Bỏ chọn để ẩn nhân viên mà không xóa'
    )

    _sql_constraints = [
        ('employee_code_unique', 'UNIQUE(employee_code)', 'Mã nhân viên phải là duy nhất!')
    ]

    @api.constrains('phone')
    def _check_phone_format(self):
        """Kiểm tra định dạng số điện thoại Việt Nam"""
        for record in self:
            if record.phone:
                # Định dạng số điện thoại Việt Nam: 0xxxxxxxxx (10 hoặc 11 số)
                phone_pattern = r'^0\d{9,10}$'
                if not re.match(phone_pattern, record.phone):
                    raise ValidationError(
                        'Số điện thoại không đúng định dạng Việt Nam!\n'
                        'Định dạng yêu cầu: 0xxxxxxxxx (10-11 số, bắt đầu bằng 0)'
                    )

    @api.depends('call_log_ids', 'call_log_ids.status')
    def _compute_call_statistics(self):
        """Tính toán thống kê cuộc gọi"""
        for record in self:
            call_logs = record.call_log_ids
            record.total_calls = len(call_logs)
            record.answered_calls = len(call_logs.filtered(lambda c: c.status == 'answered'))
            record.unanswered_calls = len(call_logs.filtered(lambda c: c.status == 'unanswered'))

    @api.model
    def create(self, vals):
        """Override create để log thông tin"""
        _logger.info(f"Tạo nhân viên mới: {vals.get('name')} - Mã: {vals.get('employee_code')}")
        return super(Staff, self).create(vals)

    def write(self, vals):
        """Override write để log thông tin"""
        for record in self:
            _logger.info(f"Cập nhật nhân viên: {record.name} (ID: {record.id})")
        return super(Staff, self).write(vals)

    def name_get(self):
        """Hiển thị tên nhân viên kèm mã"""
        result = []
        for record in self:
            name = f"[{record.employee_code}] {record.name}"
            result.append((record.id, name))
        return result

