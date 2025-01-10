from flask import Flask, jsonify
import requests

app = Flask(__name__)

# Sample data (you can replace this with real backend data)
destinations = [
    {"name": "Maldives"},
    {"name": "Swiss Alps"},
    {"name": "Kyoto, Japan"},
    {"name": "Hawaii"},
    {"name": "Bangkok, Thailand"}
]

# Route to get data from backend (existing)
@app.route('/', methods=['GET'])
def get_data():
    return jsonify(destinations)

# Route to execute Python script logic and fetch data
@app.route('/run-script', methods=['GET'])
def run_script():
    try:
        # This could be a request to another backend API or your own logic
        response = requests.get('http://127.0.0.1:5001')  # Adjust based on your backend setup

        # If successful, return the parsed JSON data
        if response.status_code == 200:
            data = response.json()
            result = [f"Data from backend: {city['name']}" for city in data]
            return jsonify({"status": "success", "data": result})
        else:
            return jsonify({"status": "failed", "message": f"Failed to fetch data. HTTP Status Code: {response.status_code}"})
    except requests.exceptions.RequestException as e:
        return jsonify({"status": "error", "message": f"An error occurred: {e}"})

if __name__ == '__main__':
    app.run(debug=True, port=5001)  # You can change the port here if necessary

import requests

def fetch_data_from_backend():
    try:
        # Make a GET request to the Flask server
        response = requests.get('http://127.0.0.1:5001')

        # Check if the response is successful
        if response.status_code == 200:
            data = response.json()  # Parse the JSON response
            print("Data from backend:")
            for city in data:
                print(f"- {city['name']}")  # Print the city name from the list
        else:
            print(f"Failed to fetch data. HTTP Status Code: {response.status_code}")

    except requests.exceptions.RequestException as e:
        print(f"An error occurred: {e}")



