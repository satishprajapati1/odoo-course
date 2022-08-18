from odoo import fields,models

class EstatePropertyType(models.Model):
    _name = 'estate.property.type'
    _description = 'Property Types'
    _order = 'name'

    name = fields.Char(required=True)
    type_ids = fields.One2many('estate.property','property_type_id')
    sequence = fields.Integer('Sequence', default=1, help="Used to order stages. Lower is better.")
    offer_ids = fields.One2many('estate.property.offer','property_id',string="Offers")
    offer_count = fields.Integer(compute='_compute_offer_count')

    _sql_constraints = [
        ('type_uniq','unique(name)','Property type must be unique')
    ]

    def _compute_offer_count(self):
        for record in self:
            record.offer_count = len(record.offer_ids)
