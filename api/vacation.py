from flask import Blueprint, request, jsonify, current_app, Response, g
from flask_restful import Api, Resource
import jwt
from model.vacation import db, Vacation

#
vacation_api = Blueprint('vacation_api', __name__, url_prefix='/api')
api = Api(vacation_api)

# API Resource
class VacationAPI(Resource):
    def get(self):
        try:
            # Fetch all vacation records
            vacations = Vacation.query.all()
            # Serialize the data
            serialized_vacations = [vacation.serialize() for vacation in vacations]
            return (serialized_vacations), 200
            #json = vacations.read()
            #return jsonify(json), 200
        except Exception as e:
            return jsonify({"error": f"An error occurred: {str(e)}"}), 500
        

    def post(self):
        try:
            # Parse JSON data from request
            data = request.get_json()
            if not data:
                return jsonify({"error": "Invalid input: No JSON data provided"}), 400

            # Validate required fields
            required_fields = ['name', 'climate', 'country']
            for field in required_fields:
                if field not in data or not data[field].strip():
                    return jsonify({"error": f"Missing or empty field: {field}"}), 400

            # Create a new Vacation object
            new_vacation = Vacation(
                name=data['name'].strip(),
                climate=data['climate'].strip(),
                country=data['country'].strip()
            )

            # Add to the database
            db.session.add(new_vacation)
            db.session.commit()
            #return "Vacation record added successfully", 201
            # Return the serialized data of the new vacation
            serialized_vacations =  new_vacation.read()
            return (serialized_vacations), 200
            #return jsonify(new_vacation.read()), 201
        except Exception as e:
            db.session.rollback()
            return jsonify({"error": f"An error occurred: {str(e)}"}), 500

    def delete(self):
        try:
            # Parse JSON data from request
            data = request.get_json()
            if not data or 'id' not in data:
                return jsonify({"error": "Invalid input: No ID provided"}), 400

            # Fetch the vacation by ID
            vacation = Vacation.query.get(data['id'])
            if not vacation:
                return jsonify({"error": "Vacation not found"}), 404
            json = vacation.read() 
            # Delete the vacation from the database
            db.session.delete(vacation)
            db.session.commit()
            return 200 
        #jsonify({"message": "Vacation record deleted successfully"}), 200
        except Exception as e:
            db.session.rollback()
            return jsonify({"error": f"An error occurred: {str(e)}"}), 500

# Add the resource to the API
api.add_resource(VacationAPI, '/vacations')
