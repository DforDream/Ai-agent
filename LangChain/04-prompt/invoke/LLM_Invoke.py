import os
from dotenv import load_dotenv
from langchain.chat_models import init_chat_model
from langchain_core.messages import HumanMessage, SystemMessage

load_dotenv(encoding="utf-8")

model = init_chat_model(
    model="qwen3.8-2.4t-a95b",
    model_provider="openai",
    api_key=os.getenv("QWEN_API_KEY"),
    base_url="https://dashscope.aliyuncs.com/compatible-mode/v1",
)
message = [
    SystemMessage(content="你是一个法律助手，只回答法律问题，超出范围回答：非法律问题无可奉告"),
    HumanMessage(content="简单介绍下广告法，一句话 50 字以内")
]
response = model.invoke(message)
print(type(response))
print(response.content)
print(response.content_blocks)