# Whisper 

- Whisper is a trained open source neural network that approaches human level robustness and accuarcy on English speech recognition/
- OpenAI API provides two endpoints:
    - transcriptions
    - translations

## Generate transcription

```python
# Reading the file
with open("./audio/Speech.mp3", "rb") as audio_file:
    # Generating transcript
    transcript = client.audio.transcriptions.create(
        model="whisper-1",
        # Audio file
        file=audio_file,
        # Defaults to English
        language="en",
    )
    # Accessing the transcript
    print(f"Transcription: {transcript.text}")
    # Close the file
    audio_file.close()
```

The default language is English. Supported languages are:
- `en` - English
- `hi` - Hindi
- `es` - Spanish
- `fr` - French
- `de` - German
- `zh` - Chinese
- `ar` - Arabic
- `ja` - Japanese

> **NOTE**: The maximum file size is 25MB, and the supported files are `MP3, MPEG, MP4, M4A, WAV`.

## Generate translation

```python
with open("./audio/Speech.mp3", "rb") as audio_file:
    transcript = client.audio.translations.create(model="whisper-1", file=audio_file)
    print(f"Transcription: {transcript.text}")
    audio_file.close()
```

Generates an English translated from a file. The file size and format 

> **NOTE**: Whisper API only translates audio into English, no matter the source language.

## Text to speech

```python
response = client.audio.speech.create(
    # Provides lowest latency but lower quality as compared to "tts-1-hd"
    model="tts-1",
    # Select a voice that suits our tone and audience (ash, onyx, alloy)
    voice="alloy",
    # Text we want to turn into audio
    input="This is an open book, filled with chapters yet unwritten, awaiting the brilliance of our minds to fill it.",
)

# Supported output formats are: MP3, OPUS, AAC, FLAC
with open("./audio/output/Speech.mp3", "wb") as audio_file:
    audio_file.write(response.content)
```