
{
    'name': 'Custom Login Theme',
    'version': '1.0',
    'category': 'Theme',
    'summary': 'Personaliza el diseño de la pantalla de login',
    'depends': ['web'],
    'data': [
        'views/login_template.xml',
    ],
    'assets': {
        'web.assets_frontend': [
            'custom_login_theme/static/src/css/login_style.css',
        ],
    },
    'installable': True,
    'auto_install': False,
}
