from odoo import models, fields, api
from odoo.exceptions import ValidationError, Warning
import os, pytz, locale

class provincias(models.Model):
    _name = 'odoo_xadrez.provincias'
    _description = 'provincias'
    #_sql_constraints = [('nomeUnico', 'unique(nomeClube)', 'Non se pode repetir o nome do clube')]

    name =fields.Char(compute="_nombre", string="Provincia") #O campo name é o que se ve representado nas relacións, por iso ten que chamarse name
    nomeProvincia = fields.Char(string="Nome provincia")
    codProvincia = fields.Char(string="Código de Provincia")

    # Da relación con País
    pais_id = fields.Many2one('odoo_xadrez.paises', ondelete="cascade", required=True)

    # Da relación con Clubes
    clubes_ids = fields.One2many("odoo_xadrez.clubes", "provincia_id")

    #O name (que aparece nas relacións) da provincia está formado polo nome da provincia e o código do seu país.
    @api.depends('pais_id', 'nomeProvincia')
    def _nombre(self):
        for rexistro in self:
            if rexistro.pais_id:
                data = ' (' +str(rexistro.pais_id.codPais) + ') '
            else:
                data = ''
            if rexistro.nomeProvincia:
                nom = str(rexistro.nomeProvincia)
            else:
                nom = ''

            rexistro.name = nom + data
