import re
from odoo import models, fields, api

class FleetVehicle(models.Model):
    _name = 'fleet.vehicle'
    _description = 'Fleet Vehicle'

    name = fields.Char(
        string='Reference',
        required=True
    )

    brand = fields.Char(
        string='Brand'
    )

    model = fields.Char(
        string='Model'
    )

    immatriculation = fields.Char(
        string='Immatriculation'
    )

    purchase_date = fields.Date(
        string='Purchase Date'
    )

    mileage = fields.Integer(
        string='Mileage'
    )

    state = fields.Selection(
        [
            ('available', 'Available'),
            ('workshop', 'In Workshop'),
            ('sold', 'Sold')
        ],
        string='Status',
        default='available',
        required=True
    )

    image = fields.Binary(string="Image")

    intervention_ids = fields.One2many(
        'fleet.intervention',
        'vehicle_id',
        string='Interventions'
    )

    slug = fields.Char(index=True, copy=False)

    @api.model_create_multi
    def create(self, vals_list):
        for vals in vals_list:
            name = vals.get('name')
            if name:
                vals['slug'] = self._generate_slug(name)
            else:
                vals['slug'] = False
        return super().create(vals_list)

    def write(self, vals):
        if 'name' in vals:
            vals['slug'] = self._generate_slug(vals.get('name') or '')
        return super().write(vals)

    def _generate_slug(self, value):
        if not value:
            return False
        slug = value.lower()
        slug = re.sub(r'[^a-z0-9]+', '-', slug)
        slug = slug.strip('-')
        return slug or False