from odoo import fields,models

class Degree(models.Model):
    _name = 'student.degree'
    _description = 'Degree Student is Pursuing'

    name = fields.Char(required=True)
    abbreviation = fields.Char(required=True)

class University(models.Model):
    _name = 'student.university'
    _description = "Student's University"

    name = fields.Char(required=True)
    abbreviation = fields.Char(required=True)
    state = fields.Many2one('res.country.state',required=True)

class Duration(models.Model):
    _name = 'student.duration'
    _description = "Duration of Course"

    name = fields.Integer(required=True,string="Duration (in Years)")
