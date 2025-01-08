from flask import Flask, request, jsonify
import json
import os

app = Flask(__name__)

# Path to store quiz results
RESULTS_FILE = "quiz_results.json"

# Helper function to save quiz data
def save_results(data):
    if not os.path.exists(RESULTS_FILE):
        with open(RESULTS_FILE, 'w') as file:
            json.dump([], file)  # Initialize empty list in JSON file
    
    with open(RESULTS_FILE, 'r+') as file:
        results = json.load(file)  # Load existing results
        results.append(data)  # Add new result
        file.seek(0)  # Reset file pointer to beginning
        json.dump(results, file, indent=4)  # Save back to file


# Root route (just for testing)
@app.route('/')
def index():
    return "Welcome to the Quiz App! Use /submit-quiz to submit quiz data and /get-results to get all results."

# Endpoint to save quiz results (POST request)
@app.route('/submit-quiz', methods=['POST'])
def submit_quiz():
    try:
        quiz_data = request.json  # Data sent from frontend
        
        # Ensure data is present
        if not quiz_data:
            return jsonify({"error": "No data received"}), 400
        
        # Example validation (ensure required fields exist)
        required_fields = ['username', 'climate', 'activities', 'budget']
        for field in required_fields:
            if field not in quiz_data:
                return jsonify({"error": f"Missing field: {field}"}), 400
        
        # Save the quiz result
        save_results(quiz_data)
        
        return jsonify({"message": "Quiz results saved successfully!"}), 200

    except Exception as e:
        return jsonify({"error": str(e)}), 500


# Endpoint to view all stored results (GET request)
@app.route('/get-results', methods=['GET'])
def get_results():
    try:
        # Check if results file exists
        if not os.path.exists(RESULTS_FILE):
            return jsonify({"message": "No results found."}), 200  # Return empty message if no data exists
        
        # Read the existing results from the file
        with open(RESULTS_FILE, 'r') as file:
            results = json.load(file)
        
        # Return the stored results
        return jsonify(results), 200

    except Exception as e:
        return jsonify({"error": str(e)}), 500


if __name__ == "__main__":
    app.run(debug=True)

