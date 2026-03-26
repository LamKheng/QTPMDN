# -*- coding: utf-8 -*-
{
    'name': "Quản lý công việc",
    'summary': "Module quản lý công việc",
    'description': """
        Quản lý thông internally công việc, liên kết với dự án và nhân sự.
    """,
    'author': "My Company",
    'category': 'Uncategorized',
    'version': '0.1',
    'depends': ['base', 'nhan_su', 'qldu'],
    'data': [
        'security/ir.model.access.csv',
        'views/cong_viec_views.xml',
        'views/du_an_inherit_views.xml',
    ],
    'demo': [],
    'installable': True,
    'application': True,
}
