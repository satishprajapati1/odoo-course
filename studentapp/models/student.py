from datetime import date
from odoo import fields,models

class Student(models.Model):
    _name = 'student'

    partner_id = fields.Many2one('res.partner',required=True,string = 'Student name')
    state = fields.Selection([('inquiry','Inquiry'),('counselling','Counselling'),('addmission','Addmission'),('canceled','Canceled')],required=True,string="Stage/State")
    dob = fields.Date(string="Date of Birth",required=True)
    gender = fields.Selection([('m','Male'),('f','Female'),('o','Other')],required=True)
    age = fields.Integer(compute='_compute_dob',readonly=True)
    #Education Background
    last_degree = fields.Many2one('student.degree') 
    university = fields.Many2one('student.university')
    passing_year = fields.Date()
    percentage = fields.Float()

    


    def _compute_dob(self):
        for record in self:
            today = date.today()
            record.age = today.year - record.dob.year -((today.month, today.day) < (record.dob.month , record.dob.day))


