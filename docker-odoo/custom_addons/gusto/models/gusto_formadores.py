
from odoo import models, fields, api


class GustoFormadores(models.Model):
    _name = 'gusto.formadores'
    #_inherit = 'mail.thread'
    _description = 'Registro de formadores'


    name=fields.Char('PARTNER')
    telefono=fields.Char('telefono')
    correo=fields.Char('correo')
    es_externo = fields.Boolean('Externo', default=True)

    ### Campos añadidos por Victor ### 14/01/2025
    ####################################################
    country_id = fields.Many2one('res.country', string="País", default=lambda self: self.env.ref('base.es'))  # Por defecto, España
    provincia_id = fields.Many2one('res.country.state', string="Provincia", domain="[('country_id', '=', country_id)]")
    provincia_ids = fields.Many2many('res.country.state', string="Provincia", domain="[('country_id', '=', country_id)]")
    company_id = fields.Many2one('res.company', string='Company', required=False,)#default=lambda self.env.company,)
    company_ids = fields.Many2many('res.company',string='Empresas Compartidas',required=False,)#default=lambda self: self.env.company)
    ####################################################
    
     
    
    #### RELACIONES
    #document_ids = fields.One2many('gusto.documentos', 'prospector_id', string="Documentos PDF")
    docaem_ids = fields.One2many('gusto.docaem', 'gusto_id', string='Documentos')
    acciones_formativas_ids = fields.One2many('gusto.acciones.formativas', 'formador_id', string="Acciones Formativas")

    
    