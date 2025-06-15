## Prompt Engineering

- Choose the latest and most capable models
- Position instructions clearly with deilimters
- Provide detailed instructions for the context, outcome or length
- Use the RFT format
- Few shot prompting
- Specify the steps required to complete the task
- Give models time to "think"

### Position instructions clearly with deilimters

Put instructions at the beginning of the prompt, each on their own line, use deilimiters to clearly indicate distinct parts of the prompt.  

```python
text = '''
prompt engineering is the new discipline for developing and optimizing prompts
'''

prompt = f'''
translate this text to German
```{text}```
'''
```

### Provide detailed instructions for the context, outcome or length

Be specific, descriptive and as detailed as possible about the desired context and outcome or length.  

```python
text = '''
a large text
'''

# Good prompt
prompt = f'''
Summarize the text below
Text: ```{text}```
'''

# Better prompt
prompt = f"""
Summarize the text below, delimited by triple backticks.
Begin the summary with an intro sentence, followed by bullet points that hihglihght the key points.
Conclude the summary with a sentence that encapsulates the central idea of the text.
Text: ```{text}```
"""
```

### Use RTF format

RTF stands for role, task amd format

```python

# mention the role
system_role = "You are an experienced Linux system administrator."

# detailed prompt with output format
prompt = """
Task: Configure an NGINX web server for hosting a website on Ubuntu.

Requirements:
1. The operating system is Ubuntu (latest LTS version assumed).
2. The website domain is gpt-prompt.ai.
3. Install and configure SSL using Let's Encrypt via Certbot.
4. Ensure all HTTP traffic is redirected to HTTPS.
5. Provide explanations after each step and command.

Output Format:
- Use clear and descriptive headings.
- Wrap each terminal command in triple backtick code blocks.
- Follow each command with a concise explanation suitable for an intermediate-level sysadmin.
- Avoid unnecessary verbosity, but don’t skip important details.

Assume a fresh Ubuntu server with sudo access and a domain already pointed to the server's IP.
"""
```

### Few shot prompting

**Zero-Shot**: user provides a prompt and the LLM tries to generate the o/p as well it can.  

**Multi-Shot**: user provides examples of desired output, along with clear instructions and context.  

We can mention the assitant role, its the assistant’s previous response. The assistant role is critical for maintaining context across multiple turns. If you're doing a multi-step conversation or follow-ups, you must include previous assistant messages like this:

```
// template:
messages = [
    {"role": "system", "content": system_role},
    {"role": "user", "content": user_prompt},
    {"role": "assistant", "content": assistant_response},
    {"role": "user", "content": followup_question},
]

// eg:
messages = [
    {"role": "system", "content": system_role},
    {"role": "user", "content": "Topic: rain"},
    {"role": "assistant", "content": "Rain falls from the sky..."},
    {"role": "user", "content": "Topic: love"},
    {"role": "user", "content": "Love is not a word, its a feeling..."}
]
```

### Give models time to think

In simple terms it is called as **think before answering**, also known as **Chain of Thought** prompting.

LLMs are token predictors, not truth validators:
- Asking for "the answer" triggers pattern recall.
- Asking for "step by step" triggers internal logic simulation.


LLMs are good at mimicking answers, but that’s not the same as reasoning.  If you ask:
> Is x = 3 the solution to 5x + 3 = 18?

It might just say "Yes", even if it's wrong - because it recognizes the structure, not the logic.

Instead of: Is x = 3 the solution?
Use:
> Solve 5x + 3 = 18 step by step. Then compare your result to x = 3 and explain if it’s correct.

**NOTE**: That’s Chain of Thought: it _unrolls reasoning_ like a chain before giving the conclusion.


### Avoid hallucinations using guarding

If you provide a prompt like
> Write an aritcle about Un-obtainium

The LLM will provide an article, even if such a thing never existed.

Instead mention
> Write an aritcle about Un-obtainium. Write only facts about this element according to source such as Wikipedia, Google scholar, Encyclopedia or reliable public sources. If you don't find information just say "I don't know".

### Other tactics

#1. Don't use negations
- Tell the prompt what to do (tell a story is less than 500 words)
- And what not to do (don't write a story longer than 500 words)

#2. We can drop hints in the prompt to get desired output

```
Write a program to convert temperatur from F to C
function() {}
```

The output will be a javascript function