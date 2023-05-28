{
    'name': 'Admission Selection',
    'version': '1.0.0',
    'sequence': -100,
    'category': 'Admission',
    'summary': 'Raffle Selection Admission Process',
    'description': """Raffle Selection Admission Process""",
    'depends': ['base'],
    'data': [
        'security/ir.model.access.csv',


        'report/student_details_template.xml',
        'report/student_token_template.xml',
        'report/report.xml',

        'wizard/all_student_report_view.xml',
        'wizard/all_student_report_token_view.xml',

        'views/admitted_student_view.xml',
        'views/apply_student_view.xml',
        'views/raffle_draw_view.xml',
        'views/menu.xml'

    ],
    'demo': [],
    'application': True,
    'auto_install': False,
    'license': 'LGPL-3',
    'assets': {},
}
