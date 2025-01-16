# -*- coding: utf-8 -*-
{
    'name': "captacion",

    'summary': """
        Modulo de captación de participantes a diferentes
        proyectos y programas de entidades""",

    'description': """
        Modulo de captación de participantes a diferentes
        proyectos y programas de entidades
    """,

    'author': "tecnoformacion",
    'website': "https://www.yourcompany.com",

    # Categories can be used to filter modules in modules listing
    # Check https://github.com/odoo/odoo/blob/16.0/odoo/addons/base/data/ir_module_category_data.xml
    # for the full list
    'category': 'Uncategorized',
    'version': '0.1',

    # any module necessary for this one to work correctly
    'depends': ['base'],

    # always loaded
    'data': [
        'security/ir.model.access.csv',
        #'views/capta_experiencialaboral.xml',
        'views/captacion_experiencialaboral.xml',
        'views/captacion_interesesprofesionales.xml',
        'views/captacion_necesidadesformacionespecifica.xml',
        'views/captacion_objetivoprofesional.xml',
        'views/captacion_participantes.xml',
        'views/captacion_proyectos.xml',
        #'views/captacion_programas.xml',
        'views/captacion_menu.xml',
        
    ],
    # only loaded in demonstration mode
    'demo': [
        'demo/demo.xml',
    ],
}
