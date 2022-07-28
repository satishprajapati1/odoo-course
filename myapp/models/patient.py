from odoo import fields,models
from datetime import date


class Patient(models.Model):
    _name = 'patient'
    _description = 'Patient'

    patient_name = fields.Many2one('res.partner',required=True)
    doctor_name = fields.Many2one('doctor',required=True)
    age = fields.Integer(required=True)
    pre_conditions = fields.Char()
    disease = fields.Char(required=True)
    symptoms = fields.Char(required=True)
    visit_date= fields.Date(default=lambda x : date.today(),required=True)