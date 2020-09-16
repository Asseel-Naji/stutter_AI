"""
This API will be handling the voice and triggering the Neural network.
"""
from flask import Flask, request, jsonify
from flask_restful import Resource, Api
from flask_cors import CORS
import json


app = Flask(__name__)
api = Api(app)
cors = CORS(app, resources={r"/*": {"origins": "*"}})



class Test(Resource):       
    def post(self):
        return "You didn't mess up yet lol"

api.add_resource(Test, '/test')

if __name__ == '__main__':  
    app.run(host='0.0.0.0', port=5333, debug=True)