## Dall-E

- Dall-E is a nuerla network and a version of GPT-3, that uses a dataset of text-images pairs.
- It is a transformer language model.

## Generating new images

Converts text prompt to images.

```python
response = client.images.generate(
    model="dall-e-3",  
    prompt="A realistic golden retriever sitting in a park",
    size="1024x1024",
    style="vivid",
    quality="standard",
    n=1,
)
```

- `model`
    - Specifies which image generation model to use.
    - Example: "dall-e-3".
    - ⚠️ **NOTE**: Violent prompts are not allowed.
    - ✅ **TIP**: You can list available models with client.models.list().
- `prompt`
    - A text description of the image you want generated.
    - This is the most important input — it drives the entire output.
- `size`:
    - Defines the resolution of the output image.
    - Format: "WIDTHxHEIGHT" (e.g., "1024x1024").
    - Higher resolutions may increase cost and time.

- `style`:
    -   Controls the visual tone or rendering type of the image.
    - Options:
        - "vivid": More saturated, stylized, and sharper.
        - "natural": Mimics real camera photos — more lifelike and subtle.
        - Default is "vivid".
- `quality`:
    - Determines the quality tier of the generated image.
    - Options:
        - "standard": Regular quality (lower cost).
        - "hd": High-definition, better detail (higher cost).
`n`:
    - Number of images to generate in the request.
    - ⚠️ **NOTE**:
        - **dall-e-2** supports multiple images per request.
        - **dall-e-3** can only generate 1 image per request - if you want more, you must call this method multiple times.


## Generating image variation

```python
# Read an existing image
image = open("./image/DP.jpg", "rb")

# Generating variations of an image
response = client.images.create_variation(
    image=image,
    size="1024x1024",
    n=1,
)
```

> NOTE: There is no "text" or "prompt" parameter.

## Editing or masking image

```python
image = open("./image/DP.png", "rb")
mask = open("./image/Moon.png", "rb")

response = client.images.edit(
    image=image, mask=mask, prompt="Put the moon in the background of the DP"
)

print(f"Edited image url: {response.data[0].url}")
```

> NOTE: jpeg/jpg image format is not supported.