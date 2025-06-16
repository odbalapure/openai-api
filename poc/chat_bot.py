import os
import time
from openai import OpenAI

client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

# q1 = "give me healthy food items"
# q2 = "make some recipe with it"
# q3 = "what is the amount of kcal"

# messages = [
#     {"role": "system", "content": "Answer as concisely as possible"},
#     {"role": "user", "content": q1},
# ]
# response = client.chat.completions.create(
#     model="gpt-3.5-turbo",
#     messages=messages,
#     temperature=0.7,
# )
# bot_response_1 = response.choices[0].message.content

# messages = [
#     {"role": "system", "content": "Answer as concisely as possible"},
#     {"role": "user", "content": q1},
#     {"role": "assitant", "content": bot_response_1},
#     {"role": "user", "content": q2},
# ]
# response = client.chat.completions.create(
#     model="gpt-3.5-turbo",
#     messages=messages,
#     temperature=0.7,
# )
# bot_response_2 = response.choices[0].message.content

questions = list()
bot_responses = list()
messages = list()

system_prompt = input("System prompt: ") or "Answer as concisely as possible"
print("\n")
messages.append({"role": "system", "content": system_prompt})

while True:
    current_question = input("Me: ")

    if current_question.lower() in ["exit", "quit", "bye"]:
        print("Chat Bot: I was happy to assist you. Bye!")
        time.sleep(2)
        break

    if current_question.lower() == "":
        continue

    # Append user's prompt
    messages.append({"role": "user", "content": current_question})
    questions.append(current_question)

    response = client.chat.completions.create(
        model="gpt-3.5-turbo",
        messages=messages,
        temperature=0.8,
    )

    current_response = response.choices[0].message.content
    print(f"Chat Bot: {current_response}\n")
    bot_responses.append(current_response)

    # Append assistant's response to continue the conversation context
    messages.append({"role": "assistant", "content": current_response})
    print("\n" + "-" * 50 + "\n")
