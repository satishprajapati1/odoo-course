from odoo import fields,models,api,exceptions
from datetime import date

class EstateProperty(models.Model):
    _name = 'estate.property'
    _description = 'Real Estate Properties'
    _order = 'id desc'

    name = fields.Char(required=True,string='Title')
    tag_ids = fields.Many2many('estate.property.tag',string='Tags')
    description = fields.Text()
    postcode = fields.Char(default='000000')
    date_availability = fields.Date(default=lambda x : date.today(),copy=False,string='Available From')
    expected_price = fields.Float(default=000000,required=True)
    selling_price = fields.Float(readonly=True,copy=False)
    bedrooms = fields.Integer(default=2)
    living_area = fields.Integer(string="Living Area (sqm)",required=True)
    facades = fields.Integer(default='1')
    garage = fields.Boolean()
    garden = fields.Boolean()
    garden_area = fields.Integer(string="Garden Area (sqm)")
    garden_orientation = fields.Selection([('E','East'),('w','West'),('N','North'),('S','South')])
    active = fields.Boolean(default=True)
    state = fields.Selection([('new','New'),('or','Offer Received'),('oa','Offer Accepted'),('so','Sold'),('ca','Canceled')],default='new',string='Status')
    property_type_id = fields.Many2one('estate.property.type',string='Property Type')
    buyer = fields.Many2one('res.partner')
    seller = fields.Many2one('res.users',string='Salesman',default=lambda self: self.env.user)
    offer_ids = fields.One2many('estate.property.offer','property_id',string="Offers")
    total_area = fields.Integer(compute='_compute_total_area',readonly=True)
    best_price = fields.Float(string="Best Offer",compute="_compute_best_offer",readonly=True)

    def _compute_total_area(self):
        for record in self:
            record.total_area = record.living_area + record.garden_area

    @api.depends("offer_ids")
    def _compute_best_offer(self):
        for record in self:
            record.best_price = 0
            for r in record.offer_ids:
                if record.best_price < r.price:
                    record.best_price = r.price

    @api.onchange("garden")
    def _onchange_garden(self):
        if self.garden == True:
            self.garden_area = 10
            self.garden_orientation = 'N'
        else: 
            self.garden_area = 0
            self.garden_orientation = ''

    def action_sold(self):
        for record in self:
            if record.state == 'ca':
                raise exceptions.UserError('Canceled Property Cannot be sold')
            record.state = 'so'
        return True

    def action_cancel(self):
        for record in self:
            if record.state == 'so':
                raise exceptions.UserError('Sold Property Cannot be canceled')
            record.state = 'ca'
        return True

    _sql_constraints = [
        ('check_expected_price', 'CHECK(expected_price >= 0)',
         'The expected price must be positive.'),
        ('check_selling_price', 'CHECK(selling_price >= 0)',
         'The selling price must be positive.')
    ]

    @api.constrains("selling_price,excpected_price")
    @api.depends("offer_ids.price")
    def _check_expected_price(self):
        for record in self:
            if ((record.offer_ids.price/record.expected_price)*100)<90:
                raise exceptions.ValidationError("The selling price cannot be lower than 90% of the expected price.")
            return True

    # @api.model
    # def unlink(self):
    #     # Do some business logic, modify vals...
    #     for record in self:
    #         if record.state != 'new' and record.state !='ca':
    #             raise exceptions.UserError('Sold Property Cannot be canceled')
    #     # Then call super to execute the parent method
    #     return super().unlink()