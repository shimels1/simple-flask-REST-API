from flask import request
from flask_restful import Resource
from util.PostedDataValidation import PostedDataValidation as validation 

class Subtraction(Resource):
    def post(self):
        postedData = request.get_json()
        statusCode = validation.checkPostedData(postedData, "Subtraction")
        print(statusCode)
        if statusCode != 200:
            retJson = {
                "message":"An error happened"
            }
            return retJson, statusCode
        x = postedData["x"]
        y = postedData["y"]
        x = int(x)
        y = int(y)
        ret = x - y
        retMap = {
            'Message': ret
        }
        return retMap, statusCode
