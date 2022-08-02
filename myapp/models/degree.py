from odoo import fields,models
from datetime import date


class Degree(models.Model):
    _name = 'degree'
    _description = 'Degree'

    degree = fields.Char()
    