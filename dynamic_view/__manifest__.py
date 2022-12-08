

{
    'name': 'Dynamic Views',
    'version': '15.0.0.0',
    'sumary': 'Management System',
    'sequence': 1,
    'description': "",
    'category': 'School',
    'author': 'Gustavo Salgado Lima',
    'depends': ['school','school_student'],
    'data': [
        "views/dynamic_view.xml",
        "security/ir.model.access.csv",
    ],
    'demo': [
      'demo.xml'
    ],
    'application': True
}
