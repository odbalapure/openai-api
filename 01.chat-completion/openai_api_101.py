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
        # contains the actual prompt
        {"role": "user", "content": "What is the theory of relativity"},
    ],
    # gives 2 answers
    # n=2,
    # controls how random the model is; "temperature" defaults to "1"
    temperature=0.2,
    # seed helps in locking the randomness
    seed=1234,
    # will get us top 10% most probable tokens
    # NOTE: Better not to use it along side "temperature"
    top_p=0.1,
    # limits the max no. of tokens to be generated in chat completion
    max_tokens=1000,
    # trims and returns the result that ends before a specified character
    stop="\n",
    # See the README for more details
    frequency_penalty=0,
    presence_penalty=0,
)

# Accessing the response
print(f"Model response is: {response.choices[0].message.content}")

# Seeing the usage
print(f"{response.usage}")
