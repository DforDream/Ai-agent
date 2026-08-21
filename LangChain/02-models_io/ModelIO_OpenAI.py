import os
from openai import OpenAI
from dotenv import load_dotenv
load_dotenv(encoding="utf-8")

client = OpenAI(
    api_key=os.getenv("QWEN_API_KEY"),
    base_url="https://dashscope.aliyuncs.com/compatible-mode/v1",
)

response = client.chat.completions.create(
    model="qwen3.8-2.4t-a95b",
    messages=[
        {"role": "system", "content": "You are a helpful assistant"},
        {"role": "user", "content": "Hello，你是谁？"}
    ],
    stream=False,
)

print(response.choices[0].message.content)