odoo.define('gusto.notification', function (require) {
    "use strict";

    var bus = require('bus.bus').bus;
    var Dialog = require('web.Dialog');

    // Suscribirse a los canales
    bus.on('notification', null, function (notifications) {
        _.each(notifications, function (notification) {
            if (notification[0].startsWith('notify_popup_')) {
                var message = notification[1].message;
                var subject = notification[1].subject;
                Dialog.alert(null, message, { title: subject });
            }
        });
    });

    bus.start_polling();
});
