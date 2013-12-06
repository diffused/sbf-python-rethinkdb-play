import sys
import unittest
import os

import rethinkdb as r
from rethinkdb.errors import RqlRuntimeError, RqlDriverError

import sure

import pprint
pp = pprint.PrettyPrinter(indent=2, width=1).pprint

# pp(unittest)



db_name = 'sbf_flask_research'
products_table = 'products'
conn = r.connect(host='localhost', port=28015, db=db_name)
# conn = r.connect(host='localhost', port=28015)

from snowboard_test_data import test_products

from products_service import ProductsService
# pp(products_service)


class PlayQueries(unittest.TestCase):
    def setUp(self):
        reseed()
        self.products_service = ProductsService(conn)

    def test_all_products(self):
        expected = len(test_products)

        results = self.products_service.List()
        # pp(results)

        len(results).should.equal(expected)

    def test_snowboards(self):
        product_type = 'snowboards'
        expected_length = len([x for x in test_products if (x['product_type'] == 'snowboards')])

        results = self.products_service.List(product_type=product_type)

        len(results).should.equal(expected_length)
        for product in results:
            product['product_type'].should.equal(product_type)

    def test_mens_snowboards(self):
        product_type = 'snowboards'
        gender = 'mens'

        results = self.products_service.List(product_type=product_type, gender=gender)

        len(results).should.be.greater_than(0)
        for p in results:
            p['product_type'].should.equal(product_type)
            p['gender'].should.equal(gender)

    def test_womens_snowboards(self):
        product_type = 'snowboards'
        gender = 'womens'

        results = self.products_service.List(product_type=product_type, gender=gender)

        len(results).should.be.greater_than(0)

        for p in results:
            p['product_type'].should.equal(product_type)
            p['gender'].should.equal(gender)


    def test_snowboards_with_size_157(self):
        product_type = 'snowboards'
        sizes = [157]

        results = self.products_service.List(product_type=product_type, sizes=sizes)

        len(results).should.be.greater_than(0)

        for product in results:
            product['product_type'].should.equal(product_type)
            any(x in sizes for x in product['sizes']).should.be.ok


    def test_snowboards_mens_with_sizes_160_152(self):
        product_type = 'snowboards'
        sizes = [160, 152]
        gender = 'mens'

        results = self.products_service.List(product_type=product_type,
            sizes=sizes, gender=gender)


        len(results).should.be.greater_than(0)

        for product in results:
            product['product_type'].should.equal(product_type)
            any(x in sizes for x in product['sizes']).should.be.ok



    def test_snowboards_with_sizes_160_152(self):
        product_type = 'snowboards'
        sizes = [160, 152]

        results = self.products_service.List(product_type=product_type,
            sizes=sizes)

        for product in results:
            product['product_type'].should.equal(product_type)
            any(x in sizes for x in product['sizes']).should.be.ok

    def test_snowboards_price_of_102_using_between(self):
        product_type = 'snowboards'
        price_from = 102.00
        price_to = 102.00

        results = self.products_service.List(product_type=product_type,
            price_range=[price_from, price_to])

        for p in results:
            p['product_type'].should.equal('snowboards')
            p['price'].should.equal(price_from)
            p['price'].should.equal(price_to)


    def test_snowboards_price_between_100_and_103(self):
        product_type = 'snowboards'
        price_from = 100.00
        price_to = 103.00

        results = self.products_service.List(product_type=product_type,
            price_range=[price_from, price_to])

        for p in results:
            p['product_type'].should.equal('snowboards')
            p['price'].should.be.greater_than_or_equal_to(price_from)
            p['price'].should.be.lower_than_or_equal_to(price_to)


    def test_snowboards_price_between_105_33_and_105_99_to_confirm_decimal_usage(self):
        # to test decimal stuff
        product_type = 'snowboards'
        price_from = 105.98
        price_to = 105.99

        results = self.products_service.List(product_type=product_type,
            price_range=[price_from, price_to])

        len(results).should_not.equal(0)

        for p in results:
            p['product_type'].should.equal(product_type)
            p['price'].should.be.greater_than_or_equal_to(price_from)
            p['price'].should.be.lower_than_or_equal_to(price_to)

    def test_snowboards_price_between_105_33_and_105_99_to_confirm_decimal_usage(self):
        # to test decimal stuff
        product_type = 'snowboards'
        price_range = [100.00]

        self.products_service.List.when.called_with(
                product_type=product_type,
                price_range=price_range
            ).should.throw(
                ValueError,
                "invalid price_range format. should be like this: [2.33, 4.99]"
            )

    def test_snowboards_brand_is_libtech(self):
        product_type = 'snowboards'
        brand_name = 'libtech'

        results = self.products_service.List(
            product_type=product_type, brand_name=brand_name)

        # pp(results)
        len(results).should.be.greater_than(0)

        for p in results:
            p['product_type'].should.equal(product_type)
            p['brand']['name'].should.equal(brand_name)


    def test_snowboards_page_1_with_page_size_3(self):
        pass

    def test_snowboards_page_2_with_page_size_3(self):
        pass

    def test_snowboards_last_page_with_less_results_than_page_size_of_3(self):
        pass

    def test_snowboards_with_board_feature_reverse_camber(self):
        pass
        # todo
        product_type = 'snowboards'
        board_features = ['reverse-camber']

        results = self.products_service.List(
            product_type=product_type,
            board_features=board_features)

        # pp(results)


def reseed():
    db_list = r.db_list().run(conn)

    if db_name not in db_list:
        r.db_create(db_name).run(conn)

    table_list = r.table_list().run(conn)

    if products_table in table_list:
        r.table_drop(products_table).run(conn)

    r.table_create(products_table).run(conn)

    r.table(products_table).insert(test_products).run(conn)


if __name__ == '__main__':
    unittest.main()
    # reseed()

