from google import genai
from PIL import Image
import io
import os

# Load API key from environment variable (never hard-code it)
gemini_api_key = os.getenv("GOOGLE_API_KEY")
if not gemini_api_key:
    raise RuntimeError("Missing GOOGLE_API_KEY environment variable")

gemini_client = genai.Client(api_key=gemini_api_key)

def get_llm_response(image_data: bytes) -> str:
    image = Image.open(io.BytesIO(image_data))
    # implement the call to the Gemini API here
    # docs: https://ai.google.dev/gemini-api/docs/text-generation
    response = gemini_client.models.generate_content(
        model="gemini-2.5-flash",
        contents = [
            image, "Coming up with a caption to describe the image."
        ],
    )
    return response.text