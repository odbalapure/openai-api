import os
from openai import OpenAI

client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

with open("./audio/sample/Speech.mp3", "rb") as audio_file:
    transcript = client.audio.transcriptions.create(
        # Model
        model="whisper-1",
        # Audio file
        file=audio_file,
        # Defaults to English
        # See README for supported language list
        language="hi",
    )
    print(f"Transcription: {transcript.text}")
    audio_file.close()
