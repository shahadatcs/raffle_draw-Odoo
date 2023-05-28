from odoo import api, fields, models
import random


class RaffleDraw(models.Model):
    _name = 'raffle.draw'
    _description = 'Raffle Draw'

    name = fields.Char(string='Name')
    all_student = fields.Many2many('apply.student', string='All Student')
    winner_student = fields.One2many('winner.student', 'raffle_id', string='Result')

    def get_all_student(self):
        records = self.env['apply.student'].search([])
        numbers = records.ids
        self.all_student = [(6, 0, numbers)]

    def raffle_student(self):
        records = self.env['apply.student'].search([])
        numbers = records.ids
        random.shuffle(numbers)
        count = 20  # Number of random numbers to generate
        random_numbers = numbers[:count]

        winners = []
        for number in random_numbers:
            winners.append((0, 0, {'student_id': number}))

        self.winner_student = winners


class WinnerStudent(models.Model):
    _name = 'winner.student'
    _description = 'Winner Student'
    student_id = fields.Many2one('apply.student', string="Id")
    name = fields.Char(related='student_id.student_first_name', string='Name')
    image = fields.Binary(related='student_id.student_image', string='Image')
    fa_name = fields.Char(related='student_id.father_full_name',string='Father Name')
    raffle_id = fields.Many2one('raffle.draw', string='Raffle ID')
    new_id1 = fields.Char(related='student_id.registration_id', string='Barcode Generator1')
    new_id2 = fields.Char(related='student_id.student_birth_certificate_no', string='Barcode Generator2')
    barcode = fields.Char(string='Barcode', compute='_compute_barcode', store=True)

    @api.depends('new_id1', 'new_id2')
    def _compute_barcode(self):
        for rec in self:
            barcode_str = ''
            if rec.new_id1:
                barcode_str += str(rec.new_id1).zfill(5)
            if rec.new_id2:
                barcode_str += str(rec.new_id2).zfill(6)
            rec.barcode = barcode_str
