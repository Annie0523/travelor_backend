# api/chatbot.py

from flask import Blueprint, request, jsonify
from flask_cors import CORS
import os
import logging

# If you are using the "google.genai" library:
from google import genai

chatbot_api = Blueprint('chatbot_api', __name__, url_prefix='/api')
CORS(chatbot_api)

@chatbot_api.route('/chatbot', methods=['POST'])
def chatbot_endpoint():
    """
    POST /api/chatbot
    Expects JSON: { "message": "<user input>" }
    Returns JSON: { "reply": "<AI response>" } or { "error": "<error message>" }
    """
    data = request.get_json(force=True)
    if not data or 'message' not in data:
        return jsonify({'error': "Missing 'message' field"}), 400

    user_message = data['message']

    # Make sure GEMINI_API_KEY is set in environment
    gemini_api_key = os.getenv('GEMINI_API_KEY')
    if not gemini_api_key:
        logging.error("GEMINI_API_KEY is not set in environment.")
        return jsonify({"error": "GEMINI_API_KEY is not set on this server."}), 500

    try:
        # Create Gemini client and call the model
        client = genai.Client(api_key=gemini_api_key)
        response = client.models.generate_content(
            model="gemini-2.0-flash",   # or whichever model you use
            contents=user_message
        )
        # Typically the .text attribute has the response
        ai_reply = getattr(response, 'text', None)
        if not ai_reply:
            return jsonify({'error': 'Gemini API returned no .text field'}), 500
        return jsonify({'reply': ai_reply}), 200

    except Exception as e:
        logging.error("Error calling Gemini API: %s", str(e))
        return jsonify({"error": str(e)}), 500
