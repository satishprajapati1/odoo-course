/** @odoo-module **/

import { Order } from 'point_of_sale.models';
import Registries from 'point_of_sale.Registries';

const TaskSatishOrder = (Order) => class TaskSatishOrder extends Order {
    constructor() {
        super(...arguments);
    }
    export_as_JSON() {
        const json = super.export_as_JSON(...arguments);
        json.total_items = this.getTotalItems();
        json.total_qty = this.getTotalQuantities();
        return json;
    }
    init_from_JSON(json) {
        super.init_from_JSON(...arguments);
        this.total_items = 0;
        this.total_qty = 0;
    }
    export_for_printing() {
        const result = super.export_for_printing(...arguments);
        result.total_items = this.getTotalItems();
        result.total_qty = this.getTotalQuantities();
        return result;
    }
    getTotalItems() {
        return this.get_orderlines().length;
    }
    getTotalQuantities(){
        let total_qty = 0;
        for (const line of this.get_orderlines()) {
            total_qty += line.quantity;
        }
        return total_qty;
    }
}
Registries.Model.extend(Order, TaskSatishOrder);