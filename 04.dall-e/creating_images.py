import os
from openai import OpenAI

client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

# Generating an image
response = client.images.generate(
    model="dall-e-3",
    # violent prompts are not allowed for image generation
    prompt="A realistic golden retriever sitting in a park",
    size="1024x1024",
    # defaults to vivid
    # vivid: saturated, stylized and more sharper images
    # natural: more like a real camera capture
    style="vivid",
    # generating "hd" images cost more
    quality="standard",
    # dall-e-2 can generate multiple images at once
    # dall-e-3 requires multiple requests for generating "> 1" image
    n=1,
)

image_url = response.data[0].url
print(f"Generated image url: {image_url}")
