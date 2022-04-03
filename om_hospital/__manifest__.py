# -*- coding: utf-8 -*-
# Part of Odoo. See LICENSE file for full copyright and licensing details.
# python files will be imported in init file, but all xml files will be imported DATA array in manifest file

{
    'name': 'Hospital Management',
    'description': """
Description
===============================================
    """,
    'version': '1.0.0',
    'category': 'Hospital',
    'author': 'Huseyin OZDOGAN',
    'summary': 'Hospital Management System',
    'auto_install': False,
    'sequence': -100,
    'depends': [
    ],
    'data': [
        'security/ir.model.access.csv',
        'views/menu.xml',
        'views/patient_view.xml',
        'views/female_patient_view.xml',
    ],
    'bootstrap': False,
    'assets': {
    },
    'demo': [
    ],
    'installable': True, # True olmayinca model wont be created
    'license': 'LGPL-3',
}
