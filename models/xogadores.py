from odoo import models, fields, api
from odoo.exceptions import ValidationError, Warning
import os, pytz, locale

class xogadores(models.Model):
    _name = 'odoo_xadrez.xogadores'
    _description = 'Xogadores de xadrez'

    nomeXogador =fields.Char(string="Nome")
    apelidosXogador = fields.Char(string="Apelidos")
    telefonoXogador = fields.Char(string="Teléfono")
    elo=fields.Integer(String="ELO")
    dataNacemento = fields.Date(string="Data de Nacemento")
    foto = fields.Binary(string='Foto')

    #Da relación con clube
    clube_id=fields.Many2one('odoo_xadrez.clubes', ondelete="cascade", required=True)
    #clube_nome=fields.Char(related="clube_id.name", string="Clube", store=True)

    #Das relacións con partidas
    partidasBrancas_ids = fields.One2many("odoo_xadrez.partidas", "xogadorBrancas_id", string="")
    partidasNegras_ids = fields.One2many("odoo_xadrez.partidas", "xogadorNegras_id", string="")

    #Campo name necesario para poder seleccionar por nome nas relacións
    #Como necesitamos que sea o nome + apelidos -> variable computada
    name = fields.Char(compute="_nombre", string="Xogador")

    @api.depends('apelidosXogador', 'nomeXogador')
    def _nombre(self):
        for rexistro in self:
            #Forma cutre de que non escriba False se por algún casual está vacío
            #Este método está mellor implementado no resto de modelos pero: preguiza
            nom=str(rexistro.nomeXogador)
            if nom =='False':
                nom=''
            ape = str(rexistro.apelidosXogador)
            if ape == 'False':
                ape = ''
            rexistro.name = nom + ' ' + ape
