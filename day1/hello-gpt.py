from openai import OpenAI
from dotenv import load_dotenv
import os

load_dotenv()

client = OpenAI(
    api_key=os.getenv("OPENAI_API_KEY"),
    base_url=os.getenv("OPENAI_BASE_URL"),
)

response = client.responses.create(
    model="gpt-5",
    input="Hello, who are you?",
    max_output_tokens=100,
)

print(response.output_text)

# uv run --with openai --with python-dotenv python hello-gpt.py
