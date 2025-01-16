from odoo import models, fields, api, _
import re
from datetime import timedelta
from odoo.exceptions import ValidationError
import logging
_logger = logging.getLogger(__name__)




class GustoTalleress(models.Model):
    _name = 'gusto.talleres'
    _description = 'Registro de talleres'

    id = fields.Integer(string='ID')
    #######################################################################################################
    #
    #    CARGA DEL STO
    #
    #######################################################################################################
    id_sto = fields.Integer('ID_STO')
    country_id = fields.Many2one('res.country', string='País', default=lambda self: self.env.ref('base.es'))
    provincia_id = fields.Many2one('res.country.state',  
                                   domain="[('country_id', '=', country_id), ('name', 'in', ['Cádiz', 'Córdoba', 'Granada', 'Huelva', 'Jaén', 'Málaga', 'Sevilla', 'Almería'])]",
                                   string='PROVINCIA')
    
    ### Campos añadidos por Victor ### 14/01/2025
    ####################################################
    pt_nombre=fields.Char('PT. NOMBRE')                    #   STO -> PT. NOMBRE
    pt_apellido1=fields.Char('PT. APELLIDO1')              #   STO -> PT. APELLIDO1
    pt_apellido2=fields.Char('PT. APELLIDO2')              #   STO -> PT. APELLIDO1

    # provincia_id = fields.Many2one('res.country.state', string="Provincia", domain="[('country_id', '=', country_id)]")
    provincia_ids = fields.Many2many('res.country.state', string="Provincia", domain="[('country_id', '=', country_id)]")
    company_id = fields.Many2one('res.company', string='Company', required=False,)#default=lambda self.env.company,)
    company_ids = fields.Many2many('res.company',string='Empresas Compartidas',required=False,)#default=lambda self: self.env.company    
    #####################################################

    name = fields.Char('DENOMINACION')    
    #tipo_ori = fields.Char('TIPO ORIENTACION')
    fec_inicio = fields.Date('F. INICIO')
    fec_fin = fields.Date('F. FIN')
    horas = fields.Float('HORAS')
    turno = fields.Char('TURNO MÑN-TARDE')
    aula = fields.Char('AULA')
    pt_nombre = fields.Char('NOMBRE')
    pt_apellido1 = fields.Char('APELLIDO1')
    pt_apellido2 = fields.Char('APELLIDO2')
    unidad = fields.Char('UNIDAD')
    tipo = fields.Many2one('gusto.tipo.formacion','TIPO STO')
    tipo_gusto = fields.Many2one('gusto.tipo.doc','TIPO GUSTO')
    estado = fields.Char('ESTADO')

    ######################################################################################################
    #
    #               NECESARIOS PARA GUSTO
    #
    ######################################################################################################


    modalidad = fields.Selection([('individual', 'Individual'), ('grupal', 'Grupal')])
    observaciones = fields.Char('Observaciones')
    docaem_ids = fields.One2many('gusto.docaem', 'taller_id', string='DOCUMENTACION')
    
    participantes_talleres_ids = fields.Many2many('gusto.gusto', relation='gusto_talleres1_rel', string='PARTICIPANTES')
    participantes_talleres2_ids = fields.One2many('gusto.gusto', 'talleres_id')
    gusto_id = fields.Many2one('gusto.gusto', string='PARTICIPANTES') # Necesario para gusto
    gusto_name = fields.Char( related='gusto_id.participante') 
    gusto_id_id = fields.Integer (related='gusto_id.id')
    
 

    @api.onchange('participantes_talleres_ids')
    def onchange_participantes(self):
        """Lógica para manejar el cambio de participantes_talleres_ids."""
        if self.modalidad != 'individual' and self.participantes_talleres_ids:
            return {
                'type': 'ir.actions.act_window',
                'res_model': 'gusto.confirm.docaem.wizard',
                'view_mode': 'form',
                'target': 'new',
                'context': {
                    'default_talleres_id': self.id,
                }
            }
        

    def create_docaem_records(self):
        """Crear registros en gusto.docaem según los criterios establecidos."""
        for record in self:
            if record.fec_inicio and record.fec_fin and record.horas:
                rango_dias = (record.fec_fin - record.fec_inicio).days + 1
                horas_por_dia = record.horas // rango_dias if rango_dias > 0 else 0

                fechas = [record.fec_inicio + timedelta(days=i) for i in range(rango_dias)]
                for fecha in fechas:
                    for participante in record.participantes_talleres_ids:
                        existe = self.env['gusto.docaem'].search([
                            ('talleres_id', '=', record.id),
                            ('fecha', '=', fecha),
                            ('participante', '=', participante.id)
                        ])
                        if not existe:
                            self.env['gusto.docaem'].create({
                                'talleres_id': record.id,
                                'fecha': fecha,
                                'horas': horas_por_dia,
                                'participante': participante.id,
                                'name': f"{participante.name} - {fecha}"
                            })

    def action_view_documents(self):
        return {
            'name': 'Documentos Relacionados',
            'type': 'ir.actions.act_window',
            'res_model': 'gusto.docaem',
            'view_mode': 'form',
            'domain': [('taller_id', '=', self.id), ('gusto_id', '=', self.gusto_id.name)],
            'context': {'default_taller_id': self.id, 'default_gusto_id': self.gusto_id.name},
            'res_id': self.id,  # Abre el archivo del registro actual
            'views': [(self.env.ref('gusto.view_file_viewer_form').id, 'form')],
            'target': 'new',  # Abrir en un popup
        }
    
    def action_open_file_viewer(self):
        # Devuelve la vista del archivo en un formulario popup
        return {
            'name': 'Visor de Archivo',
            'type': 'ir.actions.act_window',
            'view_mode': 'form',
            'res_model': 'gusto.docaem',
            'domain': [('taller_id', '=', self.id), ('gusto_id', '=', self.gusto_id.id)],
            'context': {'default_taller_id': self.id, 'default_gusto_id': self.gusto_id.id},
            'res_id': self.id,  # Abre el archivo del registro actual
            'views': [(self.env.ref('gusto.view_file_viewer_form').id, 'form')],
            'target': 'new',  # Abrir en un popup
        }
    
    
    #@api.model
    #def default_get(self, fields):
    #    """Ajustar el dominio dinámicamente según el contexto."""
    #    res = super(GustoTalleress, self).default_get(fields)
    #    if self.env.context.get('default_modalidad') == 'individual':
    #        # Caso creación desde gusto.gusto: Permitir solo 'INDIVIDUAL'
    #        res['tipo_gusto_domain'] = [('name', 'ilike', 'INDIVIDUAL')]
    #    else:
    #        # Caso creación directa desde gusto.talleres: Excluir 'INDIVIDUAL'
    #        res['tipo_gusto_domain'] = [('name', 'not ilike', 'INDIVIDUAL')]
    #    return res

    @api.onchange('tipo_gusto')
    def _onchange_tipo_gusto(self):
        """Validar que el valor de tipo_gusto cumpla con el dominio."""
        if self.tipo_gusto:
            domain = self.env.context.get('tipo_gusto_domain')
            if domain and not self.tipo_gusto.name in [d[2] for d in domain if 'name' in d]:
                self.tipo_gusto = False
                return {
                    'warning': {
                        'title': 'Selección inválida',
                        'message': 'El valor seleccionado no está permitido para este contexto.',
                    }
                }
    
    
    
    @api.model
    def create(self, vals):
        """
        Sobrescribe el método `create` para manejar tanto diccionarios como enteros y actualizar las relaciones.
        """
        
        _logger.info(f"#####################   Valores recibidos para crear un taller: {vals} . y tambien el gusto id: {self.gusto_id} ")

        # Si vals es un entero, devolver el registro correspondiente (y evitar llamar a create nuevamente)
        if isinstance(vals, int):
            _logger.warning(f"########################   Se recibió un ID en lugar de un diccionario: {vals}. Retornando el registro existente.")
            return self.browse(vals)
        
        # Si vals no es un diccionario, lanzar una excepción
        if not isinstance(vals, dict):
            raise ValidationError(f"#######################   Se esperaba un diccionario, pero se recibió: {type(vals).__name__}")
