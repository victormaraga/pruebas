
from odoo import models, fields, api, _

class GustoDocaemConfirmWizard(models.TransientModel):
    _name = 'gusto.docaem.confirm.wizard'
    _description = 'Confirmar Actualización de Documentos'

    docaem_vals = fields.Text(string="Valores a Crear", required=True)
    taller_id = fields.Many2one('gusto.talleres', string="Taller", required=True)

    def action_confirm_update(self):
        """Crear registros en gusto.docaem basados en los valores confirmados."""
        docaem_vals = eval(self.docaem_vals)  # Convertir texto a lista de diccionarios
        if docaem_vals:
            self.env['gusto.docaem'].create(docaem_vals)

    def action_cancel_update(self):
        """Cancelar la actualización y no realizar cambios."""
        return
