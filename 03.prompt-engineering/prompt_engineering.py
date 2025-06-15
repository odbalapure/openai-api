import os
from openai import OpenAI

client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))


def get_response(
    user_prompt,
    system_role="You are a helpful assistant",
    model="gpt-3.5-turbo",
    temperature=1,
):
    """
    Returns a prompt response
    :param user_prompt: str
    :param system_role: str
    :param model: str
    :param temperature: int
    :return: Prompt response
    """
    messages = (
        [
            {"role": "system", "content": system_role},
            {"role": "user", "content": user_prompt},
        ],
    )
    response = client.chat.completions.create(
        model=model,
        reasoning_effort="medium",
        temperature=temperature,
        messages=messages,
    )

    return response.choices[0].message.content


# use descriptive text
# good prompt
text = """
some huge text
"""

# use delimiters
prompt = f"""
Summarize the text below in at most 50 words
Text: ```{text}```
"""

system_role = "You are a linux sys admin."
response = get_response(user_prompt=prompt, system_role=system_role)
print(f"Length of the response: {len(response.split())}")
