# -*- coding: utf-8 -*-

from odoo import models, fields, api
import logging
_logger = logging.getLogger(__name__)

class GustoInformeProvincia(models.TransientModel):
    _name = 'gusto.informe.provincia'
    _description = 'Informe por Provincia'

    provincia = fields.Char('Provincia')
    total = fields.Integer('Total')
    orientacion_finalizada = fields.Integer('Fase Orientación Finalizada')
    formacion_finalizada = fields.Integer('Estado Formación Finalizada')

    @api.model
    def cargar_datos(self):
        _logger.info("Método cargar_datos ejecutado")
        self.search([]).unlink()
        _logger.info("Registros previos eliminados del modelo transitorio")

        resultados = self.env['gusto.gusto'].obtener_informe_provincia()
        _logger.info(f"Resultados obtenidos: {resultados}")

        for resultado in resultados:
            self.create({
                'provincia': resultado['provincia'],
                'total': resultado['total'],
                'orientacion_finalizada': resultado['orientacion_finalizada'],
                'formacion_finalizada': resultado['formacion_finalizada'],
            })
        _logger.info("Datos cargados en el modelo transitorio")