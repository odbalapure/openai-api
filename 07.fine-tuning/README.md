## Fine Tuning 

- Fine tuning means changing the base model to create a unique and differentiated experience for you users.
- Using demonstrations to show the model how to perform a task is called "few shost learning".
- Fine-tuning improves on few shot learning by training on many more examples that can fit in the prompt.
- Results in improved steerability; users will have more control over the generated output.
- Reliable output formatting; the model can consistently produce output in a desired format.
- Custom tone; ability to adjust model's output to match a specific style or voice.

Steps:
- Prepare your data
- Upload files
- Creating fine tuning job
- Use a fine-tuned model

> **NOTE**: Fine tuning costs money, there is initial training cost. Also, it has a usage cost.

## Fine Tune the GPT Model

### Prepare data

To send data to OpenAI, it needs to formatted the following way
```python
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
```

Also, we need to send the training and evaluation data:
- Training Data:
    - Think of it as a study material; its meant for learning.
    - The data that actually fine tunes the model on your specific task or domain.
    - The model will learn patterns, relationship, preferred output from this data.
- Evaluation Data:
    - Think of it as the mock test or dry run.
    - Evaluation data is for evaluation; model compares its ouput with the evaluation data.
    - Measures how well the model performs on unseen but related data during training.

### Upload files

Upload the evaluation and the training data
# Upload dataset for training and evaluation
```python
train = openai.files.create(
    file=open("train.jsonl", "rb"), purpose="fine-tune"
)  # FileObject(id='file-XUTvDccy8wPqoUFefb7FwT', bytes=6160, created_at=1750298809, filename='train.jsonl', object='file', purpose='fine-tune', status='processed', expires_at=None, status_details=None)

val = openai.files.create(
    file=open("eval.jsonl", "rb"), purpose="fine-tune"
)  # FileObject(id='file-LqMfd1ZReHxrUkbPwsdzcP', bytes=6085, created_at=1750298962, filename='eval.jsonl', object='file', purpose='fine-tune', status='processed', expires_at=None, status_details=None)
```

### Create fine tuning job

You get FileObject id that can be used to create a fine tuning job.

```python
response = openai.fine_tuning.jobs.create(
    training_file=train.id, validation_file=val.id, model="gpt-3.5-turbo"
)
# <FineTuningJob fine_tuning.job id=ftjob-GxIuSEbU4oYvFZUUndY72zpu at 0x27e52ef26f0> JSON: {
#   "object": "fine_tuning.job",
#   "id": "ftjob-GxIuSEbU4oYvFZUUndY72zpu",
#   "model": "gpt-3.5-turbo-0613",
#   "created_at": 1695972236,
#   "finished_at": null,
#   "fine_tuned_model": null,
#   "organization_id": "org-IXBiBnJ5QPnEVI56pPwN085r",
#   "result_files": [],
#   "status": "validating_files",
#   "validation_file": "file-0QC5ayB6O7gHgCBKuBOD2enn",
#   "training_file": "file-0vqcMamQA8ZMajx1FmfhheD0",
#   "hyperparameters": {
#     "n_epochs": "auto"
#   },
#   "trained_tokens": null,
#   "error": null
# }
```

Once the job has been submitted:
- Job creation returns a job id
- This response object contains the list of events which we can log
- This can also tell us whether the job was completed or not including the fine tuned model id, status completion etc.

```python
job_id = response.id
resp1 = openai.fine_tuning.jobs.retrieve(job_id)
resp2 = openai.fine_tuning.jobs.list_events(id=job_id, limit=10)
events = resp2.data
events.reverse()
for event in events:
    print(event.message)
```

### Use the fine tuned Model

The fine tuned model id can be seen in the event list object or OpenAI sends it via an email once the job is processed and the model is ready.

```python
completion = openai.chat.completions.create(
    model="ft:gpt-3.5-turbo-0613:cma::842Ezx4k",
    messages=[
        {
            "role": "system",
            "content": "You are a smart assistant that replies with Latin proverbs",
        },
        {"role": "user", "content": "How can one find inner peace?"},
    ],
)
```