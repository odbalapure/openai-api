import os
from openai import OpenAI

client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

with open("./audio/sample/Speech.mp3", "rb") as audio_file:
    # Translate the audio file to an English transcript
    translation = client.audio.translations.create(model="whisper-1", file=audio_file)
    print(f"Translation: {translation.text}")
    audio_file.close()
