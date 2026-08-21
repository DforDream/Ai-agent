import os
from langchain.chat_models import init_chat_model
from dotenv import load_dotenv
load_dotenv(encoding="utf-8")

model = init_chat_model(
    model="qwen3.8-2.4t-a95b",
    model_provider="openai",
    api_key=os.getenv("QWEN_API_KEY"),
    base_url="https://dashscope.aliyuncs.com/compatible-mode/v1",
)

print(model.invoke("你是谁").content)

message = [
    {"role": "system", "content": "You are a helpful assistant"},
    {"role": "user", "content": "Hello，你是谁？"}
]
response = model.invoke(message)
print(response.content)