
from odoo import models, fields, api, _
from datetime import datetime, date, timedelta


class GustoContratos(models.Model):
    _name = 'gusto.contratos'
    _description = 'Registro de Contratos de gusto'


    name=fields.Char(string='CONTRATO')                                                                            #       HAY QUE HACER SECUENCIA
    empresa = fields.Char(string='EMPRESA')
    modalidad = fields.Many2one('gusto.tipo.contrato', string="REGIIMEN")
    jornada = fields.Many2one('gusto.jornada', string="JORNADA")
    pmc = fields.Char(string='PMC', related='jornada.pmc')
    tipo_contratoss = fields.Many2one('gusto.tipo.contratoss', string="TIPO CONTRATO SS")                       #      TIPO CONTRATO SEGURIDAD SOCIAL
    peonadas = fields.Integer('PEONADAS')
    fecha_inicio= fields.Date( default=date.today(), string='INICIO')
    fecha_fin=fields.Date(string='FIN')
    porcentaje_jornada = fields.Float(string="% JORNADA", default=100.00)
    observacion = fields.Char(string='OBSERVACIÓN')
    medio = fields.Selection(string='MEDIO', selection=[('autocandidatura','AUTOCANDIDATURA'),('partner','PARTNER'),('prospeccion', 'PROSPECCIÓN')])
    partner_integrador = fields.Many2one('gusto.prospectores', string='INTEGRADO POR')
    
    #######################################################################################################################
    #
    #   RELACIONES
    #
    #######################################################################################################################

    participante_id=fields.Many2one(comodel_name='gusto.gusto', string='DNI', index=True)
    prospector_id=fields.Many2one('gusto.contratos', string='Partner')
    participante_gusto = fields.Char(related='participante_id.participante', string='PARTICIPANTE', index=True, store=True)
    provincia_gusto = fields.Char(related='participante_id.provincia', index=True, string='PROVINCIA', store=True)
    diascomputable_gusto = fields.Integer(related='participante_id.diascomputable', string="DIAS COMPUTABLES ACUM", store=True)
    documento_ids = fields.One2many('gusto.docaem','contrato_id', string='VIDA LABORAL')
    
    archivo = fields.Binary(string='VIDA LABORAL')
    archivo_nombre = fields.Char(string='Nombre del Archivo')  # Campo auxiliar para el nombre del archivo

    ######################################################################################################################
    #
    #   CALCULADOS
    #
    ######################################################################################################################

    diastrabajado = fields.Integer(string="DIAS TRABAJADOS", default=0, compute="_calculate_days", store=True)
    diascomputable = fields.Integer(string="DIAS COMPUTABLES", default=0 , compute="_calculate_days", store=True)
    peonadasc = fields.Integer(string="Contador de peonadas", default=0)
    fecha_objetivo = fields.Date(string='FECHA OBJETIVO')


    ########################################################################################################################
    #
    #  CALCULOS DIAS COMPUTABLES ACTUALES
    #
    ########################################################################################################################
    #
    #  REGIMEN AGRARIO   --> MINIMO 18 DIAS COMPUTABLES DESPUES SE SUMAN
    #
    #  RESTO REGIMENES:
    #
    #  JORNADA COMPLETA  --> MINIMO 30 DIAS PARA COMPUTAR
    #  JORNADA PARCIAL   --> MINIMO 60 DIAS, PARA COMPUTAR, LOS DIAS COMPUTABLES EN FUNCION DEL PORCENTAJE DE CONTRATACIO
    #
    #########################################################################################################################

    suma_diascomputable = fields.Float(
        string="Suma Días Computables",
        compute="_compute_sum_fields",
        store=True
    )
    suma_peonadasc = fields.Integer(
        string="Suma Peonadas",
        compute="_compute_sum_fields",
        store=True
    )

    provincia_participante = fields.Char(
        string="Provincia y Participante",
        compute="_compute_provincia_participante",
        store=True
    )

    #es_maximo = fields.Boolean(string="Es máximo", compute="_compute_es_maximo", store=True)

    #@api.depends('participante_id', 'diascomputable')
    #def _compute_es_maximo(self):
    #    for record in self:
    #        max_dias = self.search([('participante_id', record.participante_id.id)],
    #        order="diascompotable desc", limit=1)
    #        record.es_maximo = max_dias and max_dias.id == record.id

    @api.depends( 'participante_id')
    def _compute_provincia_participante(self):
        for record in self:
            #provincia = record.provincia_gusto or ""
            participante = record.participante_id.name or ""  # Usamos el campo `name` del participante
            participante_name = record.participante_gusto or ""
            record.provincia_participante = f"{participante} - {participante_name}"

    @api.depends('participante_id', 'diascomputable', 'peonadasc')
    def _compute_sum_fields(self):
        grouped_data = {}
        for record in self:
            if record.participante_id:
                key = record.participante_id.id
                if key not in grouped_data:
                    grouped_data[key] = {'diascomputable': 0.0, 'peonadasc': 0}
                grouped_data[key]['diascomputable'] += record.diascomputable
                grouped_data[key]['peonadasc'] += record.peonadasc
        for record in self:
            record.suma_diascomputable = grouped_data.get(record.participante_id.id, {}).get('diascomputable', 0.0)
            record.suma_peonadasc = grouped_data.get(record.participante_id.id, {}).get('peonadasc', 0)

    def ver_archivos(self):
        return 

    @api.model
    def create(self, vals):
        # Crear el registro en gusto.contratos
        contrato = super(GustoContratos, self).create(vals)

        # Crear el registro en gusto.docaem si el campo archivo tiene contenido
        if vals.get('archivo'):
            self.env['gusto.docaem'].create({
                'gusto_id': contrato.participante_id.id,
                'contrato_id': contrato.id,
                'archivo': contrato.archivo,
                'archivo_nombre': contrato.archivo_nombre,
            })
        return contrato

    def write(self, vals):
        # Actualizar el registro en gusto.contratos
        res = super(GustoContratos, self).write(vals)

        # Si el campo archivo ha cambiado, actualizar el registro en gusto.docaem
        if 'archivo' in vals:
            for contrato in self:
                docaem = self.env['gusto.docaem'].search([('contrato_id', '=', contrato.id)], limit=1)
                if docaem:
                    docaem.write({
                        'archivo': vals.get('archivo', contrato.archivo),
                        'archivo_nombre': vals.get('archivo_nombre', contrato.archivo_nombre),
                    })
                else:
                    # Crear el registro en caso de que no exista, aunque debería haberlo al crear
                    self.env['gusto.docaem'].create({
                        'gusto_id': contrato.participante_id.id,
                        'contrato_id': contrato.id,
                        'archivo': vals.get('archivo'),
                        'archivo_nombre': vals.get('archivo_nombre'),
                    })
        return res
    # Visor de documento
    def action_open_file_viewer(self):
        # Devuelve la vista del archivo en un formulario popup
        return {
            'name': 'Visor de Archivo',
            'type': 'ir.actions.act_window',
            'view_mode': 'form',
            'res_model': 'gusto.contratos',
            'res_id': self.id,  # Abre el archivo del registro actual
            'views': [(self.env.ref('gusto.view_file_viewer_form').id, 'form')],
            'target': 'new',  # Abrir en un popup
        }
    

    @api.depends('fecha_inicio','fecha_fin', 'jornada', 'porcentaje_jornada' )
    def _calculate_days(self):
        for rec in self:
            current_month = datetime.now().month
            current_year = datetime.now().year
            if rec.fecha_fin:
                fec_ref = rec.fecha_fin
                rec.diastrabajado = (rec.fecha_fin - rec.fecha_inicio ).days
            else:
                fec_ref = date.today()
                rec.diastrabajado = (fec_ref - rec.fecha_inicio ).days
            if rec.modalidad.name == 'Cuenta ajena (régimen agrario)':
                if current_month == 12:
                    next_month = 1
                    next_year = current_year + 1
                else:
                    next_month = current_month + 1
                    next_year = current_year
                peonadas_mes = self.env['gusto.contratos'].search([
                ('participante_id', '=', rec.participante_id.id),
                ('fecha_inicio', '>=', datetime(current_year, current_month, 1)),
                ('fecha_inicio', '<', datetime(next_year, next_month, 1))
            ])
                if peonadas_mes:
                # Sumar las peonadas del mes en curso
                    total_peonadas = sum(peonadas.peonadas for peonadas in peonadas_mes)
                else:
                    total_peonadas = 0

                # Si la suma excede 18, asignar el total a 'totpeonada'
                if (total_peonadas or rec.peonadasc) > 17:
                    rec.peonadasc += total_peonadas
                else:
                    rec.peonadasc = 0
            else:    
                
                if rec.pmc=='30':
                
                    ndias = 29
                else:
                    
                    ndias = 59

                if (fec_ref  - rec.fecha_inicio ).days > ndias:
                    rec.diascomputable = rec.porcentaje_jornada*(fec_ref - rec.fecha_inicio ).days/100
                else:
                    rec.diascomputable = 0

            if rec.diascomputable_gusto < 120:
                rec.fecha_objetivo = date.today()+timedelta(days=(((120-rec.diascomputable_gusto)*100)/(rec.porcentaje_jornada)))
            else:
                rec.fecha_objetivo = date.today()-timedelta(days=(((rec.diascomputable_gusto-120)*100)/(rec.porcentaje_jornada)))
