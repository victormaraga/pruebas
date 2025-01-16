
from odoo import models, fields, api


class GustoColectivo(models.Model):
    _name = 'gusto.colectivo'
    _description = 'Registro de Colectivos de gusto'

    
    name=fields.Char('Colectivo')