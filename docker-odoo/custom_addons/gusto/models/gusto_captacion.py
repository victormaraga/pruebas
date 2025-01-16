from odoo import models, fields, api, _
from datetime import datetime, date, timedelta


class GustoCaptacion(models.Model):
    _inherit = 'res.partner'
    _description = 'Registro de Caaptacion'


    es_captacion = fields.Boolean(string="Es Captacion", default=False)
    
