{
    'name': 'Estudantes',
    'version': '15.0.0.0',
    'sumary': 'School Student Management System',
    'sequence': 1,
    'description': "This is school students management system software supported in"
                   "Odoo v15",
    'category': 'School',
    'author': 'Gustavo Salgado Lima',
    'depends': ['base', 'school'],
    'data': [
        "data/hobby.csv",
        "data/school.csv",
        "data/school.student.csv",
        "data/student_data.xml",
        "security/ir.model.access.csv",
        "views/school_student_view.xml",
        "views/school_view.xml",
        "views/hobby_view.xml",
        "wizard/student_fees_update_wizard_view.xml",
    ],
    'pre_init_hook':'_gus_pre_init_hook',
    'post_init_hook':'_gus_post_init_hook',
    'uninstall_hook':'_gus_uninstall_hook',
    'post_load':'_gus_post_load_hook',
    'application': True,
}
