from flask import Blueprint, jsonify
from flask_restful import Api, Resource
from flask_cors import CORS

weather_api = Blueprint('weather_api', __name__, url_prefix='/api')
CORS(weather_api) 
api = Api(weather_api)

class WeatherAPI:
    @staticmethod
    def get_weather(name):
        cities = {
            "Sandiego": {
                "name": "San Diego",
                "value": "san_diego",
                "temperature":"00",
                "feelslike": "00",
                "humidity": "00",
                "pressure": "00",
                "windspeed": "00",
                "winddirection": "00",
            },
            "Tokyo": {
                "name": "Tokyo",
                "value": "tokyo",
                "temperature":"00",
                "feelslike": "00",
                "humidity": "00",
                "pressure": "00",
                "windspeed": "00",
                "winddirection": "00",
            },
            "Mumbai": {
                "name": "Mumbai",
                "value": "mumbai",
                "temperature":"00",
                "feelslike": "00",
                "humidity": "00",
                "pressure": "00",
                "windspeed": "00",
                "winddirection": "00",
            },
            "Cairo": {
                "name": "Cairo",
                "value": "cairo",
                "temperature":"00",
                "feelslike": "00",
                "humidity": "00",
                "pressure": "00",
                "windspeed": "00",
                "winddirection": "00",
            },
            "Lagos": {
                "name": "Lagos",
                "value": "lagos",
                "temperature":"00",
                "feelslike": "00",
                "humidity": "00",
                "pressure": "00",
                "windspeed": "00",
                "winddirection": "00",
            },
            "London": {
                "name": "London",
                "value": "london",
                "temperature":"00",
                "feelslike": "00",
                "humidity": "00",
                "pressure": "00",
                "windspeed": "00",
                "winddirection": "00",
            },
            "Paris": {
                "name": "Paris",
                "value": "paris",
                "temperature":"00",
                "feelslike": "00",
                "humidity": "00",
                "pressure": "00",
                "windspeed": "00",
                "winddirection": "00",
            },
            "Newyorkcity": {
                "name": "New York City",
                "value": "new_york_city",
                "temperature":"00",
                "feelslike": "00",
                "humidity": "00",
                "pressure": "00",
                "windspeed": "00",
                "winddirection": "00",
            },
            "Mexicocity": {
                "name": "Mexico City",
                "value": "mexico_city",
                "temperature":"00",
                "feelslike": "00",
                "humidity": "00",
                "pressure": "00",
                "windspeed": "00",
                "winddirection": "00",
            },
            "Saopaulo": {
                "name": "Sao Paulo",
                "value": "sao_paulo",
                "temperature":"00",
                "feelslike": "00",
                "humidity": "00",
                "pressure": "00",
                "windspeed": "00",
                "winddirection": "00",
            },
            "Buenosaires": {
                "name": "Buenos Aires",
                "value": "buenos_aires",
                "temperature":"00",
                "feelslike": "00",
                "humidity": "00",
                "pressure": "00",
                "windspeed": "00",
                "winddirection": "00",
            },     
        }
        return cities.get(name)

    class _sandiego(Resource): 
        def get(self):
            cities = WeatherAPI.get_weather("Sandiego")
            if cities:
                return jsonify(cities) 
            return {"Data not found"}, 404
    class _tokyo(Resource): 
        def get(self):
            cities = WeatherAPI.get_weather("Tokyo")
            if cities:
                return jsonify(cities) 
            return {"Data not found"}, 404 
    class _mumbai(Resource): 
        def get(self):
            cities = WeatherAPI.get_weather("Mumbai")
            if cities:
                return jsonify(cities) 
            return {"Data not found"}, 404 
    class _cairo(Resource): 
        def get(self):
            cities = WeatherAPI.get_weather("Cairo")
            if cities:
                return jsonify(cities) 
            return {"Data not found"}, 404 
    class _lagos(Resource): 
        def get(self):
            cities = WeatherAPI.get_weather("Lagos")
            if cities:
                return jsonify(cities) 
            return {"Data not found"}, 404 
    class _london(Resource): 
        def get(self):
            cities = WeatherAPI.get_weather("London")
            if cities:
                return jsonify(cities) 
            return {"Data not found"}, 404 
    class _paris(Resource):
        def get(self):
            cities = WeatherAPI.get_weather("Paris")
            if cities:
                return jsonify(cities) 
            return {"Data not found"}, 404 
    class _newyorkcity(Resource): 
        def get(self):
            cities = WeatherAPI.get_weather("Newyorkcity")
            if cities:
                return jsonify(cities) 
            return {"Data not found"}, 404 
    class _mexicocity(Resource): 
        def get(self):
            cities = WeatherAPI.get_weather("Mexicocity")
            if cities:
                return jsonify(cities) 
            return {"Data not found"}, 404 
    class _saopaulo(Resource): 
        def get(self):
            cities = WeatherAPI.get_weather("Saopualo")
            if cities:
                return jsonify(cities) 
            return {"Data not found"}, 404 
    class _buenosaires(Resource): 
        def get(self):
            cities = WeatherAPI.get_weather("Buenosaires")
            if cities:
                return jsonify(cities) 
            return {"Data not found"}, 404 

    # building RESTapi endpoint
api.add_resource(WeatherAPI._sandiego, '/cities/sandiego')
api.add_resource(WeatherAPI._tokyo, '/cities/tokyo')
api.add_resource(WeatherAPI._mumbai, '/cities/mumbai')
api.add_resource(WeatherAPI._cairo, '/cities/cairo')
api.add_resource(WeatherAPI._lagos, '/cities/lagos')
api.add_resource(WeatherAPI._london, '/cities/london')
api.add_resource(WeatherAPI._paris, '/cities/paris')
api.add_resource(WeatherAPI._newyorkcity, '/cities/newyorkcity')
api.add_resource(WeatherAPI._mexicocity, '/cities/mexicocity')
api.add_resource(WeatherAPI._saopaulo, '/cities/saopaulo')
api.add_resource(WeatherAPI._buenosaires, '/cities/buenosaires')

# Instantiate the StudentAPI to register the endpoints
weather_api_instance = WeatherAPI()
