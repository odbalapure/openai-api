import base64
import os
from openai import OpenAI


def encode_image(image_path):
    """
    Encode an image to base64 string
    :param image_path: Path of the image
    :return: base64 image string
    """
    with open(image_path, "rb") as image_file:
        image_binary_data = image_file.read()
        return base64.b64encode(image_binary_data).decode("utf-8")


base_image = encode_image("./image/DP.jpg")
system_message = "You scan avatar DPs"
prompt = "Describe this avatar"

client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

# Using base64 images as input
# response = client.chat.completions.create(
#     model="gpt-4o",
#     messages=[
#         {"role": "system", "content": system_message},
#         {
#             "role": "user",
#             "content": [
#                 {"type": "text", "text": prompt},
#                 {
#                     "type": "image_url",
#                     "image_url": {"url": f"data:image/jpg;base64;{base_image}"},
#                 },
#             ],
#         },
#     ],
#     temperature=0.0,
# )

image_url = "https://www.unsplash.com/food.png"

# Using images urls as input
response = client.chat.completions.create(
    model="gpt-4o",
    messages=[
        {"role": "system", "content": system_message},
        {
            "role": "user",
            "content": [
                {"type": "text", "text": prompt},
                {
                    "type": "image_url",
                    "image_url": {"url": image_url},
                },
            ],
        },
    ],
    temperature=0.0,
)
