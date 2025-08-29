from google import genai
from PIL import Image
import io
import os

gemini_api_key = 'AIzaSyB8ngAGTlAd1UNmLb_Ln4K_wN901rfRDAk'
client = genai.Client(api_key=gemini_api_key)

def get_llm_response(image_data: bytes) -> str:
    image = Image.open(io.BytesIO(image_data))
    # implement the call to the Gemini API here
    # docs: https://ai.google.dev/gemini-api/docs/text-generation

    response = client.models.generate_content(
        model="gemini-2.5-flash",
        contents=[image, "Tell me about this instrument"]
    )

    return response.text