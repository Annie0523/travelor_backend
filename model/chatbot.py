# chatbot.py
import os
import logging

# Example import for “genai” or any relevant library:
from google import genai  # Or your actual import for the Gemini API

def get_chatbot_response(user_message):
    """
    Sends 'user_message' to your Gemini/generative AI client
    and returns the textual reply.
    """
    gemini_api_key = os.getenv('GEMINI_API_KEY')
    if not gemini_api_key:
        logging.error("GEMINI_API_KEY is not set in environment variables.")
        raise Exception("GEMINI_API_KEY is not set in your environment.")
    
    # Create the Gemini client using your API key
    try:
        client = genai.Client(api_key=gemini_api_key)
    except Exception as e:
        logging.error("Could not initialize the Gemini client: %s", str(e))
        raise Exception("Could not initialize Gemini API client") from e
    
    # Now call the relevant function to generate content
    try:
        response = client.models.generate_content(
            model="gemini-2.0-flash",  # or whichever model you need
            contents=user_message
        )
        # The Gemini library typically returns an object with a .text or .contents
        return response.text
    except Exception as e:
        logging.error("Error calling Gemini API: %s", str(e))
        raise Exception("Error calling Gemini API: " + str(e))
