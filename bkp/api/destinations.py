from flask import Blueprint, jsonify
from flask_restful import Api, Resource
from flask_cors import CORS




destinations_api = Blueprint('destinations_api', __name__, url_prefix='/api')
CORS(destinations_api)
api = Api(destinations_api)
class DestinationsAPI:
    @staticmethod
    def get_destinations(name):
        destination = {
            "Maldives": {
            "name": "Maldives - an island in the Indian Ocean",
            "Climate": "Tropical",
            },
            "Cancun": {
                "name": "Cancun - famous island in Mexico",
                "Climate": "Tropical",
            },  
            "Japan": {
                "name": "Japan",
                "landmarks": "Tokyo"
               
            },
            "Hawaii": {
                "name": "Hawaii",
                "Climate": "Sunny",
                }            
        }
        return destination.get(name)




    class _maldives(Resource):
        def get(self):
            destinations = DestinationsAPI.get_destinations("Maldives")
            if destinations:
                return jsonify(destinations)
            return {"Data not found"}, 404
    class _cancun(Resource):
        def get(self):
            destinations = DestinationsAPI.get_destinations("Cancun")
            if destinations:
                return jsonify(destinations)
            return {"Data not found"}, 404
    class _japan(Resource):
        def get(self):
            destinations = DestinationsAPI.get_destinations("Japan")
            if destinations:
                return jsonify(destinations)
            return {"Data not found"}, 404
    class _hawaii(Resource):
        def get(self):
            destinations = DestinationsAPI.get_destinations("Hawaii")
            if destinations:
                return jsonify(destinations)
            return {"Data not found"}, 404




    # building RESTapi endpoint
api.add_resource(DestinationsAPI._maldives, '/destinations/maldives')
api.add_resource(DestinationsAPI._cancun, '/destinations/cancun')
api.add_resource(DestinationsAPI._japan, '/destinations/japan')
api.add_resource(DestinationsAPI._hawaii, '/destinations/hawaii')




# Instantiate the StudentAPI to register the endpoints
destinations_api_instance = DestinationsAPI()
















from flask import Flask, jsonify
import requests




app = Flask(__name__)


















