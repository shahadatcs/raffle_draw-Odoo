from odoo import api, fields, models, _
from datetime import date
from odoo.exceptions import ValidationError
from dateutil import relativedelta
import random


# create a database table
class ApplyStudent(models.Model):
    _name = "apply.student"
    _description = "Apply Student"
    _rec_name = "registration_id"

    # student_count = fields.Integer(string='Student Count', compute='_compute_student_count')
    # lucky_student_id = fields.Integer(string='Select Student', compute='student_choice')
    # father info
    father_full_name = fields.Char(string="Full Name")
    father_nationality = fields.Selection([("bangladeshi", "Bangladeshi"), ("arabic", "Arabian")],
                                          tracking=True, default='bangladeshi', string="Nationality")
    father_religion = fields.Selection([("muslim", "Muslim"), ("christian", "Christian")], string="Religion",
                                       tracking=True, default='muslim')

    father_id_no = fields.Char(string="National ID")
    father_academic = fields.Char(string="Academic Qualification")
    father_mob_no = fields.Char(string="Mobile Number")
    father_home_address = fields.Char(string="Home Address")
    father_job = fields.Char(string="Job")
    father_status = fields.Selection([("high", "High"), ("middle", "Middle")], string="Status", default='high')
    father_email = fields.Char(string="Email")

    # student personal info
    student_first_name = fields.Char(string="First Name")
    student_last_name = fields.Char(string="Last Name")
    student_birth_date = fields.Date(string="Birth Date")
    student_age = fields.Integer(string="Age", compute='calculate_age', inverse='_inverse_compute_age')
    student_place_of_birth = fields.Char(string="Place Of Birth")
    student_gender = fields.Selection([('male', 'Male'), ('female', 'Female'), ('other', 'Other')], string='Gender',
                                      tracking=True, default='other')
    student_nationality = fields.Selection([("bangladeshi", "Bangladeshi"), ("arabic", "Arabian")],
                                           tracking=True, default='bangladeshi', string="Nationality")
    student_religion = fields.Selection([("muslim", "Muslim"), ("christian", "Christian")], string="Religion",
                                        tracking=True, default='muslim')
    student_birth_certificate_no = fields.Char(string="Birth Certificate Number")

    # mother info
    mother_full_name = fields.Char(string="Full Name")
    mother_nationality = fields.Selection([("bangladeshi", "Bangladeshi"), ("arabic", "Arabian")],
                                          tracking=True, default='bangladeshi', string="Nationality")
    mother_religion = fields.Selection([("muslim", "Muslim"), ("christian", "Christian")], string="Religion",
                                       tracking=True, default='muslim')
    mother_id_no = fields.Char(string="National ID")
    mother_academic = fields.Char(string="Academic Qualification")
    mother_mob_no = fields.Char(string="Mobile Number")
    mother_home_address = fields.Char(string="Home Address")
    mother_job = fields.Char(string="Job")
    mother_status = fields.Selection([("high", "High"), ("middle", "Middle")], string="Status", default='high')
    mother_email = fields.Char(string="Email")

    # guardian info
    fg_full_name = fields.Char(string="Guardian Full Name")
    fg_relationship = fields.Selection([("muslim", "Muslim"), ("christian", "Christian")],
                                       string="Guardian Relationship With Student")
    fg_job = fields.Char(string="Guardian Job")
    fg_address = fields.Char(string="Guardian Home Address")
    fg_mob = fields.Char(string="Guardian Mobile Phone")

    # enrollment data
    applicant_date = fields.Date(string="Applicant Date")
    registration_date = fields.Date(string="Registration Date")
    grade_level = fields.Char(string="Grade Level")
    registration_id = fields.Char(string="Registration No")
    id_code = fields.Many2many('raffle.student', string="Identification Code")

    # Documents
    student_image = fields.Image(string="Student's Image")
    student_birth_certificate = fields.Image(string="Student's Birth Certificate")
    father_id_copy = fields.Image(string="Father's NID")
    Mother_id_copy = fields.Image(string="Mother's NID")

    # Create Computed Field
    @api.depends('student_birth_date')
    def calculate_age(self):
        for rec in self:
            today = date.today()
            if rec.student_birth_date:
                rec.student_age = today.year - rec.student_birth_date.year
            else:
                rec.student_age = 1

    # Inverse function for age calculation
    @api.depends('student_age')
    def _inverse_compute_age(self):
        today = date.today()
        for rec in self:
            rec.student_birth_date = today - relativedelta.relativedelta(years=rec.student_age)
        return

    # def _compute_student_count(self):
    #     lis = []
    #     for rec in self:
    #         student_count = self.env['apply.student'].search_count([''])
    #         rec.student_count = student_count
    #     print(student_count)

    # @api.depends('student_count')
    # def student_choice(self):
    #     li = []
    #     for rec in self:
    #
    #     print(random.choice())

    # def raffle_student(self):
    #
    #     record = self.env['apply.student'].search([])
    #     numbers = []
    #     for rec in record:
    #         numbers.append(rec.id)
    #
    #     n = self.student_count  # Assuming you want unique random numbers from 0 to 30
    #     count = 20  # Number of random numbers to generate
    #     random.shuffle(numbers)  # Shuffle the list
    #
    #     random_numbers = numbers[:count]  # Select the first 20 shuffled numbers
    #
    #     print(random_numbers)
