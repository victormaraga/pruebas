
from odoo import models, fields, api


class CaptacionNecesidadesformacionespecifica(models.Model):
    _name = 'captacion.necesidadesformacionespecifica'
    _description = 'Tabla auxiliar Necesidades Formacion Especifica'



    name = fields.Char('NECESIDADES FORMACION ESPECIFICA')
    company_id = fields.Many2one('res.company', string='Company', required=False,)#default=lambda self.env.company,)
    company_ids = fields.Many2many('res.company',string='Empresas Compartidas',required=False,)#default=lambda self: self.env.company)
    




    