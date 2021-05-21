# -*- coding: utf-8 -*-
{
    'name': "hospital Management",

    'summary':'Hospital Management Module',

    'description':'Module for managing Hospital',

    'author': "Bajra",
    'website': "http://www.yourcompany.com",

    # Categories can be used to filter modules in modules listing
    # Check https://github.com/odoo/odoo/blob/13.0/odoo/addons/base/data/ir_module_category_data.xml
    # for the full list
    'category': 'Tools',
    'version': '0.1',

    # any module necessary for this one to work correctly
    'depends': ['base', 'mail','sale'],

    # always loaded
    'data': [
        'security/ir.model.access.csv',
        'data/sequence.xml',
        'views/views.xml',
        'views/medicine.xml',
        'views/doctors.xml',
        'views/pharmacy.xml',
        'views/templates.xml',
        'views/websit_form.xml',
        'views/appointment.xml',
        'report/report.xml',
        'report/pharmacy_bill.xml',


    ],
    # only loaded in demonstration mode
    'demo': [
        'demo/demo.xml',
    ],
    'installable': True,
    'application': True,
    'auto_install': False,

}
