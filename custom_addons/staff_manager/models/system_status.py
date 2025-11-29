# -*- coding: utf-8 -*-
from odoo import models, fields, api
from odoo.exceptions import ValidationError
import logging

_logger = logging.getLogger(__name__)


class SystemStatus(models.Model):
    _name = 'staff.manager.system.status'
    _description = 'Trạng Thái Hệ Thống'
    _rec_name = 'name'

    name = fields.Char(
        string='Tên cấu hình',
        required=True,
        help='Tên của cấu hình hệ thống'
    )
    status = fields.Selection(
        [
            ('on', 'Bật'),
            ('off', 'Tắt'),
        ],
        string='Trạng thái',
        required=True,
        default='off',
        help='Trạng thái hoạt động của hệ thống'
    )
    max_calls = fields.Integer(
        string='Số cuộc gọi tối đa',
        default=100,
        help='Số lượng cuộc gọi tối đa cho phép trong một chu kỳ'
    )
    content_file = fields.Text(
        string='File nội dung',
        help='Nội dung file text cho hệ thống'
    )
    active = fields.Boolean(
        string='Hoạt động',
        default=True,
        help='Bỏ chọn để ẩn cấu hình mà không xóa'
    )
    last_update = fields.Datetime(
        string='Cập nhật lần cuối',
        readonly=True,
        help='Thời điểm cập nhật cấu hình lần cuối'
    )
    updated_by = fields.Many2one(
        'res.users',
        string='Người cập nhật',
        readonly=True,
        help='Người dùng cập nhật cấu hình lần cuối'
    )

    @api.constrains('max_calls')
    def _check_max_calls(self):
        """Kiểm tra số cuộc gọi tối đa"""
        for record in self:
            if record.max_calls < 0:
                raise ValidationError('Số cuộc gọi tối đa không thể âm!')
            if record.max_calls > 10000:
                raise ValidationError('Số cuộc gọi tối đa không thể vượt quá 10,000!')

    def write(self, vals):
        """Override write để cập nhật thông tin người sửa"""
        vals['last_update'] = fields.Datetime.now()
        vals['updated_by'] = self.env.user.id
        _logger.info(f"Cập nhật cấu hình hệ thống: {self.name}")
        return super(SystemStatus, self).write(vals)

    def action_turn_on(self):
        """Action button để bật hệ thống"""
        self.write({'status': 'on'})
        _logger.info(f"Đã bật hệ thống: {self.name}")
        return {
            'type': 'ir.actions.client',
            'tag': 'display_notification',
            'params': {
                'title': 'Thành công',
                'message': f'Đã bật hệ thống: {self.name}',
                'type': 'success',
                'sticky': False,
            }
        }

    def action_turn_off(self):
        """Action button để tắt hệ thống"""
        self.write({'status': 'off'})
        _logger.info(f"Đã tắt hệ thống: {self.name}")
        return {
            'type': 'ir.actions.client',
            'tag': 'display_notification',
            'params': {
                'title': 'Thành công',
                'message': f'Đã tắt hệ thống: {self.name}',
                'type': 'warning',
                'sticky': False,
            }
        }

