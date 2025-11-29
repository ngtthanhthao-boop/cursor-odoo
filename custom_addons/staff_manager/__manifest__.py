# -*- coding: utf-8 -*-
{
    'name': 'Staff Manager',
    'version': '18.0.1.1.0',
    'category': 'Human Resources',
    'summary': 'Quản lý nhân viên và cuộc gọi',
    'description': """
        Staff Manager Module
        ====================
        Module quản lý nhân viên và lịch sử cuộc gọi
        
        Tính năng chính:
        - Quản lý thông tin nhân viên
        - Theo dõi lịch sử cuộc gọi
        - Thống kê cuộc gọi theo nhân viên
        - Import dữ liệu từ Excel
        - Quản lý trạng thái hệ thống
    """,
    'author': 'Your Company',
    'website': 'https://www.yourcompany.com',
    'depends': ['base', 'web'],
    'external_dependencies': {
        'python': ['xlrd', 'xlsxwriter'],
    },
    'data': [
        'security/ir.model.access.csv',
        'views/staff_views.xml',
        'views/call_log_views.xml',
        'views/system_status_views.xml',
        'views/import_wizard_views.xml',
        'views/menu_views.xml',
    ],
    'installable': True,
    'application': True,
    'auto_install': False,
    'license': 'LGPL-3',
}

