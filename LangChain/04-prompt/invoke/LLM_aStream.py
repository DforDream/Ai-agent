import os
import asyncio
from dotenv import load_dotenv
from langchain.chat_models import init_chat_model
from langchain_core.messages import HumanMessage, SystemMessage
load_dotenv()

model = init_chat_model(
    model="qwen3.8-2.4t-a95b",
    model_provider="openai",
    api_key=os.getenv("QWEN_API_KEY"),
    base_url="https://dashscope.aliyuncs.com/compatible-mode/v1",
)

message = [
    SystemMessage(content="你叫小问，是一个乐于助人的AI人工助手"),
    HumanMessage(content="你是谁")
]

async def async_stream_call():
    response = model.astream(message)
    print(f"响应类型：{type(response)}")

    async for chunk in response:
        print(chunk.content, end="", flush=True)
        print("\n")

if __name__ == "__main__":
    asyncio.run(async_stream_call())