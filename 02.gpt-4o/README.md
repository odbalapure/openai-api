## GPT-4o

- It is large multimodal model that accepts input, both text and images and generates text as output.
- It can work on documents with text and photos, diagrams of screenshots.

### Using base64 image as an input

This is how it takes input including the text and image

```python
system_message = "You are maths professor"
prompt = "Find the area of the triangle in the image"

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
                    "image_url": {"url": f"data:image/jpg;base64;{base_image}"},
                },
            ],
        },
    ],
    temperature=0.0,
)
```

###  Using image url as an input

To use image urls, just put the url instead of the base64 string output.

```python
image_url = "https://www.unsplash.com/food.png"

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
```