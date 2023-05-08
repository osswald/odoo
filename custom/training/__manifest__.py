# -*- coding: utf-8 -*-


{
    'name': 'Training',
    'depends': [
        'base',
    ],
    'installable': True,
    'application': False,
    'license': "LGPL-3",
    'data': [
        'security/ir.model.access.csv',
        'views/training_views.xml',
        'views/training_module_views.xml',
        'views/training_date_views.xml',
        'views/training_participants_views.xml',
        'views/training_qualification_views.xml',
        'views/training_qualification_type_views.xml',
        'views/training_qualification_category_views.xml',
        'views/training_medical_fitness_level_views.xml',
        'views/training_menu_views.xml',
        'views/res_partner_views.xml',
    ],
}
