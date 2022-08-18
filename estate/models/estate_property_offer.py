from odoo import fields,models,api,exceptions
from datetime import date
import datetime
class EstatePropertyOffer(models.Model):
    _name = 'estate.property.offer'
    _description = 'Property Offers'
    _order = 'price desc'

    price = fields.Float()
    status = fields.Selection([('a','Accepted'),('r','Refused')],copy=False)
    partner_id = fields.Many2one('res.partner',required=True)
    property_id = fields.Many2one('estate.property',required=True)
    validity = fields.Integer(default=7,string='Validity (days)',compute='_compute_validity',inverse='_inverse_validity')
    date_deadline = fields.Date(string="Deadline",default=lambda x : date.today())
    property_type_id = fields.Many2one(related='property_id.property_type_id',stored=True)


    @api.depends("property_id")
    def _compute_validity(self):
        today = date.today()
        for record in self:
            record.validity = record.date_deadline.day - record.property_id.create_date.day

    def _inverse_validity(self):
        for record in self:
            record.date_deadline = datetime.datetime(int(record.property_id.create_date.year),int(record.property_id.create_date.month),int(record.property_id.create_date.day + record.validity))
            
    @api.depends("property_id,partner_id")
    def action_accept(self):
        for record in self:
            if(record.property_id._check_expected_price())==True: 
                record.status = 'a'
                record.property_id.selling_price = record.price
                record.property_id.buyer = record.partner_id
        return True
    
    def action_refuse(self):
        for record in self:
            record.status = 'r'
        return True

    _sql_constraints = [
        ('check_price', 'CHECK(price >= 0)',
         'The price must be positive.')
    ]