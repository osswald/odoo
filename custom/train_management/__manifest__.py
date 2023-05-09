# -*- coding: utf-8 -*-


{
    'name': 'Train Management',
    'depends': [
        'base',
    ],
    'author': 'Christoph Osswald',
    'installable': True,
    'application': False,
    'license': "LGPL-3",
    'data': [
        'security/ir.model.access.csv',
        'views/circuit_views.xml',
        'views/day_planning_views.xml',
        'views/day_planning_text_views.xml',
        'views/railway_company_views.xml',
        'views/station_views.xml',
        'views/vehicle_views.xml',
        'views/train_views.xml',
        'views/train_management_menu_views.xml',
    ],
}
