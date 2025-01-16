from flask import Blueprint, request, jsonify
from flask_restful import Api, Resource  # used for REST API building
#from __init__ import app
from model.comment import Comment


comment_api = Blueprint("comment_api", __name__, url_prefix='/api')

api = Api(comment_api)

class CommentAPI:
    """
    Define the API CRUD endpoints for the Comment model.
    There are two operations that correspond to common HTTP methods:
    - post: create a new comment
    - get: get all the comments
    """
    class _CRUD(Resource):
        def post(self):
            """
            Create a new comment.
            """
            print("test")
            
            # Getting the information sent w/ request
            data = request.get_json()

            # Validate data
            if not data:
                return {'message': 'No input data provided'}, 400
            if data.get('comment', '').strip() == '':
                return {'message': 'Empty comment was provided'}, 400
            comment = Comment(data.get('comment', ''))
            comment.create()
            return "success!", 200

    class _BULK_CRUD(Resource):
        def get(self):
            """
            Retrieve all comments.
            """
            comments_array = []
            for comment in Comment.query.all():
                comments_array.append(comment.comment)
            return jsonify(comments_array)

    api.add_resource(_CRUD, '/comment')
    api.add_resource(_BULK_CRUD, '/comment')
