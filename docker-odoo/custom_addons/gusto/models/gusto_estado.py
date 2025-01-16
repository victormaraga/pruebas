
from odoo import models, fields, api


class GustoTaller(models.Model):
    _name = 'gusto.taller'
    _description = 'Registro de taller'


    name=fields.Char('Taller')
    modalidad = fields.Selection([('individual', 'Individual'), ('grupal', 'Grupal')])
    duraccion = fields.Integer('en horas')


    