# -*- coding: utf-8 -*-

from odoo import models, fields, api


class library_management(models.Model):
    _name = 'library_management.library_management'
    _description = 'library_management.library_management'

    name = fields.Char(string='Percy-Jackson', required=True)
    description = fields.Text(string='Magic and Mystery')
    level = fields.Selection(string='Level', selection=[('Vol1','Lightning Thief'), ('Vol2', 'The sea of monsters'), ('Vol3', 'Titans Curse')], copy=False)
    active = fields.Boolean(string='Active', default=True)