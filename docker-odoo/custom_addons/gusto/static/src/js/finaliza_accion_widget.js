odoo.define('gusto.finaliza_accion_widget', function (require) {
    "use strict";

    const fieldRegistry = require('web.field_registry');
    const FieldBoolean = require('web.basic_fields').FieldBoolean;

    const FinalizaAccionWidget = FieldBoolean.extend({
        _render: function () {
            // Limpiar el contenido actual
            this.$el.empty();

            // Crear un elemento <span> con texto basado en el valor del campo
            const span = $('<span>');
            if (this.value) {
                span.text('FINALIZADO');
                span.addClass('text-success'); // Clase CSS para estilos opcionales
            } else {
                span.text('NO FINALIZADO');
                span.addClass('text-danger'); // Clase CSS para estilos opcionales
            }

            // Añadir el <span> al campo
            this.$el.append(span);
        },
    });

    // Registrar el widget para usarlo en las vistas XML
    fieldRegistry.add('finaliza_accion_widget', FinalizaAccionWidget);
});
