"""Allow to generate content using Google GenAI API."""

from io import BytesIO
import os

from google import genai
from PIL import Image

client = genai.Client(api_key=os.getenv("G_API_KEY"))


def get_ai_text_response(prompt: str) -> str:
    """Generate a response from the AI model."""
    try:
        response = client.models.generate_content(
            model="gemini-3-flash-preview",
            contents=prompt,
        )
        return response.text
    except Exception as e:
        return f"Error processing response: {str(e)}"


def get_ai_image_response(prompt: str, title: str) -> str:
    """Generate an image from the AI model. Use this when:
    - You need contextually relevant images that leverage world knowledge and reasoning.
    - Seamlessly blending text and images is important.
    - You want accurate visuals embedded within long text sequences.
    - You want to edit images conversationally while maintaining context.
    """
    try:
        response = client.models.generate_content(
            model="gemini-3.1-flash-image-preview",
            contents=prompt,
        )

        for part in response.candidates[0].content.parts:
            if part.inline_data:
                image_bytes = part.inline_data.data
                image = Image.open(BytesIO(image_bytes))
                image.save(f"{title}.png")
                image.show()
                return f"Generated image is saved with name '{title}.png'"

        return "Model does not return an image"
    except Exception as e:
        return f"Error processing response: {str(e)}"
