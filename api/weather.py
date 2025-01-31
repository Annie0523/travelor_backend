from flask import Blueprint, request
from flask_restful import Api, Resource
from flask_cors import CORS
from model.weather import db, Weather, initWeather

weather_api = Blueprint('weather_api', __name__, url_prefix='/api')
api = Api(weather_api)


class WeatherAPI(Resource):
    """
    A RESTful API for handling Weather resources.
    Supports GET (all), POST (create), and DELETE (by id).
    """

    def get(self):
        """
        Retrieve all Weather records from the database.
        """
        try:
            weathers = Weather.query.all()
            # Return a list of dicts; Flask-RESTful will handle JSON conversion
            return [weather.read() for weather in weathers], 200
        except Exception as e:
            return {"error": str(e)}, 500

    def post(self):
        """
        Create a new Weather entry from JSON payload.
        Expected JSON fields:
          name, temperature, feelslike, humidity,
          pressure, windspeed, winddirection
        """
        try:
            data = request.get_json()
            new_weather = Weather(
                name=data['name'],
                temperature=data['temperature'],
                feelslike=data['feelslike'],
                humidity=data['humidity'],
                pressure=data['pressure'],
                windspeed=data['windspeed'],
                winddirection=data['winddirection']
            )
            new_weather.create()
            return new_weather.read(), 201
        except Exception as e:
            return {"error": str(e)}, 400

    def delete(self):
        """
        Delete a Weather entry by 'id'.
        Expected JSON field: 'id'.
        """
        try:
            data = request.get_json()
            weather_id = data.get('id')
            if weather_id is None:
                return {"error": "Missing 'id' in request"}, 400

            weather = Weather.query.get(weather_id)
            if weather:
                weather.delete()
                return {"message": f"Successfully deleted Weather with ID {weather_id}"}, 200
            else:
                return {"error": f"Weather with ID {weather_id} not found"}, 404
        except Exception as e:
            return {"error": str(e)}, 400


@weather_api.route('/weathers/init', methods=['POST'])
def weather_init():
    """
    OPTIONAL endpoint:
    Re-create the 'weathers' table (if needed) and seed with default data.
    Call via POST /api/weathers/init
    """
    try:
        initWeather()
        return {"message": "Weather table initialized with default data"}, 201
    except Exception as e:
        return {"error": str(e)}, 500


api.add_resource(WeatherAPI, '/weathers')