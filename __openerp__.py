# -*- coding: utf-8 -*-
{
    'name': "project_serial_numbers",

    'summary': """
        This module creates the infrastructure to store information about individual components, and
        the groups that contain those elements.""",

    'description': """
    Track serial numbers for pieces of the project

    Each lowest level component has:

    - Name
    - Model/Type
    - Serial Number
    - Firmware Version
    - Notes

    A collection of lowest-level components can be grouped into a Components class. The Components Class can contain more grouped items
    """,

    'author': "Michael Watchorn",
    'website': "http://www.theWatchornGroup.com",

    # Categories can be used to filter modules in modules listing
    # Check https://github.com/odoo/odoo/blob/master/openerp/addons/base/module/module_data.xml
    # for the full list
    'category': 'Project',
    'version': '0.1',

    # any module necessary for this one to work correctly
    'depends': ['base', 'project',],

    # always loaded
    'data': [
        'views/views.xml',
        'security/ir.model.access.csv',
    ],
        # only loaded in demonstration mode
    'demo': [
        #'demo.xml',
    ],
