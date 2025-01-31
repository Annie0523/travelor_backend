from flask import Blueprint, request, jsonify
from flask_restful import Api, Resource
from model.landscape import db, Landscape

landscape_api = Blueprint('landscape_api', __name__, url_prefix='/api')
api = Api(landscape_api)

class LandscapeAPI(Resource):
    def get(self):
        landscapes = Landscape.query.all()
        return jsonify([landscape.read() for landscape in landscapes])

    def post(self):
        data = request.get_json()
        new_landscape = Landscape(data['name'], data['country'], data['city'], data['description'])
        new_landscape.create()
        return jsonify(new_landscape.read()), 201
    
    def delete(self):
        data = request.get_json()
        landscape = Landscape.query.get(data['id'])
        if landscape:
            landscape.delete()
            return jsonify(landscape.read()), 200
        else:
            return jsonify({"error": "Landscape not found"}), 404

api.add_resource(LandscapeAPI, '/landscapes')
