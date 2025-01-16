# -*- coding: utf-8 -*-

from odoo import models, fields, api, _


class GustoHistoricoSto(models.Model):
    _name = 'gusto.historico.sto'
    _description = 'Registro historico de sto'

    
    id_participante_sto = fields.Integer('ID_STO')         #   PREVISTO STO
    name=fields.Char('DNI/NIE')                            #   STO -> NIF/NIE
    provincia=fields.Char('PROVINCIA')                     #   STO -> PROVINCIA
    participante=fields.Char('PARTICIPANTE')               #   STO -> PARTICIPANTE
    pt_nombre=fields.Char('PT. NOMBRE')                    #   STO -> PT. NOMBRE
    pt_apellido1=fields.Char('PT. APELLIDO1')              #   STO -> PT. APELLIDO1
    pt_apellido2=fields.Char('PT. APELLIDO2')              #   STO -> PT. APELLIDO1
    unidad=fields.Char('UNIDAD')                           #   STO -> UNIDAD
    alta_sto=fields.Date('F. ALTA STO')                    #   STO -> FECHA INICIO
    baja_sto=fields.Date('F. BAJA STO')                    #   STO -> FECHA FIN
    colectivo=fields.Many2one('gusto.colectivo', 'COLECTIVO')           #   STO -> COLECTIVO
    inicio_atencion=fields.Date('INICIO ATENCIÓN')         #   STO -> FECHA INICIO ATENCION
    fin_atencion=fields.Date('FIN ATENCIÓN')               #   STO -> FECHA FIN ATENCION
    h_orienta=fields.Char('H. ORIENTACIÓN')                #   STO -> H. HORIENTA
    h_forma=fields.Char('H. FORMACIÓN')                    #   STO -> H. FORMACION
    recibi=fields.Date('INCENTIVO')                        #   STO -> FECHA RECIBI
    inicio_inserccion=fields.Date('INICIO INSERCCIÓN')     #   STO -> FECHA INICIO INSERCCION
    fin_inserccion=fields.Date('FIN INSERCCIÓN')           #   STO -> FECHA FIN INSERCCION
    h_fase_inserccion=fields.Char('H. FASE INSERCCIÓN')    #   STO -> H. FASE INSERCCION -> ACTUAL OI4OH
    d_fase_inserccion=fields.Char('H. FASE INSERCCIÓN')    #   STO -> d. FASE INSERCCION -> NUEVO
    fecha_valor=fields.Date('FECHA ACTUALIZACION STO')
    
