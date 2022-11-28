{
    'name': 'school_extend',
    'version': '15.0.0.0',
    'sumary': 'School Extend',
    'sequence': 1,
    'description': "Extend..."
                   "Odoo v15",
    'category': 'School',
    'author': 'Gustavo Salgado Lima',
    'depends': ['base','school_student'],
    'data': [
        "security/ir.model.access.csv",
        "views/student_extend_view.xml",
    ],
    'aplication': True
}
