# chatbot_api.py
from flask import Blueprint, request, jsonify
from model.chatbot import get_chatbot_response

# This blueprint is mounted at /api/chatbot
chatbot_api = Blueprint('chatbot_api', __name__, url_prefix='/api/chatbot')
chatbot_api.strict_slashes = False  # Avoid 308 if user calls /api/chatbot/ with a slash

@chatbot_api.route('', methods=['POST'])  # route is /api/chatbot (no slash)
def chatbot_endpoint():
    data = request.get_json(force=True)
    if not data or 'message' not in data:
        return jsonify({'error': "Missing 'message' field"}), 400

    user_message = data['message']
    try:
        reply = get_chatbot_response(user_message)
        return jsonify({'reply': reply}), 200
    except Exception as e:
        return jsonify({'error': str(e)}), 500
