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
        self.new_user = {
                      "Username":"Irene",
                      "Password":"12345",

                     }
        self.new_user = {
            "Username":"Irene",
            "Password":12345,

        }


    def test_post_Signup(self):
        result=self.app.post('/signup', data=json.dumps(self.new_user), content_type="application/json")
        self.assertEqual(result.status_code, 200)
    def test_post_Login(self):
        result=self.app.post('/login', data=json.dumps(self.new_user), content_type="application/json")
        self.assertEqual(result.status_code, 200)

    def test_post_Products(self):
        result=self.app.post('/products', data=json.dumps(self.new_product), content_type="application/json")
        self.assertEqual(result.status_code, 201)

    def test_get_products(self):
        result=self.app.get('/products', content_type="application/json")
        self.assertEqual(result.status_code, 200)

    def test_get_specificproduct(self):
        result=self.app.get('/products/1', content_type="application/json")
        self.assertEqual(result.status_code, 200)


    def test_post_SaleRecords(self):
        result=self.app.post('/salerecords', data=json.dumps(self.new_sale_order), content_type="application/json")
        self.assertEqual(result.status_code, 201)

    def test_get_SaleRecords(self):
        result=self.app.get('/salerecords', content_type="application/json")
        self.assertEqual(result.status_code, 200)

    def test_get_SpecificSale(self):
        result=self.app.get('/salerecords/2', content_type="application/json")
        self.assertEqual(result.status_code, 200)
