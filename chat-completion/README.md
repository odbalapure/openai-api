## Installion and API key

#### Install openai locally

```zsh
pip3 install --upgrade openai -q
```

**NOTE**: 
- `--upgrade` will upgrade the package to the latest version if already installed.
- We can use `gpt-3.5-turbo` for chat completion; but it can be used for non-chat tasks as well.

## Dash Board

API Keys: https://platform.openai.com/account/api-keys
Usage: https://platform.openai.com/settings/organization/usage
Tokenizer: https://platform.openai.com/tokenizer


#### Accessing API Key

```python
import openai
import os
import getpass

# Getting the API key via environment variable
openai.api_key = os.environ["OPENAI_API_KEY"]
print(openai.api_key)

# Getting the API key via terminal
key = getpass.getpass("Enter you API key: ")
openai.api_key = key
print(key)

# Getting the API key from a file
key = open("key.txt").read().strip("\n")
print(key)
```

**NOTE**: If the API KEY is part of the shell file, simply do this
```python
import os
key = os.getenv("OPENAI_API_KEY")
```

## Exploring OpenAI module

```python
import os
from openai import OpenAI

client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

# Get the list of all openai models
print(client.models.list())
```

## First prompt

```python
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
```