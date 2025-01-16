
from odoo import models, fields, api


class GustoTipoDocumento(models.Model):
    _name = 'gusto.tipo.documento'
    _description = 'Registro de tipo documento'


    name = fields.Char(string="Tipo de Documento", required=True)


    