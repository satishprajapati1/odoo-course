from odoo import models, fields, api


class PosOrder(models.Model):
    _inherit = 'pos.order'

    total_items = fields.Integer(string="Total Items")
    total_qty = fields.Float(string="Total Quantities")

    @api.model
    def _order_fields(self, ui_order):
        order_fields = super(PosOrder, self)._order_fields(ui_order)
        order_fields['total_items'] = ui_order.get('total_items')
        order_fields['total_qty'] = ui_order.get('total_qty')
        return order_fields