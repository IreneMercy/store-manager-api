from flask import Flask, jsonify,request, make_response
from flask_restful import Resource, Api

app = Flask (__name__)
api = Api(app)

product_details = []
class Products(Resource):
    def get(self):
        return make_response(jsonify({"product_details":product_details}), 200)

    def post(self):
        data = request.get_json()
        id=len(product_details)+1
        product_category = data['Category']
        product_name = data['Name']
        product_description = data['Description']
        product_quantity = data['Quantity']
        price = data['Price']
        expected_returns = int(price) * int(product_quantity)

        new_product = {
                    "id":id,
                    "Category":product_category,
                    "Name":product_name,
                    "Description":product_description,
                    "Quantity":product_quantity,
                    "Price":price,
                    "Expected Returns":expected_returns
        }

        product_details.append(new_product)
        return make_response( jsonify({"product details":product_details}), 201)

class SpecificProduct(Resource):
    def get(self, id):
        for product in product_details:
            if product['id'] == id:
                return make_response(jsonify({"product_details":product}), 200)
        else:
            return make_response(jsonify({"status" : "Ok",
                                         "Message" : "No product with that id"}))

sale_records=[]
class SaleRecord(Resource):
    def get(self):
        return make_response(jsonify({"sale_records":sale_records}), 200)
    def post(self):
        data = request.get_json()
        id=len(sale_records)+1
        product_category = data['Category']
        product_name = data['Name']
        product_quantity = data['Quantity']
        price = data['Price'] 
        expected_returns = int(price) * int(product_quantity)

        new__sale_order = {
                    "id":id,
                    "Category":product_category,
                    "Name":product_name,
                    "Quantity":product_quantity,
                    "Price":price,
                    "Expected Returns":expected_returns
        }

        sale_records.append(new__sale_order)
        return make_response( jsonify({"sale records":sale_records}), 201)

class SpecificSale(Resource):
    def get(self,id):
        for sale in sale_records:
            if sale['id'] == id:
                return make_response(jsonify({"sale_records":sale}), 200)
        else:
            return make_response(jsonify({"status":"Ok",
                                          "Message":"No sale with that id"}))