
from odoo import models, fields, api


class GustoTipoContrato(models.Model):
    _name = 'gusto.tipo.contrato'
    _description = 'Configuración Tipo Contrato'

    name = fields.Char(string='Tipo Contrato')
    estado = fields.Selection(string="Estado", default="activo",
                             selection=[('activo', 'Activo'),
                                        ('nodisponible', 'No Disponible')])

