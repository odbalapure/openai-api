## Text Embedding

- An embedding is a numeric representation of data/text.
- Its a vector of floating point numbers.

Why we need it?
> When we are dealing with natural language processing models, you are working with text. They cannot deal with text easily.

Goat and cow are similar words.  
Capital and capitol are not similar. 

> **NOTE**: Vectors that are numerically similar are semantically similar as well

Distance b/w two embeddings measure their relatedness, which translates the relatedness b/w the text concept they represent.  

Embedding applications:
- Semantic search
- Clustering
- Recommendations
- Anamoly detection
- Diversity measurement
- Classification

Building a chatbot for CS, embedding can help the model understand - _I need help with billing_ or _I have payment problem_ are related issues.

## Create an embedding

```python
text = "Sample text"
model="text-embedding-3-small"
text = text.replace("\n", " ")
response = client.embeddings.create(
    model=model,
    input=text,
)

return response.data[0].embedding
```

## Estimate cost of embedding

Token cost estimation using the `tiktoken` package.

```python
import tiktoken
import pandas

# Getting list of words from the CSV
data = pandas.read_csv("./csv/word_embedding.csv")
words = list(data["text"])

# Calculate the no. of tokens
enc = tiktoken.encoding_for_model("text-embedding-3-small")
total_tokens = sum([len(enc.encode(word)) for word in words])

# Find cost per token
cost_per_token = 0.02 / 1_00_000
estimated_cost = total_tokens * cost_per_token

print(f"Estimated cost in USD: {estimated_cost:.10f}")
```