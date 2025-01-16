
from odoo import models, fields, api


class CaptacionProyectos(models.Model):
    _name = 'captacion.proyectos'
    _description = 'Registro de proyectos '


    name = fields.Char('DENOMINACION')
    country_id = fields.Many2one('res.country', string="País", default=lambda self: self.env.ref('base.es'))  # Por defecto, España
    provincia_id = fields.Many2one('res.country.state', string="Provincia", domain="[('country_id', '=', country_id)]")
    provincia_ids = fields.Many2many('res.country.state', string="Provincia", domain="[('country_id', '=', country_id)]")
    company_id = fields.Many2one('res.company', string='Company', required=False,)#default=lambda self.env.company,)
    company_ids = fields.Many2many('res.company',string='EMPRESAS',required=False,)#default=lambda self: self.env.company)
    denominacion = fields.Char('DENOMINACION')
    situacion = fields.Selection([('abierto','ABIERTO'), ('cerrado','CERRADO'),], string="ESTADO")
    observaciones = fields.Char('Observaciones')
    participantes_ids = fields.Many2many('captacion.participantes', relation='captacion_participantes_proyectos_rel',string='PARTICIPANTES')
    programas_ids = fields.Many2many('captacion.programas', relation='captacion_programas_proyectos_rel',string='PPROGRAMAS')
    
    




    