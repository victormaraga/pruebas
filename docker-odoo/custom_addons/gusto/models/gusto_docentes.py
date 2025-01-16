
from odoo import models, fields, api


class GustoDocentes(models.Model):
    _name = 'gusto.docentes'
    _description = 'Registro de docentes'


    name=fields.Char('docentes')
