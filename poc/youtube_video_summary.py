import yt_dlp
import os
import re
from openai import OpenAI

client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))


def sanitize_filename(title: str) -> str:
    title = title.lower().strip()
    title = re.sub(r"\s+", "_", title)
    title = re.sub(r"[^\w\-\.]+", "", title)
    return title


def download_audio(url: str, output_dir: str = "audio/download") -> str:
    os.makedirs(output_dir, exist_ok=True)

    # Step 1: Get video info without downloading
    with yt_dlp.YoutubeDL({}) as ydl:
        info = ydl.extract_info(url, download=False)
        raw_title = info["title"]
        safe_title = raw_title.lower().strip()
        safe_title = re.sub(r"\s+", "_", safe_title)
        safe_title = re.sub(r"[^\w\-\.]+", "", safe_title)

    # Step 2: Define output template using sanitized title
    sanitized_outtmpl = os.path.join(output_dir, f"{safe_title}.%(ext)s")

    # Step 3: Download with audio extraction
    ydl_opts = {
        "format": "bestaudio/best",
        "outtmpl": sanitized_outtmpl,
        "postprocessors": [
            {
                "key": "FFmpegExtractAudio",
                "preferredcodec": "mp3",
                "preferredquality": "192",
            }
        ],
    }

    with yt_dlp.YoutubeDL(ydl_opts) as ydl:
        info = ydl.extract_info(url, download=True)

    return os.path.join(output_dir, f"{safe_title}.mp3")


def get_translation(audio_file):
    with open(audio_file, "rb") as f:
        transcript = client.audio.translations.create(model="whisper-1", file=f)
        print(f"Transcription for audio: {transcript.text}")


audio_file = download_audio("https://www.youtube.com/watch?v=RI3JCq9-bbM")
get_translation(audio_file)
