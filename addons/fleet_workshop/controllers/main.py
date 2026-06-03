# import re

from odoo import http
from odoo.http import request

class FleetWebsite(http.Controller):

    @http.route('/vehicules', type='http', auth='public', website=True)
    def vehicles(self, **kw):

        domain = []

        search = kw.get('search')

        if search:
            domain.extend([
                '|',
                '|',
                '|',
                ('name', 'ilike', search),
                ('brand', 'ilike', search),
                ('model', 'ilike', search),
                ('immatriculation', 'ilike', search),
            ])

        states = request.httprequest.args.getlist('state')

        if states:
            domain.append(('state', 'in', states))

        brand = kw.get('brand')

        if brand:
            domain.append(('brand', '=', brand))

        order = kw.get('order', 'create_date desc')

        page = int(kw.get('page', 1))

        page_size = 12

        Vehicle = request.env['fleet.vehicle'].sudo()

        total = Vehicle.search_count(domain)

        vehicles = Vehicle.search(
            domain,
            order=order,
            limit=page_size,
            offset=(page - 1) * page_size
        )

        brands = Vehicle.search([]).mapped('brand')

        page_count = (total + page_size - 1) // page_size

        query_string = ''

        for key, value in kw.items():
            if key != 'page':
                query_string += f'&{key}={value}'

        return request.render(
            'fleet_workshop.vehicles_page',
            {
                'vehicles': vehicles,
                'search': search,
                'states': states,
                'brand': brand,
                'brands': brands,
                'order': order,
                'page': page,
                'page_count': page_count,
                'total': total,
                'query_string': query_string
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
    
    @http.route('/vehicules/search', type='json', auth='public', website=True)
    def vehicles_search(self, search='', **kw):

        domain = []

        if search:
            domain.extend([
                '|',
                '|',
                '|',
                ('name', 'ilike', search),
                ('brand', 'ilike', search),
                ('model', 'ilike', search),
                ('immatriculation', 'ilike', search),
            ])

        vehicles = request.env['fleet.vehicle'].sudo().search(
            domain,
            limit=50,
            order='name asc'
        )

        html = request.env['ir.qweb']._render(
            'fleet_workshop.vehicle_cards',
            {
                'vehicles': vehicles
            }
        )

        return {
            'html': html
        }

# Créé des sluges
# class DebugController(http.Controller):
#     @http.route('/debug/slugs', type='http', auth='user')
#     def debug(self, **kw):
#         records = request.env['fleet.vehicle'].sudo().search([])
#         for r in records:
#             if r.name:
#                 r.slug = re.sub(r'[^a-z0-9]+', '-', r.name.lower()).strip('-')
#             else:
#                 r.slug = False
#         return "Slugs updated"