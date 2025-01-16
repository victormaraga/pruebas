
from odoo import models, fields, api, exceptions, _
import re

class GustoAccionesFormativas(models.Model):
    _name = 'gusto.acciones.formativas'
    #_inherit = 'mail.thread'
    _description = 'Registro de acciones formativas sto'



    id_sto = fields.Integer('ID STO')
    name = fields.Char('Nº AF')
    nexp = fields.Char('Nº EXP Vº Bº')
    country_id = fields.Many2one('res.country', string='PAÍS', default=lambda self: self.env.ref('base.es'))
    provincia_ids = fields.Many2many(
        'res.country.state', 
        string='PROVINCIA',
        domain="[('country_id', '=', country_id), ('name', 'in', ['Cádiz', 'Córdoba', 'Granada', 'Huelva', 'Jaén', 'Málaga', 'Sevilla', 'Almería'])]")
    
    ### Campos añadidos por Victor ### 14/01/2025
    ####################################################
    pt_nombre=fields.Char('PT. NOMBRE')                    #   STO -> PT. NOMBRE
    pt_apellido1=fields.Char('PT. APELLIDO1')              #   STO -> PT. APELLIDO1
    pt_apellido2=fields.Char('PT. APELLIDO2')              #   STO -> PT. APELLIDO1

    provincia_id = fields.Many2one('res.country.state', string="Provincia", domain="[('country_id', '=', country_id)]")
    # provincia_ids = fields.Many2many('res.country.state', string="Provincia", domain="[('country_id', '=', country_id)]")
    company_id = fields.Many2one('res.company', string='Company', required=False,)#default=lambda self.env.company,)
    company_ids = fields.Many2many('res.company',string='Empresas Compartidas',required=False,)#default=lambda self: self.env.company    
    #####################################################
    
    prev_inicio = fields.Date(string='INICIO PREVISTO')    # Debe heredar de prospestor externo previsto
    prev_fin = fields.Date(string='FIN PREVISTO')          # Debe heredar de prospector externo previsto
    inicio = fields.Date(string='INICIO AF')               # Debe Heredar de STO
    fin = fields.Date(string='FIN AF')                     # Debe Heredar de STO
    accion = fields.Many2one('gusto.accionformativa', string='ACCION')
    nombreaccion = fields.Char('DESCRIPCION', related='accion.name')
    modalidad = fields.Selection([('online', 'On line'), ('presencial', 'Presencial')], string='MODALIDAD')
    participantes = fields.Integer(string='Nº PARTICIPANTES')
    prospector_id = fields.Many2one('gusto.prospectores', string='PARTNER')
    formador_id = fields.Many2one('gusto.formadores', string='FORMADOR')
    prospector_factura = fields.Many2one('gusto.formadores', string='FACTURACIÓN')

    recurso = fields.Selection(string='RECURSO', selection=[('interno','INTERNO'),('externo','EXTERNO')])
    estado = fields.Char('ESTADO')
    prosp_form_id = fields.Many2one('gusto.prospectores', string='FORMACION')
    
    contrata_prev = fields.Integer(string='CONTRATACIONES PREV')
    contrata_real = fields.Integer(string='CONTRATACIONES REAL')
    observaciones = fields.Char(string='OBSERVACIONES')
    docente3 = fields.Many2many('gusto.docentes', string='DOCENTES')
    participante_ids = fields.One2many('gusto.gusto', 'acciones_formativas_id', string='PARTICIPANTE')
    n_part_prev = fields.Integer('Nº PART. PREV.')
    n_part_real = fields.Integer('Nº PART. REAL')
    presupuesto_solicitado = fields.Float('PRESUPUESTO SOLICITADO')
    coste = fields.Float('COSTE')
    pendiente_justificar = fields.Float('PENDIENTE JUSTIFICAR')
    validacion = fields.Boolean('VALIDACIÓN')
    horas = fields.Float('HORAS ACCION')



    

    gusto_id = fields.Many2one('gusto.gusto')
    #talleres_id = fields.Many2one('gusto.talleres')

    docaem_ids = fields.One2many('gusto.docaem', 'acciones_id', string='DOCUMENTACION')
    unidad = fields.Char('UNIDAD')
    tipo = fields.Char('TIPO')
    pt_nombre=fields.Char('PT. NOMBRE')                    #   STO -> PT. NOMBRE
    pt_apellido1=fields.Char('PT. APELLIDO1')              #   STO -> PT. APELLIDO1
    pt_apellido2=fields.Char('PT. APELLIDO2')              #   STO -> PT. APELLIDO1



    @api.constrains('modalidad', 'provincia_ids')
    def _check_provincia_ids_limit(self):
        for record in self:
            if record.modalidad == 'presencial' and len(record.provincia_ids) > 1:
                raise exceptions.ValidationError("Solo se permite seleccionar una provincia para la modalidad presencial.")


    @api.model
    def default_get(self, fields):
        res = super(GustoAccionesFormativas, self).default_get(fields)
        res['country_id'] = self.env.ref('base.es').id  # Pone por defecto españa
        return res


   