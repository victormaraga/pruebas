# -*- coding: utf-8 -*-

from odoo import models, fields, api


class ResPartner(models.Model):
    """Inherits 'res partner' para añadir los campos necesarios para DOCENTES"""
    _inherit = 'res.partner'

    # Para docentes
    es_docente = fields.Boolean()
    estado_docente = fields.Selection(string="Estado", default="libre",
                             selection=[('libre', 'Libre'),
                                        ('ocupado', 'Ocupado'),
                                        ('otro', 'Otro')])

    # Para participantes
    es_participante = fields.Boolean()
    estado_participante = fields.Selection(string="Estado", default="participando",
                             selection=[('participando', 'Participando'),
                                        ('solicitando', 'Solicitando')])

     # Para partners
    es_partner = fields.Boolean()
    estado_partner = fields.Selection(string="Estado", default="disponible",
                             selection=[('disponible', 'Disponible'),
                                        ('ocupado', 'Ocupado')])
