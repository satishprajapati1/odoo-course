{
    'name': 'Task Satish',
    'author' : 'Satish Prajapati',
    "version": "15.0.1.0.0",
    "website": "https://www.tecblic.com",
    'depends': ['point_of_sale'],
    'data' : [
        'views/pos_order_views.xml'
    ],
    'assets': {
        'point_of_sale.assets': [
            'task_satish/static/src/js/*.js',
            'task_satish/static/src/xml/*.xml',
        ],
    },
}
