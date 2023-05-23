from odoo import api, fields, models
import random
import barcode
import base64
import qrcode
from io import BytesIO
from barcode import Code128
from barcode.writer import ImageWriter


class RaffleDraw(models.Model):
    _name = 'raffle.draw'
    _description = 'Raffle Draw'

    name = fields.Char(string='Name')
    all_student = fields.Many2many('apply.student', string='All Student')
    winner_student = fields.One2many('winner.student', 'raffle_id', string='Result')

    def get_all_student(self):
        records = self.env['apply.student'].search([])
        numbers = []
        for rec in records:
            numbers.append(rec.id)
        self.write({'all_student': [(6, 0, numbers)]})

    def raffle_student(self):
        records = self.env['apply.student'].search([])
        numbers = []
        for rec in records:
            numbers.append(rec.id)
        random.shuffle(numbers)
        count = 20  # Number of random numbers to generate
        random_numbers = numbers[:count]

        winners = self.env['winner.student']
        for number in random_numbers:
            winners += self.env['winner.student'].new({'student_id': number})

        self.winner_student = winners


class WinnerStudent(models.Model):
    _name = 'winner.student'

    student_id = fields.Many2one('apply.student', string="Id")
    name = fields.Char(string='Name', compute='get_st_name')
    image = fields.Char(string='Image', compute='get_st_img')
    raffle_id = fields.Many2one('raffle.draw', string='Raffle ID')
    new_id1 = fields.Char(string='Barcode Generator1', compute='get_registration_id')
    new_id2 = fields.Char(string='Barcode Generator2', compute='get_certificate_id')
    barcode = fields.Char(string='Barcode', compute='_compute_barcode')

    @api.depends('student_id')
    def get_st_name(self):
        for rec in self:
            rec.name = rec.student_id.student_first_name

    @api.depends('student_id')
    def get_st_img(self):
        for rec in self:
            rec.image = rec.student_id.student_image

    @api.depends('student_id')
    def get_registration_id(self):
        for rec in self:
            rec.new_id1 = rec.student_id.registration_id

    @api.depends('student_id')
    def get_certificate_id(self):
        for rec in self:
            rec.new_id2 = rec.student_id.student_birth_certificate_no

    @api.onchange('new_id')
    def _compute_barcode(self):
        my_str = ''
        for rec in self:
            if rec.new_id1:
                my_str = my_str + str(rec.new_id1).zfill(5)
            if rec.new_id2:
                my_str = my_str + str(rec.new_id2).zfill(6)
            rec.barcode = my_str
            my_str = ''

