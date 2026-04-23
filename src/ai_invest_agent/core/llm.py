from openai import OpenAI
from ai_invest_agent.config.settings import OPENAI_API_KEY, MODEL

client = OpenAI(api_key=OPENAI_API_KEY)

def call_llm(prompt: str) -> str:
    response = client.chat.completions.create(
        model=MODEL,
        messages=[{"role": "user", "content": prompt}]
    )
    return response.choices[0].message.content