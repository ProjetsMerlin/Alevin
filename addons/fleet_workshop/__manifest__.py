{
    'name': 'Fleet Workshop',
    'version': '18.0.1.0.0',
    'category': 'Fleet',
    'summary': 'Vehicle and workshop management',
    'author': 'Odoo Learning',
    'license': 'LGPL-3',
    'depends': [
        'base',
        'contacts',
        'website'
    ],
    'data': [
        'security/ir.model.access.csv',
        'views/vehicle_views.xml',
        'views/intervention_views.xml',
        'views/website_templates.xml'
    ],
    'installable': True,
    'application': True,
}