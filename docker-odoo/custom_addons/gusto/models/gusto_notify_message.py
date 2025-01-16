from odoo import models, fields, api
from datetime import datetime, timedelta

class GustoNotifyMessage(models.Model):
    _name = 'gusto.notify.message'
    _description = 'Notificación de Mensaje'

    name = fields.Char(string='Asunto', required=True)
    message = fields.Text(string='Mensaje', required=True)
    send_date = fields.Datetime(string='Fecha de Envío', default=lambda self: fields.Datetime.now())
    expiration_date = fields.Datetime(string='Fecha de Expiración')
    target_users = fields.Many2many('res.users', string='Usuarios Destinatarios')
    all_users = fields.Boolean(string='Enviar a Todos los Usuarios', default=False)
    sent = fields.Boolean(string='Enviado', default=False)
    auto_close_sessions = fields.Boolean(string='Cerrar Sesiones Automáticamente', default=False)
    close_sessions_date = fields.Datetime(string='Fecha para Cerrar Sesiones')

    @api.model
    def send_message(self):
        """Enviar el mensaje a los usuarios seleccionados o a todos"""
        active_messages = self.search([('sent', '=', False), ('send_date', '<=', fields.Datetime.now())])
        for message in active_messages:
            # Notificar a todos o a usuarios específicos
            if message.all_users:
                users = self.env['res.users'].search([])
            else:
                users = message.target_users

            for user in users:
                # Enviar notificación a cada usuario conectado
                self.env['bus.bus']._sendone(
                    f'notify_popup_{user.id}',
                    'popup_notification',
                    {'message': message.message, 'subject': message.name}
                )
            message.sent = True  # Marcar como enviado

    @api.model
    def close_sessions(self):
        """Cerrar sesiones para mensajes programados"""
        close_messages = self.search([
            ('auto_close_sessions', '=', True),
            ('close_sessions_date', '<=', fields.Datetime.now()),
            ('sent', '=', True)
        ])
        for message in close_messages:
            if message.all_users:
                sessions = self.env['ir.sessions'].search([])
            else:
                sessions = self.env['ir.sessions'].search([('user_id', 'in', message.target_users.ids)])
            sessions.unlink()  # Cerrar sesiones
