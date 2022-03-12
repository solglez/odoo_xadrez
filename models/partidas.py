from odoo import models, fields, api
from odoo.exceptions import ValidationError, Warning
import os, pytz, locale

class partidas(models.Model):
    _name = 'odoo_xadrez.partidas'
    _description = 'Partidas de xadrez'

    dataPartida = fields.Date(string="Data da Partida", default=lambda self: fields.Date.today())
    resultado = fields.Selection([('Victoria Blancas', 'Victoria Brancas'), ('Victoria Negras', 'Victoria Negras'), ('Tablas', 'Táboas')], string="Resultado")

    # Das relacións con xogadores (Todo o comentado é de antes de descubrir que era necesario o campo name para as relacións)
    xogadorNegras_id = fields.Many2one('odoo_xadrez.xogadores', ondelete="cascade", required=True, string="Xogador con Negras")
    # nomeConNegras = fields.Char(related="xogadorNegras_id.nomeXogador", string="Nome Negras")
    # apelidosConNegras=fields.Char(related="xogadorNegras_id.apelidosXogador", string="Apelidos Negras")
    # xogadorNegras=fields.Char(compute="_xogadorNegras", string="Xogador con Negras")
    #xogadorNegras=fields.Char(related="xogadorNegras_id.name", string="Xogador con Negras")

    xogadorBrancas_id = fields.Many2one('odoo_xadrez.xogadores', ondelete="cascade", required=True, string="Xogador con Brancas")
    # nomeConBrancas = fields.Char(related="xogadorBrancas_id.nomeXogador", string="Nome Brancas")
    # apelidosConBrancas = fields.Char(related="xogadorBrancas_id.apelidosXogador", string="Apelidos Brancas")
    # xogadorBrancas = fields.Char(compute="_xogadorBrancas", string="Xogador con Brancas")
    #xogadorBrancas = fields.Char(related="xogadorBrancas_id.name", string="Xogador con Brancas")

    # @api.depends('apelidosConNegras', 'nomeConNegras')
    # def _xogadorNegras(self):
    #     for rexistro in self:
    #         rexistro.xogadorNegras = str(rexistro.nomeConNegras)+' '+str(rexistro.apelidosConNegras)
    #
    # @api.depends('apelidosConBrancas', 'nomeConBrancas')
    # def _xogadorBrancas(self):
    #     for rexistro in self:
    #         rexistro.xogadorBrancas = str(rexistro.nomeConBrancas) + ' ' + str(rexistro.apelidosConBrancas)