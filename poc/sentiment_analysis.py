import os
from openai import OpenAI

client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))


def gpt_classify_human_emotions(user_prompt, emotions):
    system_prompt = f"""
    You are an emotionally intelligent assistant
    Classify the sentiment of the user's text with ONLY ONE OF THE FOLLOWING EMOTIONS {emotions}:
    After classifying the text, response with the emption ONLY.
    """
    response = client.chat.completions.create(
        model="gpt-3.5-turbo",
        messages=[
            {"role": "system", "content": system_prompt},
            {"role": "user", "content": user_prompt},
        ],
        # Response will only be one word
        max_tokens=20,
        # Want it to be determinstic
        temperature=0,
    )

    return response.choices[0].message.content or "N/A"


emotions = "positive, negative, angry, sad, tried"
prompt = "AI will take over the world"
print(gpt_classify_human_emotions(prompt, emotions))
