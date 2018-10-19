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
    def test_post_Products(self):
        result=self.app.post('/products', data=json.dumps(self.new_product), content_type="application/json")
        self.assertEqual(result.status_code, 201)