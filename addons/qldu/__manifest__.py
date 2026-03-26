# -*- coding: utf-8 -*-
{
    'name': "Quản lý dự án",
    'summary': "Module quản lý dự án",
    'description': """
        Quản lý thông tin dự án và liên kết với nhân sự.
    """,
    'author': "My Company",
    'category': 'Uncategorized',
    'version': '0.1',
    'depends': ['base', 'nhan_su'],
    'data': [
        'security/ir.model.access.csv',
        'views/du_an_views.xml',
    ],
    'demo': [],
    'installable': True,
    'application': True,
}
