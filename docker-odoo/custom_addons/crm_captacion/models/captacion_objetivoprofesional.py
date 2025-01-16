
from odoo import models, fields, api


class CaptacionObjetivoprofesional(models.Model):
    _name = 'captacion.objetivoprofesional'
    _description = 'Tabla auxiliar Objetivo profesional '



    name = fields.Char('OBJETIVO PROFESIONAL')
    company_id = fields.Many2one('res.company', string='Company', required=False,)#default=lambda self.env.company,)
    company_ids = fields.Many2many('res.company',string='Empresas Compartidas',required=False,)#default=lambda self: self.env.company)
    




    