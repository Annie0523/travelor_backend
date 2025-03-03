import os
import logging
from google import genai  # Import the Gemini SDK

def get_chatbot_response(user_message):
    gemini_api_key = os.getenv('GEMINI_API_KEY')
    if not gemini_api_key:
        logging.error("GEMINI_API_KEY is not set in your environment.")
        raise Exception("GEMINI_API_KEY is not set in your environment.")
    
    # Initialize the Gemini client using your API key
    client = genai.Client(api_key=gemini_api_key)
    
    # Use the generate_content method as per the Gemini quickstart instructions.
    try:
        response = client.models.generate_content(
            model="gemini-2.0-flash",  # Use the model identifier from the guide
            contents=user_message
        )
        # Assuming the SDK returns an object with a .text attribute containing the reply.
        return response.text
    except Exception as e:
        logging.error("Error calling Gemini API: " + str(e))
        raise Exception("Error calling Gemini API: " + str(e))
