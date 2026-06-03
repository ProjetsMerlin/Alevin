import re

from odoo import http
from odoo.http import request

class FleetWebsite(http.Controller):

    @http.route('/vehicules', type='http', auth='public', website=True)
    def list_vehicles(self, **kw):

        vehicles = request.env['fleet.vehicle'].sudo().search([])

        return request.render(
            'fleet_workshop.vehicles_page',
            {
                'vehicles': vehicles
            }
        )
    
    @http.route('/vehicules/<string:slug>', type='http', auth='public', website=True)
    def vehicle_detail(self, slug, **kw):
        vehicle = request.env['fleet.vehicle'].sudo().search([('slug', '=', slug)], limit=1)
        if not vehicle:
            return request.not_found()
        return request.render('fleet_workshop.vehicle_detail', {
            'vehicle': vehicle
        })
    
class DebugController(http.Controller):

    @http.route('/debug/slugs', type='http', auth='user')
    def debug(self, **kw):
        records = request.env['fleet.vehicle'].sudo().search([])
        for r in records:
            if r.name:
                r.slug = re.sub(r'[^a-z0-9]+', '-', r.name.lower()).strip('-')
            else:
                r.slug = False
        return "Slugs updated"