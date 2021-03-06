# .*. coding: utf-8 .*.

{
    'name': 'Odoo Academy',
    'summary': 'Academy app to manage training',
    'description': """
        Academy Module to manage Training:
        - Courses
        - Sessions
        - Attendees
    """,
    'author': 'Mihir',
    'website': 'https://www.odoo.com',
    'category': 'Training week 2',
    'version': '0.1',
    'depends': ['base'],
    'data': [
        'security/academy_security.xml',
        'security/ir.model.access.csv',
        'views/academy_menuitems.xml',
        'views/course_views.xml',
        'views/session_views.xml',
        'demo/academy_demo.xml',
    ],
    'demo': [
        'demo/academy_demo.xml',
    ],
}