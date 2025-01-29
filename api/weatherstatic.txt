from flask import Flask, jsonify
from flask_cors import CORS, cross_origin
from flask import Blueprint, jsonify
from flask_restful import Api, Resource
import json
import os


weather_api = Blueprint('weather_api', __name__,)
CORS(weather_api) 
api = Api(weather_api)
# ================== Static DATA ==================
weather_data = {
    "Sandiego": {
        "name": "San Diego",
        "temperature": "20°C",
        "feelslike": "19°C",
        "humidity": "18%",
        "pressure": "1021 hPa",
        "windspeed": "3.6 m/s",
        "winddirection": "300°",
    },
    "Tokyo": {
        "name": "Tokyo",
        "temperature": "5°C",
        "feelslike": "4°C",
        "humidity": "55%",
        "pressure": "1020 hPa",
        "windspeed": " 1.54 m/s",
        "winddirection": "200°",
    },
    "Mumbai": {
        "name": "Mumbai",
        "temperature": "24°C",
        "feelslike": "24°C",
        "humidity": "60%",
        "pressure": "1011 hPa",
        "windspeed": "1.37 m/s",
        "winddirection": "100°",
    },
    "Cairo": {
        "name": "Cairo",
        "temperature": "14°C",
        "feelslike": "14°C",
        "humidity": "72%",
        "pressure": "1020 hPa",
        "windspeed": "0.51 m/s",
        "winddirection": "90°",
    },
    "Lagos": {
        "name": "Lagos",
        "temperature": "24°C",
        "feelslike": "25°C",
        "humidity": "84%",
        "pressure": "1009 hPa",
        "windspeed": "1.72 m/s",
        "winddirection": "233°",
    },
    "London": {
        "name": "London",
        "temperature": "4°C",
        "feelslike": "1°C",
        "humidity": "86%",
        "pressure": "1037 hPa",
        "windspeed": "2.68 m/s",
        "winddirection": "259°",
    },
    "Paris": {
        "name": "Paris",
        "temperature": "-1°C",
        "feelslike": "-4°C",
        "humidity": "85%",
        "pressure": "1039 hPa",
        "windspeed": "2.06 m/s",
        "winddirection": "350°",
    },
    "Newyorkcity": {
        "name": "New York City",
        "temperature": "5°C",
        "feelslike": "1°C",
        "humidity": "53%",
        "pressure": "1013 hPa",
        "windspeed": "5.14 m/s",
        "winddirection": "260°",
    },
    "Mexicocity": {
        "name": "Mexico City",
        "temperature": "23°C",
        "feelslike": "22°C",
        "humidity": "29%",
        "pressure": "1012 hPa",
        "windspeed": "1.34 m/s",
        "winddirection": "70°",
    },
    "Saopaulo": {
        "name": "Sao Paulo",
        "temperature": "19°C",
        "feelslike": "19°C",
        "humidity": "79%",
        "pressure": "1012 hPa",
        "windspeed": "6.17 m/s",
        "winddirection": "160°",
    },
    "Buenosaires": {
        "name": "Buenos Aires",
        "temperature": "27°C",
        "feelslike": "28°C",
        "humidity": "58%",
        "pressure": "1009 hPa",
        "windspeed": "8.05 m/s",
        "winddirection": "80°",
    },
}


@weather_api.route ('/check', methods=['GET'])
@cross_origin()
def home():
    return "working"

@weather_api.route("/weather", methods=["GET"])
def get_weather():
    return jsonify(weather_data)

if __name__ == "__main__":
    weather_api.run(debug=True, port=8887)
