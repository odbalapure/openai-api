import tiktoken
import pandas

data = pandas.read_csv("./csv/word_embedding.csv")
words = list(data["text"])

enc = tiktoken.encoding_for_model("text-embedding-3-small")
total_tokens = sum([len(enc.encode(word)) for word in words])

cost_per_token = 0.02 / 1_00_000
estimated_cost = total_tokens * cost_per_token

print(f"Estimated cost in USD: {estimated_cost:.10f}")
