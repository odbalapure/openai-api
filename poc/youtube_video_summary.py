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


def get_summar(audio_file):
    with open(audio_file, "rb") as f:
        transcript = client.audio.transcriptions.create(model="whisper-1", file=f)

        system_prompt = "You are to summarize youtube video transcripts"
        prompt = f"""Create a summary of the following text.
        Text: {transcript.text}"""

        summary_respons = client.chat.completions.create(
            model="gpt-3.5-turbo",
            messages=[
                {"role": "system", "content": system_prompt},
                {"role": "user", "content": prompt},
            ],
            temperature=1,
        )

        return summary_respons.choices[0].message.content


audio_file = download_audio("https://www.youtube.com/watch?v=RI3JCq9-bbM")
summary = get_summar(audio_file)
print(f"Video summary {summary}")
