import unittest
import json
from app import create_app

class AddProduct(unittest.TestCase):
    def setUp(self):
        self.app =  create_app().test_client()
        self.app.testing = True
        self.new_product = {
                            "Category" : "Nike",
                            "Name" : "Nike Max",
                            "Description" : "Super power",
                            "Quantity" : 782,
                            "Price" : 1200
                            }
        self.new_sale_order={
                            "Category":"Max",
                            "Name":"Fox",
                            "Quantity":6,
                            "Price":1000
                        }
    def test_post_Products(self):
        result=self.app.post('/products', data=json.dumps(self.new_product), content_type="application/json")
        self.assertEqual(result.status_code, 201)

    def test_get_products(self):
        result=self.app.get('/products', content_type="application/json")
        self.assertEqual(result.status_code, 200)


    def test_post_SaleRecords(self):
        result=self.app.post('/salerecords', data=json.dumps(self.new_sale_order), content_type="application/json")
        self.assertEqual(result.status_code, 201)

    def test_get_SaleRecords(self):
        result=self.app.get('/salerecords', content_type="application/json")
        self.assertEqual(result.status_code, 200)