import os
from flask import Flask
from  app.api.v1 import blp


def create_app():
     app = Flask(__name__)
     app.register_blueprint(blp)
     return app