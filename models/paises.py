from odoo import models, fields, api
from odoo.exceptions import ValidationError, Warning
import os, pytz, locale

class paises(models.Model):
    _name = 'odoo_xadrez.paises'
    _description = 'Paises'
    _sql_constraints = [('nomeUnico', 'unique(nomeClube)', 'Non se pode repetir o nome do clube')]

    name =fields.Char(string="Nome do País")
    codPais = fields.Char(string="Codigo de País")

    #Da relación con provincias
    provincias_ids=fields.One2many("odoo_xadrez.provincias", "pais_id")

    # Da relación con Clubes
    clubes_ids = fields.One2many("odoo_xadrez.clubes", "pais_id")