from odoo import fields,models

class Courses(models.Model):
    _name = 'student.course'    
    _description = 'Student course'

    name = fields.Char(required=True)
    abbreviation = fields.Char(required=True)
    course_fees = fields.Float(required=True)
    duration = fields.Many2one('student.duration',required=True)
    eligibility = fields.Integer(required=True)
    cutoff = fields.Float(required=True,string = "Minumum Cut off in Percentage")