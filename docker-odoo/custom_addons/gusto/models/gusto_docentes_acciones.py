
from odoo import models, fields, api


class GustoDocentesAcciones(models.Model):
    _name = 'gusto.docentes.acciones'
    _description = 'Registro de Docente en las acciones de gusto'


    docentes_id=fields.Many2one('gusto.docentes', string='docente')
    accion_id=fields.Many2one('gusto.acciones.formativas', string='Accion')