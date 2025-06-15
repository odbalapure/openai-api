import os
from openai import OpenAI

client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))
response = client.audio.speech.create(
    # Provides lowest latency but lower quality as compared to "tts-1-hd"
    model="tts-1",
    # Select a voice that suits our tone and audience
    voice="alloy",
    # Text we want to turn into audio
    input="This is an open book, filled with chapters yet unwritten, awaiting the brilliance of our minds to fill it.",
)

# Supported output formats are: MP3, OPUS, AAC, FLAC
with open("./audio/output/Speech.mp3", "wb") as audio_file:
    audio_file.write(response.content)
