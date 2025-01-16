
from odoo import models, fields, api


class GustoSectoresParticipantes(models.Model):
    _name = 'gusto.sectores.participantes'
    _description = 'Registro de Sectores de los participantes de gusto'


    participante_id=fields.Many2one('gusto.gusto', string='participante')
    sectores_id=fields.Many2one('gusto.sectorocupacion', string='sector')