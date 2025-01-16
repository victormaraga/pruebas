from odoo import models, fields, api, tools

class GustoGustoSQL(models.Model):
    _name = 'gusto.gusto.sql'
    _description = 'Modelo SQL para campos calculados'
    _auto = False  # Indica que no se debe crear una tabla automáticamente


    q_participante = fields.Integer(string='PARTICIPANTES STO')
    q_baja = fields.Integer(string='BAJA STO')
    q_orientacion = fields.Integer(string='ORIENTACION')
    q_persona_atendida = fields.Integer(string='PERSONA ATENDIDA')
    q_incentivo = fields.Integer(string='INCENT.PAGADO')
    q_oi40h = fields.Integer(string='OI 40H')
    q_insertados = fields.Integer(string='INSERTADOS')
    q_prioritarios = fields.Integer(string='PRIORITARIOS')
    q_isosinoi = fields.Integer(string='ISO SIN OI')
    q_isoconoi = fields.Integer(string='ISO CON OI')
    provincia=fields.Char('PROVINCIA', index=True)


    @api.model
    def init(self):
        """Crea o reemplaza la vista SQL para este modelo."""
        tools.drop_view_if_exists(self._cr, 'gusto_gusto_sql')
        self._cr.execute("""
            CREATE OR REPLACE VIEW gusto_gusto_sql AS (
                SELECT
                    id AS id,
                    q_participante,
                    q_baja,
                    q_orientacion,
                    q_persona_atendida,
                    q_incentivo, 
                    q_oi40h, 
                    q_insertados,  
                    q_prioritarios,
                    q_isosinoi,    
                    q_isoconoi,    
                    provincia
                FROM
                    gusto_gusto
            )
        """)