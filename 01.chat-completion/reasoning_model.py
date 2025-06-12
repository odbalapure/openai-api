import os
from openai import OpenAI

client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))


def get_response(prompt):
    """
    Return a prompt response
    :param prompt: str
    :return: Chat response
    """
    response = client.chat.completions.create(
        model="o3-mini",
        # defaults to medium
        reasoning_effort="medium",
        # don't let the model generate > 10k tokens
        max_completion_tokens=100000,
        messages=[
            {"role": "system", "content": "You are helpful assistant!"},
            {"role": "user", "content": prompt},
        ],
    )

    return response.choices[0].message.content


get_response("Write about AI revolution in 50 words")
