
from odoo import models, fields, api


class CaptacionProcedenciaentrada(models.Model):
    _name = 'captacion.procedenciaentrada'
    _description = 'Tabla auxiliar Procedencia Entrada '



    name = fields.Char('PROCEDENCIA ENTRADA')
    #company_id = fields.Many2one('res.company', string='Company', required=False,)#default=lambda self.env.company,)
    




    