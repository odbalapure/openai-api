import os
from openai import OpenAI

import pandas

client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))


def get_embedding(text, model="text-embedding-3-small"):
    """
    Create embedding from the text data
    :text str: CSV row text
    :model str: Model
    :return: Embedding
    """
    text = text.replace("\n", " ")
    response = client.embeddings.create(
        model=model,
        input=text,
    )

    return response.data[0].embedding


# This is some random text
data = pandas.read_csv("./csv/sample.csv")
data = data.sample(frac=1)  # frac means randomly shuffled

data["embedding"] = data["text"].apply(lambda x: get_embedding(x))
#      text     embedding
# 2    eggs     [float1, float2, ..., float1536]
# 1   curry     [float1, float2, ..., float1536]
# 0    fish     [float1, float2, ..., float1536]
# 4  cheese     [float1, float2, ..., float1536]
# 3    mayo     [float1, float2, ..., float1536]

data.to_csv("./csv/word_embedding.csv", index=False)  # Don't add DataFrame index column
# text,embedding
# fish,[float1, float2, ..., float1536]
# mayo,[float1, float2, ..., float1536]
# cheese,[float1, float2, ..., float1536]
# eggs,[float1, float2, ..., float1536]
# curry,[float1, float2, ..., float1536]
