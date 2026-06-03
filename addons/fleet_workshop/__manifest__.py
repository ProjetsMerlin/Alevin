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
        'views/vehicles_templates.xml',
        'views/vehicle_templates.xml',
    ],
    'assets': {
    'web.assets_frontend': [
        'fleet_workshop/static/src/js/vehicle_search.js',
        ],
    },
    'installable': True,
    'application': True,
}