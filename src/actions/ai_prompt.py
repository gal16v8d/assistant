"""Allow to generate content using Google GenAI API."""

from io import BytesIO
import os

from google import genai
from google.genai import types
from PIL import Image


client = genai.Client(api_key=os.getenv("G_API_KEY"))


def get_ai_text_response(prompt: str) -> str:
    """Generate a response from the AI model."""
    response = client.models.generate_content(
        model="gemini-2.0-flash",
        contents=prompt,
    )
    return response.text


def get_ai_image_response(prompt: str, title: str) -> str:
    """Generate an image from the AI model. Use this when:
    - You need contextually relevant images that leverage world knowledge and reasoning.
    - Seamlessly blending text and images is important.
    - You want accurate visuals embedded within long text sequences.
    - You want to edit images conversationally while maintaining context.
    """
    response = client.models.generate_content(
        model="gemini-2.0-flash-preview-image-generation",
        contents=prompt,
        config=types.GenerateContentConfig(response_modalities=["TEXT", "IMAGE"]),
    )

    text_response = "Error generating image."

    for part in response.candidates[0].content.parts:
        if part.text is not None:
            text_response = part.text
        elif part.inline_data is not None:
            image = Image.open(BytesIO((part.inline_data.data)))
            image.save(f"{title}.png")
            image.show()

    return (
        f"Generated image is saved with name '{title}.png' and response {text_response}"
    )


def get_ai_image_response_v3(prompt: str, title: str) -> str:
    """Generate an image from the AI model. Use this when:
    - Image quality, photorealism, artistic detail, or specific styles (e.g., impressionism, anime) are top priorities.
    - Performing specialized editing tasks like product background updates or image upscaling.
    - Infusing branding, style, or generating logos and product designs.
    - Multiple images are needed from a single prompt.
    - This is only for billed users
    """
    response = client.models.generate_images(
        model="imagen-3.0-generate-002",
        prompt=prompt,
        config=types.GenerateImagesConfig(
            number_of_images=2,
        ),
    )

    img_count = 0
    for generated_image in response.generated_images:
        image = Image.open(BytesIO(generated_image.image.image_bytes))
        image.save(f"{title}{img_count}.png")
        image.show()
        img_count += 1

    return f"Generated images are saved in assistant directory with pattern '{title}-#.png'."
