from flask import Flask
from flask_restful import Api
from resources.Addition import Addition
from resources.Division import Division
from resources.Multiplication import Multiplication
from resources.Subtraction import Subtraction

app = Flask(__name__)
api = Api(app)

api.add_resource(Addition, "/addition")
api.add_resource(Subtraction, "/subtraction")
api.add_resource(Multiplication, "/multiplication")
api.add_resource(Division, "/division")