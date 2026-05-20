import os

from openai import OpenAI

client = OpenAI(
    api_key=os.getenv("GROQ_API_KEY"),
    base_url="https://api.groq.com/openai/v1"
)

def researcher_agent(task: str):

    response = client.chat.completions.create(
        model="llama-3.3-70b-versatile",
        messages=[
            {
                "role": "system",
                "content": "You are a world class AI researcher."
            },
            {
                "role": "user",
                "content": task
            }
        ]
    )

    return response.choices[0].message.content
