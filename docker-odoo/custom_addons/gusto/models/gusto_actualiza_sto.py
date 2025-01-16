# -*- coding: utf-8 -*-

from odoo import models, fields, api


class GustoActualizaSto(models.Model):
    _name = 'gusto.actualiza.sto'
    _description = 'Registro de actualizaciones de sto'

    
    name=fields.Char('DNI/NIE')                            #   STO
    provincia=fields.Char('Provincia')                     #   STO 
    participante=fields.Char('Participante')               #   STO
    pt_nombre=fields.Char('PT. Nombre')                    #   STO
    pt_apellido1=fields.Char('PT. Apellido1')              #   STO
    pt_apellido2=fields.Char('PT. Apellido2')              #   STO
    unidad=fields.Char('Unidad')                           #   STO
    alta_sto=fields.Date('F. Alta STO')                    #   STO
    baja_sto=fields.Date('F. Baja STO')                    #   STO
    colectivo=fields.Many2one('gusto.colectivo')           #   STO
    inicio_atencion=fields.Date('Inicio Atención')         #   STO
    fin_atencion=fields.Date('Fin Atención')               #   STO
    h_forma=fields.Char('H. Formación')                    #   STO
    recibi=fields.Date('Incentivo')                        #   STO
    inicio_inserccion=fields.Date('Inicio Insercción')     #   STO
    fin_inserccion=fields.Date('Fin Insercción')           #   STO
    h_fase_inserccion=fields.Char('H. Fase nsercción')     #   STO
    
    fecha_actualizacion = fields.Date('Fecha de actualización')


   
            
  