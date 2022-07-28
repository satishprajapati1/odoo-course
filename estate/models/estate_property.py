
from odoo import fields,models
from datetime import date


class EstateProperty(models.Model):
    _name = 'estate.property'
    _description = 'Real Estate Properties'

    title = fields.Char(required=True)
    description = fields.Text()
    postcode = fields.Char(default='000000')
    available_from = fields.Date(default=lambda x : date.today(),copy=False)
    expected_price = fields.Float(default=000000)
    selling_price = fields.Float(readonly=True,copy=False)
    bedrooms = fields.Integer(default=2)
    living_area = fields.Integer(string="Living Area (sqm)")
    facades = fields.Integer(default='1')
    garage = fields.Boolean()
    garden = fields.Boolean()
    garden_area = fields.Integer(string="Garden Area (sqm)")
    garden_orientation = fields.Selection([('E','East'),('w','West'),('N','North'),('S','South')])
    active = fields.Boolean()
    state = fields.Selection([('new','New'),('or','Offer Received'),('oa','Offer Accepted'),('so','Sold'),('ca','Canceled')])
    property_type = fields.Many2one('estate.property.type')
    buyer = fields.Char()
    seller = fields.Char()
	

class EstatePropertyType(models.Model):
    _name = 'estate.property.type'
    _description = 'Property Types'

    name = fields.Char(required=True)

   