import os
from openai import OpenAI

client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

# Read an existing image
image = open("./image/DP.jpg", "rb")

# Generating variations of an image
# NOTE: There is no text or prompt parameter
response = client.images.create_variation(
    image=image,
    size="1024x1024",
    n=1,
)

image_url = response.data[0].url
print(f"Generated image url: {image_url}")
