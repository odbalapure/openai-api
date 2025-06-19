import openai
import os
import json

client = openai.OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

data = []

# Read the contents
with open("proverbs.jsonl", "r") as file:
    for line in file:
        data.append(json.loads(line))

# Format the file contents as per OpenAI API
data_formatted = [
    {
        "messages": [
            {
                "role": "system",
                "content": "You are smart assitant that replies with latin proverbs.",
            },
            {"role": "user", "content": x["question"]},
            {"role": "assitant", "content": x["answer"]},
        ]
    }
    for x in data
]

training_data_set = data_formatted[:25]
evaluation_data_set = data_formatted[25:50]

# Saving training data set to train.jsonl
with open("train.jsonl", "w") as f:
    for line in training_data_set:
        json.dump(line, f)
        f.write("\n")

# Saving evaluation data set to eval.jsonl
with open("eval.jsonl", "w") as f:
    for line in evaluation_data_set:
        json.dump(line, f)
        f.write("\n")

# Upload dataset for training and evaluation
train = openai.files.create(
    file=open("train.jsonl", "rb"), purpose="fine-tune"
)  # FileObject(id='file-XUTvDccy8wPqoUFefb7FwT', bytes=6160, created_at=1750298809, filename='train.jsonl', object='file', purpose='fine-tune', status='processed', expires_at=None, status_details=None)

val = openai.files.create(
    file=open("eval.jsonl", "rb"), purpose="fine-tune"
)  # FileObject(id='file-LqMfd1ZReHxrUkbPwsdzcP', bytes=6085, created_at=1750298962, filename='eval.jsonl', object='file', purpose='fine-tune', status='processed', expires_at=None, status_details=None)

print(train.id, val.id)  # file-C9KbAwszdH69Qhix5WWBDM file-UviGaTfrBJEJBf3FrLvXk6

# Create fine tuning job
response = openai.fine_tuning.jobs.create(
    training_file=train.id, validation_file=val.id, model="gpt-3.5-turbo"
)

# This response object contains the list of events which we can log
# This can also tell us whether the job was completed or not including the fine tuned model id
job_id = response.id
resp1 = openai.fine_tuning.jobs.retrieve(job_id)
resp2 = openai.fine_tuning.jobs.list_events(id=job_id, limit=10)
events = resp2.data
events.reverse()
for event in events:
    print(event.message)


# Using the fine tuned model
completion = openai.chat.completions.create(
    model="ft:gpt-3.5-turbo-0613:cma::842Ezx4k",  # Model ID from the CHATGPT (email notification), once the job creation finishes
    messages=[
        {
            "role": "system",
            "content": "You are a smart assistant that replies with Latin proverbs",
        },
        {"role": "user", "content": "How can one find inner peace?"},
    ],
)
