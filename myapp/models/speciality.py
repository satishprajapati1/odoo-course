from urllib import request
from odoo import fields,models

class Speciality(models.Model):
    _name = 'speciality'
    _description = 'Speciality'

    speciality = fields.Char()