
from odoo import fields,models


class EstateProperty(models.Model):
    _name = 'estate.property'
    _description = 'Real Estate Properties'

    title = fields.Char(required=True)
    description = fields.Char()
    postcode = fields.Char()
    available_from = fields.Date()
    expected_price = fields.Float()
    selling_price = fields.Float()
    bedrooms = fields.Integer()
    living_area = fields.Integer(string="Living Area (sqm)")
    facades = fields.Integer()
    garage = fields.Boolean()
    garden = fields.Boolean()
    garden_area = fields.Integer(string="Garden Area (sqm)")
    garden_orientation = fields.Selection([('E','East'),('w','West'),('N','North'),('S','South')])
    active = fields.Boolean()
	

   