{
    'name': 'Custom Login Odoo',
    'version': '1.0',
    'category': 'Custom',
    'description': 'Modificación del login para agregar un texto personalizado.',
    'author': 'Tu Nombre',
    'depends': ['web'],  # Dependemos del módulo web para poder personalizar el login
    'data': [
        'views/login_template.xml',  # El archivo XML con la plantilla modificada
    ],
    'installable': True,
    'auto_install': False,
}
