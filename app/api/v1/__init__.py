from app.api.v1.views import Products, SpecificProduct, SaleRecord,SpecificSale,Login,Signup
from flask import Blueprint
from flask_restful import Api


blp=Blueprint("lop",__name__)
api=Api(blp)
api.add_resource(Products, '/products')
api.add_resource(Signup, '/signup')
api.add_resource(Login, '/login')
api.add_resource(SpecificProduct, '/products/<int:id>')
api.add_resource(SaleRecord, '/salerecords')
api.add_resource(SpecificSale, '/salerecords/<int:id>')