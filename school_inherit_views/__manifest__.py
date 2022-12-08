{
    'name': 'Estudantes Inherit Views',
    'version': '15.0.0.0',
    'sumary': 'School Student Inherit View Management System',
    'sequence': 1,
    'description': "This is school students inherit view management system software supported in"
                   "Odoo v15",
    'category': 'School',
    'author': 'Gustavo Salgado Lima',
    'depends': ['base', 'school', 'school_student'],
    'data': [
        "views/student_extend.xml",
    ],
    'application': True
}
