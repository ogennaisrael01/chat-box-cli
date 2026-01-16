from google import genai
import os
import logging
from helpers import retry_on_failure

logger = logging.getLogger(__name__)

GOOGLE_API_SECRET = os.getenv("GOOGLE_API_SECRET")

@retry_on_failure
def chats_ai(message: str, history: list):
    if GOOGLE_API_SECRET is None:
        raise ValueError("Google api key cannot be empty")
    secret_key = GOOGLE_API_SECRET.strip()
    client = genai.Client(api_key=secret_key)
    try:
        chats = client.chats.create(model="gemini-3-flash-preview", history=history)
        response = chats.send_message(message=message)
    except Exception:
        logger.exception(f"Failed to generate chat for message {message}", exc_info=True)
        raise
    return response.text