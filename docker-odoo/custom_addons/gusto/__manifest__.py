# -*- coding: utf-8 -*-
{
    'name': "gusto",

    'summary': """
        Gestión Usuarios Sistema Telemático de 
        Orientación""",

    'description': """
        Gestión Usuarios Sistema Telemático de 
        Orientación
    """,

    'author': "My Company",
    'website': "https://www.yourcompany.com",

    # Categories can be used to filter modules in modules listing
    # Check https://github.com/odoo/odoo/blob/16.0/odoo/addons/base/data/ir_module_category_data.xml
    # for the full list
    'category': 'Uncategorized',
    'version': '0.1',

    # any module necessary for this one to work correctly
    'depends': ['base', 'mail'], # 'web'],

    'assets': {
   #'web.assets_backend': [
   #     'gusto/static/src/css/custom.css',   
    #],
    },

    # always loaded
    'data': [
        'security/gusto_gestion_grupos.xml',
        'security/ir.model.access.csv',
        #'security/ir.model.access.orientacion.csv',

        'views/gustos_gusto.xml',
        'views/gustos_acciones_formativas.xml',
        'views/gustos_talleres.xml',
        'views/gustos_contratos.xml',
        'views/gustos_contratos_sum.xml',
        'views/gustos_prospectores.xml',
        'views/gustos_formadores.xml',
        # NECESARIAS
        'views/gustos_docaem.xml',
        'views/gustos_fileviewer.xml',
        'views/gustos_historico_sto.xml',
        'views/gustos_view_form_gusto_talleres_creation.xml',
        'views/gustos_view_form_gusto_contratos_creation.xml',
        'views/gustos_confirm_docaem_wizard.xml',
        'views/gustos_docaem_confirm_wizard.xml',

        # PARAMETRICAS
        'views/gustos_docentes.xml',
        'views/gustos_accionformativa.xml',
        'views/gustos_colectivo.xml',
        'views/gustos_perfilocupacion.xml',
        'views/gustos_sectorocupacion.xml',
        'views/gustos_jornada.xml',
        'views/gustos_taller.xml',
        'views/gustos_tipo_doc.xml',
        
        #'views/gustos_docentes_acciones.xml',
        #'views/gustos_perfiles_participantes.xml',
        #'views/gustos_tipo_documento.xml',
        'views/gustos_tag.xml',
        'views/gustos_tipo_tag.xml',
        'views/gustos_categoria_tag.xml',

        #'views/reporte_personalizado.xml',
        'views/view_gusto_informe_provincia.xml',
        'views/gustos_gusto_sql.xml',

        'views/gustos_contratos_informe.xml',
        'views/gustos_datos.xml',
        'views/gustos_objetivos.xml',
        #'views/gustos_objetivos2.xml',
        #'views/gustos_candidatos.xml',
        #
        #'views/gustos_formaciones.xml',
        #'views/gustos_tipo_formacion.xml',
        #'views/gustos_provisional.xml',
        #'data/notify_cron.xml',
        #'views/gustos_notify_message.xml',
        #'views/gustos_talleres_import_wizard.xml',
        # llamadas a formularios desde gusto
        
        'views/menus.xml',
        #'views/views.xml',
        'views/templates.xml',
    ],
    # only loaded in demonstration mode
    'demo': [
        'demo/demo.xml',
    ],
}
