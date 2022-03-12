# -*- coding: utf-8 -*-
# from odoo import http


# class OdooXadrez(http.Controller):
#     @http.route('/odoo_xadrez/odoo_xadrez/', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/odoo_xadrez/odoo_xadrez/objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('odoo_xadrez.listing', {
#             'root': '/odoo_xadrez/odoo_xadrez',
#             'objects': http.request.env['odoo_xadrez.odoo_xadrez'].search([]),
#         })

#     @http.route('/odoo_xadrez/odoo_xadrez/objects/<model("odoo_xadrez.odoo_xadrez"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('odoo_xadrez.object', {
#             'object': obj
#         })
