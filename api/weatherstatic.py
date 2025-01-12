from flask import Blueprint, jsonify, request
from flask_restful import Api, Resource
from flask_cors import CORS

# Create Blueprint and API instance
weather_api = Blueprint('weather_api', __name__, url_prefix='/api')
CORS(weather_api)
api = Api(weather_api)

class WeatherAPI:
    @staticmethod
    def get_weather(name):
        cities = {
            "sandiego": {
                "name": "San Diego",
                "value": "san_diego",
                "temperature": "00",
                "feelslike": "00",
                "humidity": "00",
                "pressure": "00",
                "windspeed": "00",
                "winddirection": "00",
            },
            "tokyo": {
                "name": "Tokyo",
                "value": "tokyo",
                "temperature": "00",
                "feelslike": "00",
                "humidity": "00",
                "pressure": "00",
                "windspeed": "00",
                "winddirection": "00",
            },
            "mumbai": {
                "name": "Mumbai",
                "value": "mumbai",
                "temperature": "00",
                "feelslike": "00",
                "humidity": "00",
                "pressure": "00",
                "windspeed": "00",
                "winddirection": "00",
            },
            "cairo": {
                "name": "Cairo",
                "value": "cairo",
                "temperature": "00",
                "feelslike": "00",
                "humidity": "00",
                "pressure": "00",
                "windspeed": "00",
                "winddirection": "00",
            },
            "lagos": {
                "name": "Lagos",
                "value": "lagos",
                "temperature": "00",
                "feelslike": "00",
                "humidity": "00",
                "pressure": "00",
                "windspeed": "00",
                "winddirection": "00",
            },
            "london": {
                "name": "London",
                "value": "london",
                "temperature": "00",
                "feelslike": "00",
                "humidity": "00",
                "pressure": "00",
                "windspeed": "00",
                "winddirection": "00",
            },
            "paris": {
                "name": "Paris",
                "value": "paris",
                "temperature": "00",
                "feelslike": "00",
                "humidity": "00",
                "pressure": "00",
                "windspeed": "00",
                "winddirection": "00",
            },
            "newyorkcity": {
                "name": "New York City",
                "value": "new_york_city",
                "temperature": "00",
                "feelslike": "00",
                "humidity": "00",
                "pressure": "00",
                "windspeed": "00",
                "winddirection": "00",
            },
            "mexicocity": {
                "name": "Mexico City",
                "value": "mexico_city",
                "temperature": "00",
                "feelslike": "00",
                "humidity": "00",
                "pressure": "00",
                "windspeed": "00",
                "winddirection": "00",
            },
            "saopaulo": {
                "name": "Sao Paulo",
                "value": "sao_paulo",
                "temperature": "00",
                "feelslike": "00",
                "humidity": "00",
                "pressure": "00",
                "windspeed": "00",
                "winddirection": "00",
            },
            "buenosaires": {
                "name": "Buenos Aires",
                "value": "buenos_aires",
                "temperature": "00",
                "feelslike": "00",
                "humidity": "00",
                "pressure": "00",
                "windspeed": "00",
                "winddirection": "00",
            },
        }
        return cities.get(name.lower())

    # Individual Resource Classes
    class Sandiego(Resource):
        def get(self):
            print(f"Request URL: {request.path}")  # Debugging request path
            city_data = WeatherAPI.get_weather("sandiego")
            if city_data:
                return jsonify(city_data)
            return {"message": "City not found"}, 404

    class Tokyo(Resource):
        def get(self):
            print(f"Request URL: {request.path}")  # Debugging request path
            city_data = WeatherAPI.get_weather("tokyo")
            if city_data:
                return jsonify(city_data)
            return {"message": "City not found"}, 404

    class Mumbai(Resource):
        def get(self):
            print(f"Request URL: {request.path}")  # Debugging request path
            city_data = WeatherAPI.get_weather("mumbai")
            if city_data:
                return jsonify(city_data)
            return {"message": "City not found"}, 404

    class Cairo(Resource):
        def get(self):
            print(f"Request URL: {request.path}")  # Debugging request path
            city_data = WeatherAPI.get_weather("cairo")
            if city_data:
                return jsonify(city_data)
            return {"message": "City not found"}, 404

    class Lagos(Resource):
        def get(self):
            print(f"Request URL: {request.path}")  # Debugging request path
            city_data = WeatherAPI.get_weather("lagos")
            if city_data:
                return jsonify(city_data)
            return {"message": "City not found"}, 404

    class London(Resource):
        def get(self):
            print(f"Request URL: {request.path}")  # Debugging request path
            city_data = WeatherAPI.get_weather("london")
            if city_data:
                return jsonify(city_data)
            return {"message": "City not found"}, 404

    class Paris(Resource):
        def get(self):
            print(f"Request URL: {request.path}")  # Debugging request path
            city_data = WeatherAPI.get_weather("paris")
            if city_data:
                return jsonify(city_data)
            return {"message": "City not found"}, 404

    class NewYorkCity(Resource):
        def get(self):
            print(f"Request URL: {request.path}")  # Debugging request path
            city_data = WeatherAPI.get_weather("newyorkcity")
            if city_data:
                return jsonify(city_data)
            return {"message": "City not found"}, 404

    class MexicoCity(Resource):
        def get(self):
            print(f"Request URL: {request.path}")  # Debugging request path
            city_data = WeatherAPI.get_weather("mexicocity")
            if city_data:
                return jsonify(city_data)
            return {"message": "City not found"}, 404

    class SaoPaulo(Resource):
        def get(self):
            print(f"Request URL: {request.path}")  # Debugging request path
            city_data = WeatherAPI.get_weather("saopaulo")
            if city_data:
                return jsonify(city_data)
            return {"message": "City not found"}, 404

    class BuenosAires(Resource):
        def get(self):
            print(f"Request URL: {request.path}")  # Debugging request path
            city_data = WeatherAPI.get_weather("buenosaires")
            if city_data:
                return jsonify(city_data)
            return {"message": "City not found"}, 404

# Register Individual Routes
api.add_resource(WeatherAPI.Sandiego, '/cities/sandiego')
api.add_resource(WeatherAPI.Tokyo, '/cities/tokyo')
api.add_resource(WeatherAPI.Mumbai, '/cities/mumbai')
api.add_resource(WeatherAPI.Cairo, '/cities/cairo')
api.add_resource(WeatherAPI.Lagos, '/cities/lagos')
api.add_resource(WeatherAPI.London, '/cities/london')
api.add_resource(WeatherAPI.Paris, '/cities/paris')
api.add_resource(WeatherAPI.NewYorkCity, '/cities/newyorkcity')
api.add_resource(WeatherAPI.MexicoCity, '/cities/mexicocity')
api.add_resource(WeatherAPI.SaoPaulo, '/cities/saopaulo')
api.add_resource(WeatherAPI.BuenosAires, '/cities/buenosaires')
