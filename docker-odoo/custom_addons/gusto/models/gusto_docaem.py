from odoo import models, fields, api, _


class GustoDocaem(models.Model):
    _name = 'gusto.docaem'
    _description = 'Documentos Andalucia Emplea Mas'

    id = fields.Integer(string='ID')
    tipo_doc_id = fields.Many2one('gusto.tipo.doc', string='Tipo Documento')#, required=True)
    grupal = fields.Boolean(string='Grupal', default=False) 
    name = fields.Char(string='Nombre')
    fecha = fields.Date(string='Fecha')
    horas = fields.Integer(string='HORAS')

    ### Campos añadidos por Victor ### 14/01/2025
    ####################################################
    country_id = fields.Many2one('res.country', string="País", default=lambda self: self.env.ref('base.es'))  # Por defecto, España
    provincia_id = fields.Many2one('res.country.state', string="Provincia", domain="[('country_id', '=', country_id)]")
    provincia_ids = fields.Many2many('res.country.state', string="Provincia", domain="[('country_id', '=', country_id)]")
    company_id = fields.Many2one('res.company', string='Company', required=False,)#default=lambda self.env.company,)
    company_ids = fields.Many2many('res.company',string='Empresas Compartidas',required=False,)#default=lambda self: self.env.company)
    ####################################################
    
    # Campo para archivo con límite de 5MB
    archivo = fields.Binary(string='Archivo')
    archivo_nombre = fields.Char(string='Nombre del Archivo')  # Campo auxiliar para el nombre del archivo

    gusto_id = fields.Many2one('gusto.gusto')
    participante_gusto = fields.Char(related='gusto_id.participante', string='PARTICIPANTE')
    gusto_id_id = fields.Integer(related='gusto_id.id', string='ID GUSTO', store=True)

   # gusto_ids = fields.One2many('gusto.gusto', 'taller_id')

    taller_id = fields.Many2one('gusto.talleres')
    taller_id_sto = fields.Integer(related='taller_id.id_sto', string='ID_STO T.')
    taller_id_id = fields.Integer(related='taller_id.id', string='ID_TALLER')

    acciones_id = fields.Many2one('gusto.acciones.formativas')

    contrato_id = fields.Many2one('gusto.contratos', string='CONTRATO')

    # Visor de documento
    def action_open_file_viewer(self):
        # Devuelve la vista del archivo en un formulario popup
        return {
            'name': 'Visor de Archivo',
            'type': 'ir.actions.act_window',
            'view_mode': 'form',
            'res_model': 'gusto.docaem',
            'res_id': self.id,  # Abre el archivo del registro actual
            'views': [(self.env.ref('gusto.view_file_viewer_form').id, 'form')],
            'target': 'new',  # Abrir en un popup
        }
    
   