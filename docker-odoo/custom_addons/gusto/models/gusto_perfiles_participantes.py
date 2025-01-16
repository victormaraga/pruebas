
from odoo import models, fields, api


class GustoPerfilesParticipantes(models.Model):
    _name = 'gusto.perfiles.participantes'
    _description = 'Registro de Perfiles de los participantes de gusto'


    participante_id=fields.Many2one('gusto.gusto', string='participante')
    perfiles_id=fields.Many2one('gusto.perfilocupacion', string='perfil')