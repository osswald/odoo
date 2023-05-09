# -*- coding: utf-8 -*-


{
    'name': 'Shift',
    'author': 'Christoph Osswald',
    'depends': [
        'base',
        'training',
        'train_management',
    ],
    'data': [
        'security/ir.model.access.csv',
        'views/shift_position_views.xml',
        'views/shift_position_type_views.xml',
        'views/shift_template_views.xml',
        'views/shift_menu_views.xml',
    ],
    'installable': True,
    'application': False,
    'license': "LGPL-3"
}
