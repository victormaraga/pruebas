
from odoo import models, fields, api


class GustoSectorocupacion(models.Model):
    _name = 'gusto.sectorocupacion'
    _description = 'Registro de Sector ocupacion de gusto'


    name=fields.Char('Sector Ocupación')