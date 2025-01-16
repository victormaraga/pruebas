# -*- coding: utf-8 -*-
# from odoo import http


# class Gusto(http.Controller):
#     @http.route('/gusto/gusto', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/gusto/gusto/objects', auth='public')
#     def list(self, **kw):
#         return http.request.render('gusto.listing', {
#             'root': '/gusto/gusto',
#             'objects': http.request.env['gusto.gusto'].search([]),
#         })

#     @http.route('/gusto/gusto/objects/<model("gusto.gusto"):obj>', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('gusto.object', {
#             'object': obj
#         })
