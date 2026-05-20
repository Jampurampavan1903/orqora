import os
from pathlib import Path

from openai import OpenAI
from dotenv import load_dotenv

env_path = Path(__file__).resolve().parent.parent / ".env"
load_dotenv(dotenv_path=env_path)

client = OpenAI(
    api_key=os.getenv("GROQ_API_KEY"),
    base_url="https://api.groq.com/openai/v1"
)


def reviewer_agent(plan: str):

    prompt = f"""
    You are a senior reviewer agent.

    Review the following execution plan.

    Improve it and identify missing steps.

    Plan:
    {plan}
    """

    response = client.chat.completions.create(
       model="llama-3.3-70b-versatile",
        messages=[
            {
                "role": "user",
                "content": prompt
            }
        ]
    )

    return response.choices[0].message.content
