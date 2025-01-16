
from odoo import models, fields, api


class GustoTipoContratoss(models.Model):
    _name = 'gusto.tipo.contratoss'
    _description = 'Configuración Tipo Contrato SS'

    name = fields.Char(string='Clave')
    descripcion = fields.Char(string='Descripción')
    comentario = fields.Char(string='Comentario')
    estado = fields.Selection(string="Estado", default="activo",
                             selection=[('activo', 'Activo'),
                                        ('nodisponible', 'No Disponible')])

