from odoo import models, fields, api
import base64
import csv
from io import StringIO

class GustoImportcsvAccionesfWizard(models.TransientModel):
    _name = 'gusto.importcsv.accionesf.wizard'
    _description = 'Import CSV for modelo_A'

    csv_file = fields.Binary(string='CSV File', required=True)
    csv_filename = fields.Char(string='File Name')
    csv_record_count = fields.Integer(string='CSV Records', readonly=True)

    


    update_needed_count = fields.Integer(string='Records Requiring Update', readonly=True)
    no_counter = fields.Integer(string='No Pasa', readonly=True)
    datocsv = fields.Char('datocsv')
    datobase = fields.Char('datobase')
    def process_csv(self):
        # Decodificar el archivo CSV
        csv_data = base64.b64decode(self.csv_file)
        data_file = StringIO(csv_data.decode("utf-8"))
        data_file.seek(0)
        file_reader = []
        reader = csv.reader(data_file, delimiter=';')
        
        csv_record_counter = 0
        update_needed_counter = 0
        no_counter = 0

        

        # Leer cada fila del archivo CSV y contar registros
        for row in reader:
            csv_record_counter += 1
            name = row[0]
            pt_nombre = row[1] 
            pt_apellido1 = row[2] 
            pt_apellido2 = row[3] 
            
            # Buscar si el registro ya existe en modelo_A
            record = self.env['gusto.acciones.formativas'].search([('name', '=', name.upper())], limit=1)
            
            if record:
                # Verificar si necesita actualización
                if (record.pt_nombre != pt_nombre or
                    record.pt_apellido1 != pt_apellido1 or
                    record.pt_apellido2 != pt_apellido2):
                    update_needed_counter += 1
            else:
                no_counter += 1
            

        # Actualizar los contadores en el formulario
        self.csv_record_count = csv_record_counter
        self.update_needed_count = update_needed_counter
        self.no_counter = no_counter
        return {
            'type': 'ir.actions.act_window',
            'res_model': 'gusto.importcsv.accionesf.wizard',
            'view_mode': 'form',
            'res_id': self.id,
            'target': 'new',
        }

    def update_records(self):
        # Decodificar el archivo CSV
        csv_data = base64.b64decode(self.csv_file)
        data_file = StringIO(csv_data.decode("utf-8"))
        data_file.seek(0)
        file_reader = []
        reader = csv.reader(data_file, delimiter=',')
        
       
        # Actualizar cada fila del archivo CSV
        for row in reader:
            name = row[0] 
            nexp = row[1] 
            provincias = row[2]  ############## CALCULAR PROVINCIAS
            prev_inicio = row[3] 
            prev_fin = row[4] 
            fecha_inicio = row[5]
            fecha_fin = row[6]
            accion_formativa = row[7]   ######  Buscar acción formativa
            modalidad = row[8]  
            participantes = row[9]      ######  Contar  quizas no 2º vuelta
            prospector = row[10]         ######  Relacionar con prospectores Formador
            docentes = row[11]           ##############  Mismo calculo que provincias
            observacion = row[12]
            # Buscar si el registro ya existe en modelo_A
            record = self.env['gusto.acciones.formativas'].search([('name', '=', name)], limit=1)
            
            if record:
                # Actualizar los campos que sean diferentes


                record.write({
                    'nexp': nexp,
    
                    
                    'prospector_id': prospector,
      
                    'observaciones': observacion
                })
            
        return {
            'type': 'ir.actions.act_window',
            'res_model': 'gusto.importcsv.accionesf.wizard',
            'view_mode': 'form',
            'res_id': self.id,
            'target': 'new',
        }

    def cancel_update(self):
        # Acción para cancelar y salir del formulario
        return {'type': 'ir.actions.act_window_close'}