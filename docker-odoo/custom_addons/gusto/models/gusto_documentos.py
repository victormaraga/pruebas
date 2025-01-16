
from odoo import models, fields, api


class GustoDocumentos(models.Model):
    _name = 'gusto.documentos'
    _description = 'Registro de documentos'


    name = fields.Char(string="Nombre del Documento", required=True)
    document_file = fields.Binary(string="Archivo PDF", attachment=True, required=True)
    document_type_id = fields.Many2one('gusto.tipo.documento', string="Tipo de Documento", required=True)
    fecha = fields.Date('Fecha valor', required=True)
    gusto_id = fields.Many2one('gusto.gusto', string="Participante", ondelete='cascade')

    prospector_id = fields.Many2one('gusto.prospectores', string="Prospector", ondelete='cascade')


    

    