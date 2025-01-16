from odoo import models, fields

class GustoFormaciones(models.Model):
    _name = 'gusto.formaciones'
    _description = 'Tipo Formaciones'

    
    gusto_id = fields.Many2one('gusto.gusto', string="Participante")
    tipo_formacion = fields.Many2one('gusto.tipo.formacion', string="Tipo")
    accion_id = fields.Many2one('gusto.acciones.formativas', string="Accion Formativa")
    taller_id = fields.Many2one('gusto.talleres', string="Taller")
    fecha_inicio = fields.Date('Inicio')
    fecha_fin = fields.Date("Fin")
    horas = fields.Float('Horas')
    #docaem_ids = fields.Many2many('gusto.docaem')
    
    