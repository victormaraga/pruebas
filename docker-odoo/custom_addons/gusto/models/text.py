gusto_gusto_obj = env['gusto.gusto']

provincias = ['SEVILLA', 'CÓRDOBA', 'GRANADA', 'MÁLAGA', 'JAÉN']

# Iteramos por los registros
for record in records:
    if record.concepto == 'PARTICIPANTES STO' and record.provincia in provincias:
        # Obtenemos el conteo según la provincia
        count = gusto_gusto_obj.search_count([
            ('q_participante', '=', 1),
            ('provincia', '=', record.provincia)
        ])
        # Actualizamos el campo `real` del registro
        record.write({'real': count})
        
    if record.concepto == 'BAJA STO' and record.provincia in provincias:
        # Obtenemos el conteo según la provincia
        count = gusto_gusto_obj.search_count([
            ('q_baja', '=', 1),
            ('provincia', '=', record.provincia)
        ])
        # Actualizamos el campo `real` del registro
        record.write({'real': count})
    
    if record.concepto == 'ORIENTACIÓN' and record.provincia in provincias:
        # Obtenemos el conteo según la provincia
        count = gusto_gusto_obj.search_count([
            ('q_orientacion', '=', 1),
            ('provincia', '=', record.provincia)
        ])
        # Actualizamos el campo `real` del registro
        record.write({'real': count})

    if record.concepto == 'PERSONA ATENDIDA' and record.provincia in provincias:
        # Obtenemos el conteo según la provincia
        count = gusto_gusto_obj.search_count([
            ('q_persona_atendida', '=', 1),
            ('provincia', '=', record.provincia)
        ])
        # Actualizamos el campo `real` del registro
        record.write({'real': count})
    
    if record.concepto == 'INCENT.PAGADO' and record.provincia in provincias:
        # Obtenemos el conteo según la provincia
        count = gusto_gusto_obj.search_count([
            ('q_incentivo', '=', 1),
            ('provincia', '=', record.provincia)
        ])
        # Actualizamos el campo `real` del registro
        record.write({'real': count})
    
    if record.concepto == 'OI 40H' and record.provincia in provincias:
        # Obtenemos el conteo según la provincia
        count = gusto_gusto_obj.search_count([
            ('q_oi40h', '=', 1),
            ('provincia', '=', record.provincia)
        ])
        # Actualizamos el campo `real` del registro
        record.write({'real': count})
    
    if record.concepto == 'INSERTADOS ' and record.provincia in provincias:
        # Obtenemos el conteo según la provincia
        count = gusto_gusto_obj.search_count([
            ('q_insertados', '=', 1),
            ('provincia', '=', record.provincia)
        ])
        # Actualizamos el campo `real` del registro
        record.write({'real': count})
        
    if record.concepto == 'PRIORITARIOS' and record.provincia in provincias:
        # Obtenemos el conteo según la provincia
        count = gusto_gusto_obj.search_count([
            ('q_prioritarios', '=', 1),
            ('provincia', '=', record.provincia)
        ])
        # Actualizamos el campo `real` del registro
        record.write({'real': count})
        
    if record.concepto == 'ISO SIN OI' and record.provincia in provincias:
        # Obtenemos el conteo según la provincia
        count = gusto_gusto_obj.search_count([
            ('q_isosinoi', '=', 1),
            ('provincia', '=', record.provincia)
        ])
        # Actualizamos el campo `real` del registro
        record.write({'real': count})
    
    if record.concepto == 'ISO CON OI' and record.provincia in provincias:
        # Obtenemos el conteo según la provincia
        count = gusto_gusto_obj.search_count([
            ('q_isoconoi', '=', 1),
            ('provincia', '=', record.provincia)
        ])
        # Actualizamos el campo `real` del registro
        record.write({'real': count})


##############################################################
###########     VIEJO  
############################################################
        