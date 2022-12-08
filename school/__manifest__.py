{
    'name': 'Escola',
    'version': '15.0.0.0',
    'sumary': 'School Management System',
    'sequence': 1,
    'description': "This is school management system software supported in"
                   "Odoo v15",
    'category': 'School',
    'author': 'Gustavo Salgado Lima',
    'depends': ['base'],
    'data': [
        "data/school_data.xml",
        "security/groups.xml",
        "security/ir.model.access.csv",
        "security/access_rights_data.xml",
        "views/school_view.xml",
    ],
    'demo': [
        "demo/school_demo_data.xml",
    ],
    'application': True
}
