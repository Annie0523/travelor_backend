from flask import Flask, jsonify
from flask_cors import CORS
from flask import Blueprint, jsonify
from flask_restful import Api, Resource

app = Flask(__name__)
CORS(app)

explore_api = Blueprint('explore_api', __name__, url_prefix='/api')
CORS(explore_api) 
api = Api(explore_api)


# ================== Static DATA ==================
cities_data = [
    {
        "name": "Tokyo",
        "value": "tokyo",
        "position": [35.6895, 139.6917],
        "category": "Modern",
        "interest": "Anime",
    },
    {
        "name": "Mumbai",
        "value": "mumbai",
        "position": [19.0760, 72.8777],
        "category": "Religious",
        "interest": "bollywood",
    },
    {
        "name": "Cairo",
        "value": "cairo",
        "position": [30.0444, 31.2357],
        "category": "historical",
        "interest": "pyramids",
    },
    {
        "name": "Lagos",
        "value": "lagos",
        "position": [6.5244, 3.3792],
        "category": "Scenic",
        "interest": "afrobeat",
    },
    {
        "name": "London",
        "value": "london",
        "position": [51.5074, -0.1278],
        "category": "historical",
        "interest": "theatre",
    },
    {
        "name": "Paris",
        "value": "paris",
        "position": [48.8566, 2.3522],
        "category": "cultural",
        "interest": "fashion",
    },
    {
        "name": "New York City",
        "value": "new_york_city",
        "position": [40.7128, -74.0060],
        "category": "Modern",
        "interest": "Empire State",
    },
    {
        "name": "Mexico City",
        "value": "mexico_city",
        "position": [19.4326, -99.1332],
        "category": "cultural",
        "interest": "Hispanic",
    },
    {
        "name": "São Paulo",
        "value": "sao_paulo",
        "position": [-23.5505, -46.6333],
        "category": "Natural",
        "interest": "party",
    },
    {
        "name": "Buenos Aires",
        "value": "buenos_aires",
        "position": [-34.6037, -58.3816],
        "category": "historical",
        "interest": "football",
    }
]




@app.route("/")
def home():
    return jsonify(cities_data)  # Correct


@app.route("/cities", methods=["GET"])
def get_cities():
    return jsonify(cities_data)


if __name__ == "__main__":
    app.run(debug=True)


#breakpoint on 88

