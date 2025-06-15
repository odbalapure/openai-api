import os
from openai import OpenAI

client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

image = open("./image/DP.png", "rb")
mask = open("./image/Moon.png", "rb")

response = client.images.edit(
    image=image, mask=mask, prompt="Put the moon in the background of the DP"
)

# NOTE: jpeg/jpg is unsupported
print(f"Edited image url: {response.data[0].url}")
