{
    'name': 'Aulas',
    'version': '15.0.0.0',
    'sumary': 'School Classes Management System',
    'sequence': 1,
    'description': "This is school classes management system software supported in"
                   "Odoo v15",
    'category': 'School',
    'author': 'Gustavo Salgado Lima',
    'depends': ['base', 'school_student'],
    'data': [
        "data/school.class.csv",
        "security/ir.model.access.csv",
        "views/school_class_view.xml",
        "views/school_student_view.xml",
    ],
    'demo': [ ],
    'application': True
}
