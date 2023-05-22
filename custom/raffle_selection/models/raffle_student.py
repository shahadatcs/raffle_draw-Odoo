from odoo import api, fields, models, _


class RaffleStudent(models.Model):
    _name = 'raffle.student'
    _description = 'Raffle Student'

    name = fields.Char(string='Name')
    winner_ids = fields.Many2many('apply.student', string='Winners')


