from odoo import api, fields, models


class AdmitStudent(models.Model):
    _name = 'admit.student'
    _description = 'Admitted Student'

    st_id = fields.Many2one('winner.student', string='Get Winner Student')
    barcode = fields.Char(string='Barcode')
    name = fields.Char(string='Name', related='st_id.name')
    image = fields.Binary(string='Image', related='st_id.image')
    reg_No = fields.Char(string='Registration No', related='st_id.new_id1')
    admission_confirmed = fields.Boolean(string='Admission Confirmed', default=False)

    def action_search_by_barcode(self):
        for record in self:
            if record.barcode:
                winner_student = self.env['winner.student'].search([('barcode', '=', record.barcode)], limit=1)
                if winner_student:
                    record.st_id = winner_student.id
                    record.name = winner_student.name
                    record.reg_No = winner_student.new_id1
                    record.image = winner_student.image
                else:
                    record.st_id = False
                    record.name = False
                    record.reg_No = False
                    record.image = False

    def action_confirm_admission(self):
        self.admission_confirmed = True
