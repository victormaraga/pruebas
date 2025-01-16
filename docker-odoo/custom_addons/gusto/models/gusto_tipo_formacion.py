from odoo import models, fields

class GustoTipoFormacion(models.Model):
    _name = 'gusto.tipo.formacion'
    _description = 'Tipo Formacion'

    name = fields.Char(string='Tipo Formacion', required=True)