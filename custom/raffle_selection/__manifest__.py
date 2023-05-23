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

        # 'report/report.xml',
        # 'report/winner_student_details.xml',

        'views/apply_student_view.xml',
        'views/winner_student_view.xml',
        'views/raffle_draw_view.xml',
        'views/menu.xml'

    ],
    'demo': [],
    'application': True,
    'auto_install': False,
    'license': 'LGPL-3',
    'assets': {},
}
