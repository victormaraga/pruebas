
from odoo import models, fields, api


class CaptacionExperiencialaboral(models.Model):
    _name = 'captacion.experiencialaboral'
    _description = 'Tabla auxiliar Experiencia Laboral '



    name = fields.Char('EXPERIENCIA LABORAL')
    denominacion = fields.Char('EXPERIENCIA LABORAL')
    company_id = fields.Many2one('res.company', string='Company', required=False,)#default=lambda self.env.company,)
    company_ids = fields.Many2many('res.company',string='Empresas Compartidas',required=False,)#default=lambda self: self.env.company)
    




    