################################
# ACCESSING API_KEY
################################

# import openai
# import os
# import getpass

# Getting the API key via environment variable
# openai.api_key = os.environ["OPENAI_API_KEY"]
# print(openai.api_key)

# Getting the API key via terminal
# key = getpass.getpass("Enter you API key: ")
# openai.api_key = key
# print(key)

# Getting the API key from a file
# key = open("key.txt").read().strip("\n")
# print(key)


################################
# OPENAI API
################################

import os
from openai import OpenAI

print(os.getenv("OPENAI_API_KEY"))


client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

response = client.chat.completions.create(
    model="gpt-3.5-turbo-1106",
    messages=[
        # sets the tone of the assitant
        {"role": "system", "content": "You are helpful assistant!"},
        # consits the actual prompt
        {"role": "user", "content": "What is the theory of relativity"},
    ],
    # gives 2 answers
    n=2,
)

# Accessing the response
print(f"Model response is: {response.choices[0].message.content}")
