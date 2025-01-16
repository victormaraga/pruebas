
from odoo import models, fields, api


class GustoAccionesParticipantes(models.Model):
    _name = 'gusto.acciones.participantes'
    _description = 'Registro de participantes por acción de gusto'


    participante_id=fields.Many2one('gusto.gusto', string='participante')
    acciones_id=fields.Many2one('gusto.acciones.formativas', string='Acción')