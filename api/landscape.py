from flask import Blueprint, jsonify
from flask_restful import Api, Resource
from flask_cors import CORS

landscape_api = Blueprint('landscape_api', __name__, url_prefix='/api')
CORS(landscape_api) 
api = Api(landscape_api)

class LandscapeAPI:
    @staticmethod
    def get_landscape(name):
        landscapes = {
            "Greatwall": {
                "name": "The Great Wall",
                "location": "China",
                "Introduction": "Protective wall built to keep out invaders",
            },
            "Deathvalley": {
                "name": "Death Valley",
                "location": "United States",
                "Introduction": "Hottest place in the United States",
            },            
        }
        return landscapes.get(name)

    class _greatwall(Resource): 
        def get(self):
            landscape = LandscapeAPI.get_landscape("Greatwall")
            if landscape:
                return jsonify(landscape) 
            return {"Data not found"}, 404 
    class _deathvally(Resource): 
        def get(self):
            landscape = LandscapeAPI.get_landscape("Deathvalley")
            if landscape:
                return jsonify(landscape) 
            return {"Data not found"}, 404 

    # building RESTapi endpoint
api.add_resource(LandscapeAPI._greatwall, '/landscape/greatwall')
api.add_resource(LandscapeAPI._deathvally, '/landscape/deathvalley')

# Instantiate the StudentAPI to register the endpoints
landscape_api_instance = LandscapeAPI()
