{
    'name': 'Estudantes',
    'version': '15.0.0.0',
    'sumary': 'School Student Management System',
    'sequence': 1,
    'description': "This is school students management system software supported in"
                   "Odoo v15",
    'category': 'School',
    'author': 'Gustavo Salgado Lima',
    'depends': ['base','school'],
    'data': [
        "security/ir.model.access.csv",
        "views/school_student_view.xml",
        "views/school_view.xml",
        "views/hobby_view.xml"
    ],
    'aplication': True
}
