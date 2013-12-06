import sys
import unittest
import os

import rethinkdb as r
from rethinkdb.errors import RqlRuntimeError, RqlDriverError


# conn = r.connect(host='localhost', port=28015, db='sbf_flask_research')
# p = r.table('products')


class ProductsService(object):
    def __init__(self, conn):
        self.conn = conn

    def List(self, product_type=None, brand_name=None, gender=None,
        price_range=None, sizes=None, board_features=None):

        if price_range and len(price_range) != 2:
            raise ValueError("invalid price_range format. should be like this: [2.33, 4.99]")

        q = r.table('products')

        if product_type:
            q = self.filter_equals(q, 'product_type', product_type)

        if brand_name:
            q = q.filter(lambda product:
                (product['brand']['name'] == brand_name)
            )

        if gender:
            q = self.filter_equals(q, 'gender', gender)

        if price_range:
            price_from, price_to = price_range
            q = self.filter_between_range_inclusive(q, 'price', price_from, price_to)

        if sizes:
            q = self.filter_contains(q, 'sizes', sizes)

        if board_features:
            q = q.filter(lambda product:
                (product['board_features']['sysname'].filter(lambda row_field_value:
                    r.expr(['reverse-camber']).contains(row_field_value)
                ).count() > 0)
            )

        results = list(q.run(self.conn))

        return results


    def filter_contains(self, q, field, values):
        return q.filter(lambda row:
            (row[field].filter(lambda row_field_value:
                r.expr(values).contains(row_field_value)
            ).count() > 0)
        )

    def filter_equals(self, q, field, value):
        return q.filter(lambda row:
            (row[field] == value)
        )

    def filter_between_range_inclusive(self, q, field, value_from, value_to):
        return q.filter(lambda row:
            (row[field] >= value_from) &
            (row[field] <= value_to)
        )