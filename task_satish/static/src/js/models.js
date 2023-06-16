odoo.define('task_satish.models', function (require) {
    "use strict";

var models = require('point_of_sale.models');

models.load_fields('pos.order',['total_items','total_qty']);

});