from odoo import fields,models
from datetime import date


class Doctor(models.Model):
    _name = 'doctor'
    _description = 'Doctor'

    doctor_name = fields.Many2one('res.partner',required=True)
    degree = fields.Text(required=True)
    speciality = fields.Selection([('e','Ear'),('n','Nose'),('b','Brain')],required=True)
    licence_number = fields.Char(required=True)

    

   