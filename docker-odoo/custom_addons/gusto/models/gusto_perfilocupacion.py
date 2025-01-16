
from odoo import models, fields, api


class GustoPerfilocupacion(models.Model):
    _name = 'gusto.perfilocupacion'
    _description = 'Registro de Perfil Ocupacion de gusto'


    name=fields.Char('Perfil Ocupación')
   