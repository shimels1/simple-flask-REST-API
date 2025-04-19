from flask import Flask
from flask_restful import Api
from api.resources.Addition import Addition
from api.resources.Division import Division
from api.resources.Multiplication import Multiplication
from api.resources.Subtraction import Subtraction

app = Flask(__name__)
api = Api(app)

api.add_resource(Addition, "/addition")
api.add_resource(Subtraction, "/subtraction")
api.add_resource(Multiplication, "/multiplication")
api.add_resource(Division, "/division")

if __name__ == '__main__':
    app.run(debug=True)
