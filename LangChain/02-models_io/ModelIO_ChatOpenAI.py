import os
from langchain_openai import ChatOpenAI
from dotenv import load_dotenv
load_dotenv(encoding="utf-8")

model = ChatOpenAI(
    model="qwen3.8-2.4t-a95b",
    api_key=os.getenv("QWEN_API_KEY"),
    base_url="https://dashscope.aliyuncs.com/compatible-mode/v1",
)

message = [
    {"role": "system", "content": "You are a helpful assistant"},
    {"role": "user", "content": "Hello，你是谁？"}
]

response=model.invoke(message)
print(response.content)