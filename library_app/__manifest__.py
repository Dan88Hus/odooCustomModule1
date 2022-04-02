{
    'name': "Library Management",

    'summary': """Manage Library catalogue and book lending.""",

    'description': """
        Long description of module's purpose
    """,

    'author': "Huseyin Ozdogan",
    'website': "http://www.yourcompany.com",

    # Categories can be used to filter modules in modules listing
    # Check https://github.com/odoo/odoo/blob/15.0/odoo/addons/base/data/ir_module_category_data.xml
    # for the full list
    'category': 'Services/Library',
    "licence": "AGPL-3",
    'version': '0.1',

    # any module necessary for this one to work correctly
    'depends': ['base'],

    # always loaded
    'data': [
        'security/library_security.xml',
        'views/library_menu.xml',
    ],
    # only loaded in demonstration mode
    # 'demo': [
    #     'demo/demo.xml',
    # ],
    "application": True
}
# -*- coding: utf-8 -*-
