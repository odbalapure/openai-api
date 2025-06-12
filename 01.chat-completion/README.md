## Installion and API key

#### Install openai locally

```zsh
pip3 install --upgrade openai -q
```

**NOTE**: 
- `--upgrade` will upgrade the package to the latest version if already installed.
- We can use `gpt-3.5-turbo` for chat completion; but it can be used for non-chat tasks as well.

## Dash Board

- API Keys: https://platform.openai.com/account/api-keys
- Usage: https://platform.openai.com/settings/organization/usage
- Tokenizer: https://platform.openai.com/tokenizer


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

<br>

## Exploring OpenAI module

### Initializing the openai client

```python
import os
from openai import OpenAI

client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

# Get the list of all openai models
print(client.models.list())
```

### First prompt

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
        # contains the actual prompt
        {"role": "user", "content": "What is the theory of relativity"},
    ],
    # gives 2 answers
    n=2,
    temperature=0.2,
    seed=1234,
    top_p=1,
    max_tokens=1000,
    stop="\n",
    frequency_penalty=0,
    presence_penalty=0,
)
```

Where,
- `n`: 
    - Gives the no. of answers
    - Eg: n=2 will give 2 answers
    - **NOTE**: Make sure to use "n=1" for predictible result
- `temperature`:
    - Higher value makes the model more creative; but it can generate nonsense
    - Lower value  makes the model more determinsitc; generate predictable results
    - The value ranges from "0" to "2.0"
    - **NOTE**: OpenAI models are non-determinstic, i.e. identical inputs can produce different outputs
- `seed`:
    - It helps in locking the randomness
    - Ensures reproducibility; using same "prompt", "model", "temperature", "seed" ensure the same result
- `top_p`:
    - Every token has a 'probability' value
    - **top_p** adds the values and returns only the tokens whose added value reaches the input value
    - Eg: `top_p=0.1` will get us top 10% most probable tokens
    - **NOTE**: Better not to use it along side "temperature"
- `max_tokens`:
    - Limits the max no. of tokens to be generated in chat completion
    - **NOTE**: Should be chosen carefully; else the output will be cutoff and won't make sense
- `stop`:
    - Trims and returns the result that ends before a specified character
    - Supports up to 4 stop sequences using a list.
    - Eg: Example: stop = [":", "\n"]
- `frequency_penalty`:
    - It defaults to 0; ranges from -2.0 to +2.0
    - Higher values reduce repeated tokens; encourages more varied word choice
    - It reduces frequent repetition; avoids saying the same word over and over
- `presence_penalty`:
    - It defaults to 0; ranges from -2.0 to +2.0
    - Promotes diversity; avoids even mentioning the same word twice

### frequency_penalty VS presence_penalty

If the following sentence is being generated
> "I saw an apple. The apple was red. The apple was tasty."

With `presence_penalty`:
- The model sees that it already used the word "apple" once, so it tries not to use it again at all.
- Result might be:
> "I saw an apple. The fruit was red and tasty."

With `frequency_penalty`:
- The model can still use "apple" again, just not too many times.
- Result might be:
> "I saw an apple. The apple was red. It was tasty."

<br>

## Reasoning Models

The cheapest and most capable chat completion model is `gtp-3.5-turbo`, whereas the `o3-mini` is the cheapest reasoning-focused model.

**NOTE**: Its best to wrap prompt inside a python like docstring `""" {prompt} """`.

```python
response = client.chat.completions.create(
        model="o3-mini",
        # parameter works for "o-series" reasoning model only
        # controls how much internal reasoning the model uses before responding
        # defaults to "medium"
        reasoning_effort="medium",
        messages=[
            {"role": "system", "content": "You are helpful assistant!"},
            {"role": "user", "content": prompt},
        ],
    )
```

**NOTE**: Reasoning models take longer to respond.

### Best Practices

- If quick factual responses are required, standard GPT models are more than sufficient
- Keep prompts simple and direct
    - Good: 'summarize the paper in one paragraphq'
    - Bad: 'think step by step and summarize this paper while considering key findings, methods, implication'
- Avoid chain of thoughts
    - They already generate internal thought process
    - Its better to ask for final model to avoid performance degradation
- Use delimiters for clarification
    - Use XML tags, markdown for code blocks etc.
- Start with zero-shot, then use few-shot if needed
    - If the model struggles, provide 1 or 2 carefully chosen examples
    - Eg:
        - `input`: Describe AI breakthrough in 50 words
        - `example`: gpt-4o reduced latency, improving real time interactions
        - `your turn`:
- Provide specific guidelines
    - Eg: Instead of asking for cost effective solution, ask for solution with budget under 500 and setup time under 2hrs
- Be clear about end goal
    - Eg: Generate a plan for AI powered chatbot and success criteria would be keeping the cost under $1k per month

<br>

## How GTP models work

- OpenAI's GPT family of models are all Large Language Models (LLM).
- An LLM is a type of AI that can generate and understand human language.