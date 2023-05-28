from odoo import fields, models, api


class StudentReportWizard(models.TransientModel):
    _name = 'student.report.wizard'
    _description = 'Student Report Wizard'

    raffle_id = fields.Many2one('raffle.draw', string='Raffle Winner')

    def action_print_reports(self):
        report_data = []
        for rec in self:
            for student in rec.raffle_id.winner_student:
                report_data.append({
                    'name': student.name,
                    'reg_id': student.new_id1,
                    'father_name': student.student_id.father_full_name,
                    'barcode': student.barcode,
                    'image': student.image
                })
        data = {
            "student_info": report_data
        }
        print(data)
        return self.env.ref('raffle_selection.report_student_details_record').report_action(self, data=data)
