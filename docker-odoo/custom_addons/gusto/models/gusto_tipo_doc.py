from odoo import models, fields

class GustoTipoDoc(models.Model):
    _name = 'gusto.tipo.doc'
    _description = 'Tipo Documento'

    id = fields.Integer('ID')
    categoria = fields.Selection([
        ('participante', 'Participante'),
        ('administracion', 'Administración')
    ], string='Categoría', required=True)
    #tipo = fields.Selection([('prospeccion','Prospección'),('tallergrupal', 'Taller Grupal'),('')])
    name = fields.Char(string='Name', required=True)