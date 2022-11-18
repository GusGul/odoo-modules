{
    'name': 'Biblioteca',
    'version': '15.0.0.0',
    'sumary': 'Library Management System',
    'sequence': 1,
    'description': "This is library management system software supported in"
                   "Odoo v15",
    'category': 'Library',
    'author': 'Gustavo Salgado Lima',
    'depends': ['base'],
    'data': [
        "security/ir.model.access.csv",
        "views/library_view.xml",
        "views/author_profile_view.xml",
        "views/category_view.xml"
    ],
    'aplication': True
}
