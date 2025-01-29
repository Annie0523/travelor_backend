from flask import Blueprint, request
from flask_restful import Api, Resource
from flask_cors import CORS
from model.explore import db, Explore, initExplore

# Blueprint + CORS for /api routes
explore_api = Blueprint('explore_api', __name__, url_prefix='/api')
CORS(explore_api)
api = Api(explore_api)

class ExploreAPI(Resource):
    """
    A RESTful API for handling Explore resources.
    Supports GET (all), POST (create), PUT (update), and DELETE (by id).
    """

    def get(self):
        """Retrieve all Explore records from the database."""
        try:
            explores = Explore.query.all()
            # Return a list of dictionaries. Flask-RESTful will auto-JSONify.
            return [explore.serialize() for explore in explores], 200
        except Exception as e:
            return {"error": str(e)}, 500

    def post(self):
        """
        Create a new Explore entry from JSON payload.
        Required JSON fields: 'name', 'value', 'position', 'category', 'interest'.
        """
        try:
            data = request.get_json()
            new_explore = Explore(
                name=data['name'],
                value=data['value'],
                position=data['position'],
                category=data['category'],
                interest=data['interest']
            )
            new_explore.create()  # Writes to DB
            # Return a dict (Flask-RESTful auto-JSONifies); status code 201 indicates "Created"
            return new_explore.serialize(), 201
        except Exception as e:
            return {"error": str(e)}, 400

    def put(self):
        """
        Update an existing Explore entry by 'id'.
        Required JSON fields: 'id', plus any of the fields you want to update:
            'name', 'value', 'position', 'category', 'interest'.
        """
        try:
            data = request.get_json()
            explore_id = data.get('id', None)
            if explore_id is None:
                return {"error": "Missing 'id' in request"}, 400

            explore = Explore.query.get(explore_id)
            if explore is None:
                return {"error": f"Explore with ID {explore_id} not found"}, 404

            # Option A: call model's update() with all data
            explore.update(data)

            # or Option B: manually set fields:
            # explore.name = data.get('name', explore.name)
            # explore.value = data.get('value', explore.value)
            # ... etc. then db.session.commit() ...

            return explore.serialize(), 200
        except Exception as e:
            return {"error": str(e)}, 400

    def delete(self):
        """
        Delete an Explore entry by 'id'.
        Required JSON field: 'id'.
        """
        try:
            data = request.get_json()
            explore_id = data.get('id', None)
            if explore_id is None:
                return {"error": "Missing 'id' in request"}, 400

            explore = Explore.query.get(explore_id)
            if explore:
                explore.delete()
                return {"message": f"Successfully deleted Explore with ID {explore_id}"}, 200
            else:
                return {"error": f"Explore with ID {explore_id} not found"}, 404
        except Exception as e:
            return {"error": str(e)}, 400


# OPTIONAL: If you want an endpoint to re-initialize default data (Tokyo, etc.)
@explore_api.route('/explores/init', methods=['POST'])
def explore_init():
    """
    Re-create the 'explores' table (if needed) and seed with default data.
    You can call this route from Postman: POST /api/explores/init
    """
    try:
        initExplore()
        return {"message": "Explore table initialized with default data"}, 201
    except Exception as e:
        return {"error": str(e)}, 500

# Register the Resource with the API
api.add_resource(ExploreAPI, '/explores')