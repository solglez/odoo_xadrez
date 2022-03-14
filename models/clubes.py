from odoo import models, fields, api
from odoo.exceptions import ValidationError, Warning
import os, pytz, locale

class clubes(models.Model):
    _name = 'odoo_xadrez.clubes'
    _description = 'odoo_xadrez de Sol González'
    _sql_constraints = [('nomeUnico', 'unique(nomeClube)', 'Non se pode repetir o nome do clube')]

    name =fields.Char(string="Nome do Clube", required=True) #O campo name é o que se ve representado nas relacións, por iso ten que chamarse name
    nif = fields.Char(string="NIF")
    telefono = fields.Char(string="Teléfono", default="")
    codigoRexistro = fields.Char(string="Código de Rexistro")
    cp = fields.Integer(string="Código Postal")
    localXogo = fields.Char(string="Local de xogo (Enderezo)")
    localidade = fields.Char(string="Localidade")
    #provincia = fields.Char(string="Provincia", default="Pontevedra (ES)")
    pais = fields.Char(string="País", default="España")

    #Da relación con xogadores
    xogadores_ids=fields.One2many("odoo_xadrez.xogadores", "clube_id")

    # Da relación con país - Por defecto España (engadida en templates.xml)
    pais_id = fields.Many2one('odoo_xadrez.paises', ondelete="cascade",
                              default=lambda self: self.env['odoo_xadrez.paises'].search(
                                  [('codPais', '=', "ES")], limit=1))

    # Da relación con provincia - As provincias desplegadas dependen do país (por defecto pontevedra)
    provincia_id = fields.Many2one('odoo_xadrez.provincias', domain="[('pais_id','=',pais_id)]", default=lambda self: self.pais_id.provincias_ids.search(
                                            [], limit=1))


    # provincia_id = fields.Many2one('odoo_xadrez.provincias', domain="[('pais_id','=',pais_id)]", default=lambda self:
    # self.env[pais_id.provincias_ids].search([('codProvincia', '=', 'PON')], limit=1))


    #Da forma seguinte se desplegaban tódalas provincias independentes do país e por defecto era Pontevedra
    # # Da relación con provincia - Por defecto Pontevedra (engadida en templates.xml)
    # provincia_id = fields.Many2one('odoo_xadrez.provincias', ondelete="cascade", required=True,
    #                                default=lambda self: self.env['odoo_xadrez.provincias'].search(
    #                                    [('codProvincia', '=', "PON")], limit=1))

