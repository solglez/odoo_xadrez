from odoo import models, fields, api
from odoo.exceptions import ValidationError, Warning
import os, pytz, locale

class clubes(models.Model):
    _name = 'odoo_xadrez.clubes'
    _description = 'odoo_xadrez de Sol González'
    _sql_constraints = [('nomeUnico', 'unique(nomeClube)', 'Non se pode repetir o nome do clube')]

    name =fields.Char(string="Nome do Clube") #O campo name é o que se ve representado nas relacións, por iso ten que chamarse name
    nif = fields.Char(string="NIF")
    telefono = fields.Char(string="Teléfono", default="")
    codigoRexistro = fields.Char(string="Código de Rexistro")
    cp = fields.Integer(string="Código Postal")
    localXogo = fields.Char(string="Local de xogo (Enderezo)")
    localidade = fields.Char(string="Localidade")
    provincia = fields.Char(string="Provincia", default="Pontevedra (ES)")
    pais = fields.Char(string="País", default="España")

    #Da relación con xogadores
    xogadores_ids=fields.One2many("odoo_xadrez.xogadores", "clube_id")