#
        # Crear el registro con los valores válidos
        res = super(GustoTalleress, self).create(vals)

        # Registrar el ID del nuevo taller
        #_logger.info(f"#######################    Se creó un nuevo taller con ID: {res.id}")

        # Vincular al gusto.gusto si es necesario
        if 'gusto_id' in vals:
            gusto = self.env['gusto.gusto'].browse(vals['gusto_id'])
            _logger.info(f"$$$$$$$$$$$$$$$$$$$$$$$$    El ID del gusto asociado es: {gusto_id}")
            if gusto:
                _logger.info(f"$$$$$$$$$$$$$$$$$$$$$$   Talleres antes de actualizar en gusto.gusto: {gusto.talleres_gusto_ids.ids}")
                gusto.write({'talleres_gusto_ids': [(4, res.id)]})
                _logger.info(f"$$$$$$$$$$$$$$$$$$$$$$$    Talleres después de actualizar en gusto.gusto: {gusto.talleres_gusto_ids.ids}")
#
                # Vincular el participante en el taller
                _logger.info(f"$$$$$$$$$$$$$$$$$   Participantes antes de actualizar en gusto.talleres: {res.participantes_talleres_ids.ids}")
                res.write({'participantes_talleres_ids': [(4, gusto.id)]})
                _logger.info(f"$$$$$$$$$$$$$$$$$$$$$$$   Participantes después de actualizar en gusto.talleres: {res.participantes_talleres_ids.ids}")
#
        return res

