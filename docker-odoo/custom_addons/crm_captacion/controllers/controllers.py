# -*- coding: utf-8 -*-
# from odoo import http


# class Andalucia(http.Controller):
#     @http.route('/andalucia/andalucia', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/andalucia/andalucia/objects', auth='public')
#     def list(self, **kw):
#         return http.request.render('andalucia.listing', {
#             'root': '/andalucia/andalucia',
#             'objects': http.request.env['andalucia.andalucia'].search([]),
#         })

#     @http.route('/andalucia/andalucia/objects/<model("andalucia.andalucia"):obj>', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('andalucia.object', {
#             'object': obj
#         })
