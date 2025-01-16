# -*- coding: utf-8 -*-

from odoo import models, fields, api, _



class GustoTag(models.Model):
    _name = 'gusto.tag'
    _description = 'Gusto Tag'

    tipo_tag_id = fields.Many2one('gusto.tipo.tag', string='Tipo Tag', required=True)
    name = fields.Char(string='Name', required=True)
    nivel = fields.Char(string='Nivel')
    experiencia = fields.Selection([
        ('1', '1'),
        ('2', '2'),
        ('3', '3'),
        ('4', '4'),
        ('5', '5'),
        ('6', '+5')
    ], string='Experiencia')

    gusto_id = fields.Many2one('gusto.gusto')

    tipot_nivel_sino = fields.Boolean(related='tipo_tag_id.nivel_sino', string='Categoria Nivel Sino', store=True)
    tipot_experiencia = fields.Boolean(related='tipo_tag_id.experiencia', string='Categoria Experiencia', store=True)


    @api.onchange('tipo_tag_id')
    def _onchange_tipo_tag(self):
        # Mostrar o esconder los campos dependiendo de la categoría
        if self.tipo_tag_id and self.tipo_tag_id.categoria_id:
            self.nivel = '' if not self.tipo_tag_id.categoria_id.nivel_sino else self.nivel
            self.experiencia = False if not self.tipo_tag_id.categoria_id.experiencia else self.experiencia
