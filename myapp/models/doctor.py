from odoo import fields,models
from datetime import date


class Doctor(models.Model):
    _name = 'doctor'
    _description = 'Doctor'

    doctor_name = fields.Many2one('res.partner',required=True)
    degree = fields.Many2many('degree',required=True)
    speciality = fields.Many2many('speciality',required=True)
    licence_number = fields.Char(required=True)

    

   