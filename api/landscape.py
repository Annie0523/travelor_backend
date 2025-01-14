from flask import Blueprint, request, jsonify
from flask_restful import Api, Resource
from flask_cors import CORS
from model.landscape import db, Landscape

landscape_api = Blueprint('landscape_api', __name__, url_prefix='/api')
CORS(landscape_api) 
api = Api(landscape_api)

class LandscapeAPI(Resource):
    def get(self):
        landscapes = Landscape.query.all()
        return jsonify([landscape.serialize() for landscape in landscapes])

    def post(self):
        data = request.get_json()
        new_landscape = Landscape(
            name=data['name'],
            country=data['country'],
            city=data['city'],
            description=data['description']
        )
        db.session.add(new_landscape)
        db.session.commit()
        return jsonify(new_landscape.serialize()), 201

api.add_resource(LandscapeAPI, '/landscapes')
