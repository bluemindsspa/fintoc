# -*- coding: utf-8 -*-
{
    'name': "Integracion con Fintoc",

    'summary': """
        Integración con Fintoc""",

    'description': """
        Conecta las cuentas bancarias para importar de manera automática los extractos bancarios y poder realizar la conciliación bancaria
    """,
    "images": ["static/description/Fintoc_portada.png","static/description/Fintoc1.png"],
    "license": "OPL-1",
    'author': "Blueminds",
    'website': "http://www.blueminds.cl",
    'contributors': ["Boris Silva <bsilva@blueminds.cl>","Verónica López <vlopez@blueminds.cl>"],

    'category': 'Account',
    'version': '1.1',

    # any module necessary for this one to work correctly
    'depends': ['base', 'account'],

    # always loaded
    'data': [
        'security/ir.model.access.csv',
        'views/res_company_view.xml',
        'views/account_view.xml',
        'wizard/bank_statement_view.xml',
        'data/cron.xml',
    ],
}
