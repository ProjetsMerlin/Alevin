from odoo import models, fields

class FleetIntervention(models.Model):
    _name = 'fleet.intervention'
    _description = 'Workshop Intervention'
    _order = 'date desc'

    name = fields.Char(
        string='Description',
        required=True
    )

    date = fields.Date(
        string='Date',
        required=True,
        default=fields.Date.today
    )

    vehicle_id = fields.Many2one(
        'fleet.vehicle',
        string='Vehicle',
        required=True
    )

    customer_id = fields.Many2one(
        'res.partner',
        string='Customer'
    )

    mechanic_id = fields.Many2one(
        'res.users',
        string='Mechanic'
    )

    cost = fields.Float(
        string='Cost'
    )

    notes = fields.Text(
        string='Notes'
    )