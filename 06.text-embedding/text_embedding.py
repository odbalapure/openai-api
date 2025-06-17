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
# 2    eggs     [xxx, yyy, zzz]
# 1   curry     [xxx, yyy, zzz]
# 0    fish     [xxx, yyy, zzz]
# 4  cheese     [xxx, yyy, zzz]
# 3    mayo     [xxx, yyy, zzz]

data.to_csv("./csv/word_embedding.csv", index=False)  # Don't add DataFrame index column
# text,embedding
# fish,[xxx, yyy, zzz]
# mayo,[xxx, yyy, zzz]
# cheese,[xxx, yyy, zzz]
# eggs,[xxx, yyy, zzz]
# curry,[xxx, yyy, zzz]
