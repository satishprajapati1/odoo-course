/** @odoo-module **/

import OrderSummary from 'point_of_sale.OrderSummary';
import Registries from 'point_of_sale.Registries';

export const TaskSatishOrderSummary = (OrderSummary) =>
    class TaskSatishOrderSummary extends OrderSummary {
        getTotalItems() {
            const order = this.env.pos.get_order();
            return order.get_orderlines().length;
        }
        getTotalQuantities() {
            const order = this.env.pos.get_order();
            return order.getTotalQuantities();
        }
    };

Registries.Component.extend(OrderSummary, TaskSatishOrderSummary)
