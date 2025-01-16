from odoo import models, fields, api

class GustoConfirmDocaemWizard(models.TransientModel):
    _name = 'gusto.confirm.docaem.wizard'
    _description = 'Confirmación de creación de registros en gusto.docaem'

    talleres_id = fields.Many2one('gusto.talleres', string="Taller")

    def confirm_creation(self):
        """Acción al confirmar la creación de registros."""
        if self.talleres_id:
            self.talleres_id.create_docaem_records()
