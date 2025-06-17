import os
from openai import OpenAI

client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))


def create_meal_plan(ingredients, kcal):
    prompt = f"""
    Create a healthy meal plan for breakfast, lunch, dinner based on the
    ingredient in {ingredients}.
    The total calories should be below {kcal}
    """
    messages = [
        {"role": "system", "content": "You are a talented cook."},
        {"role": "user", "content": prompt},
    ]

    response = client.chat.completions.create(
        model="gpt-3.5-turbo",
        messages=messages,
        # Don't want determinstic answers
        temperature=1,
        max_tokens=1024,
        n=1,
    )

    return response.choices[0].message.content


foods = "Lentils, cabbage, corriander, oil"
output = create_meal_plan(foods, 1000)
