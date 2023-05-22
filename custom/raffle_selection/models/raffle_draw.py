from odoo import api, fields, models
import random


class RaffleDraw(models.Model):
    _name = 'raffle.draw'
    _description = 'Raffle Draw'

    name = fields.Char(string='Name')
    prize_ids = fields.Many2many('apply.student', string='Result')

    def all_student(self):
        records = self.env['apply.student'].search([])
        numbers = []
        for rec in records:
            numbers.append(rec.id)
        random_numbers = numbers[:]
        self.write({'prize_ids': [(6, 0, random_numbers)]})

    def raffle_student(self):
        records = self.env['apply.student'].search([])
        numbers = []
        for rec in records:
            numbers.append(rec.id)
        random.shuffle(numbers)
        count = 20  # Number of random numbers to generate
        random_numbers = numbers[:count]
        self.write({'prize_ids': [(6, 0, random_numbers)]})
