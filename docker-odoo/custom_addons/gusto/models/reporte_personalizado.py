from odoo import models, api

class GustoReportePersonalizado(models.Model):
    _name = 'gusto.reporte.personalizado'
    _description = 'Gusto Reporte Personalizado'

    @api.model
    def generar_reporte(self):
        # Aquí obtendremos los datos como antes.
        Model = self.env['gusto.gusto']

        reporte = [
            {'concepto': 'PARTICIPANTES STO', 'REAL': Model.search_count([]), 'PREV': 0},
            {'concepto': 'BAJAS STO', 'REAL': Model.search_count([('baja_sto', '!=', False)]), 'PREV': 0},
            {'concepto': 'ORIENTACION', 
             'REAL': Model.search_count([('est_orientacion', '=', 'finalizada')]),
             'PREV': Model.search_count([('est_orientacion', '=', 'encurso')])},
            {'concepto': 'PERSONA ATENDIDA', 
             'REAL': Model.search_count([('fase_orienta', '=', 'FINALIZADA')]),
             'PREV': Model.search_count([('fase_orienta', '=', 'EN CURSO')])},
            {'concepto': 'INCENT.PAGADO', 
             'REAL': Model.search_count([('est_incentivo', '=', 'si')]),
             'PREV': Model.search_count([('est_incentivo', '=', 'no'), ('fase_orienta', '=', 'FINALIZADA')])},
            {'concepto': 'OI 40H', 
             'REAL': Model.search_count([('est_orientacion40', '=', 'finalizada')]),
             'PREV': Model.search_count([('est_orientacion40', '=', 'encurso')])},
        ]

        for row in reporte:
            row['TOTAL'] = row['REAL'] + row['PREV']
        
        return reporte

    def imprimir_reporte(self):
        """
        Método para generar el PDF del informe.
        """
        datos_reporte = self.generar_reporte()
        # Renderizar el informe con QWeb
        return self.env.ref('gusto.reporte_personalizado_pdf').report_action(self, data={'reporte': datos_reporte})

