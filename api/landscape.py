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
        try:
            data = request.get_json()
            if not data:
                return jsonify({"error": "Invalid input: No JSON data provided"}), 400

            required_fields = ['name', 'country', 'city', 'description']
            for field in required_fields:
                if field not in data or not data[field].strip():
                    return jsonify({"error": f"Missing or empty field: {field}"}), 400

            new_landscape = Landscape(
                name=data['name'].strip(),
                country=data['country'].strip(),
                city=data['city'].strip(),
                description=data['description'].strip()
            )

            db.session.add(new_landscape)
            db.session.commit()
            
            return jsonify(new_landscape.read())
        
        except Exception as e:
            db.session.rollback()
            return jsonify({"error": f"An error occurred: {str(e)}"}), 500

    def put(self):
        try:
            data = request.get_json()
            if not data or 'id' not in data:
                return jsonify({"error": "Invalid input: No ID provided"}), 400

            landscape = Landscape.query.get(data['id'])
            if not landscape:
                return jsonify({"error": "Landscape not found"}), 404

            landscape.update(
                name=data.get('name', landscape.name).strip(),
                country=data.get('country', landscape.country).strip(),
                city=data.get('city', landscape.city).strip(),
                description=data.get('description', landscape.description).strip()
            )
            db.session.commit()
            return jsonify(landscape.read())
        except Exception as e:
            db.session.rollback()
            return jsonify({"error": f"An error occurred: {str(e)}"}), 500

    def delete(self):
        try:
            data = request.get_json()
            if not data or 'id' not in data:
                return jsonify({"error": "Invalid input: No ID provided"}), 400

            landscape = Landscape.query.get(data['id'])
            if not landscape:
                return jsonify({"error": "Landscape not found"}), 404

            db.session.delete(landscape)
            db.session.commit()
            return jsonify({"message": "Landscape record deleted successfully"}), 200
        except Exception as e:
            db.session.rollback()
            return jsonify({"error": f"An error occurred: {str(e)}"}), 500

api.add_resource(LandscapeAPI, '/landscapes')
