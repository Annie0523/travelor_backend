from flask import Blueprint, jsonify
from flask_restful import Api, Resource
from flask_cors import CORS

student_api = Blueprint('student_api', __name__, url_prefix='/api')
CORS(student_api) 
api = Api(student_api)

class StudentAPI:        
    class _Johan(Resource): 
        def get(self):
           # implement the get method 
           data =  {
                "FirstName": "Johan",
                "LastName": "Mascarenhas",
                "DOB": "Jnauary 8",
                "Residence": "San Diego",
                "Email": "johanmascarenhas.jm@gmail.com",
                "Favorite_song": "Thick of it by KSI",
                "Hobbies": ["Gymnasium", "swimming", "Videogames"]
            }
           return jsonify(data)
    
    class _Luke(Resource): 
        def get(self):
           # implement the get method 
           data =  {
                "FirstName": "Luke",
                "LastName": "Starr",
                "DOB": "November 2",
                "Residence": "San Diego",
                "Email": "lstarr1100@gmail.com",
                "Favorite_Videogame": "Elden Ring",
                "Hobbies": ["Videogames", "Guitar", "Musicproduction"]
            }
           return jsonify(data)
       
    class _Anyi(Resource): 
        def get(self):
           # implement the get method 
           data =  {
                "FirstName": "Anyi",
                "LastName": "Wang",
                "DOB": "May 23",
                "Residence": "San Diego",
                "Email": "anyiw887@gmail.com",
                "Favorite_Videogame": "Splatoon",
                "Hobbies": ["Baking", "Chinese Zither", "Badminton"]
            }
           return jsonify(data)
    
    class _Collin(Resource): 
        def get(self):
           # implement the get method 
           data =  {
                "FirstName": "Collin",
                "LastName": "Ge",
                "DOB": "March 26",
                "Residence": "San Diego",
                "Email": "collinxiaoheizi@gmail.com",
                "Favorite_Videogame": "Honkai starrail",
                "Hobbies": ["Cooking", "fishing", "crafting stuff"]
            }
           return jsonify(data)
       
    class _Michelle(Resource): 
        def get(self):
           data = {
               "FirstName": "Michelle",
                "LastName": "Kuruvilla",
                "DOB": "July 7",
                "Residence": "San Diego",
                "Email": "kuruvillamichelle@gmail.com",
                "Favorite_Videogame": "Agario",
                "Hobbies": ["Eating", "Listeningtomusic", "Reading"]
           }
           return jsonify(data)

    # building RESTapi endpoint
    api.add_resource(_Johan, '/student/johan')          
    api.add_resource(_Luke, '/student/luke')
    api.add_resource(_Anyi, '/student/anyi')
    api.add_resource(_Collin, '/student/collin')
    api.add_resource(_Michelle, '/student/michelle')