# -*- encoding:utf-8 -*-

from odoo import fields, models, api

class ProductTemplate(models.Model):
    _inherit = 'product.template'
    is_session_product = fields.Boolean(string="Use as Session Product", default=False)
