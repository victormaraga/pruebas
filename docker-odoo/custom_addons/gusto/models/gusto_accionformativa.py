
from odoo import models, fields, api


class GustoAccionfomativa(models.Model):
    _name = 'gusto.accionformativa'
    _description = 'Registro de accion formativa sto'


    name=fields.Char('Acción Formativa')
    duraccion = fields.Integer('en horas')

    