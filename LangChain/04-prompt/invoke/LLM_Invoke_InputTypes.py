import asyncio
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

def demo_message_objects():
    message = [
        SystemMessage(content="你是一个专业的数学助手，回答要简短。"),
        HumanMessage(content="你好，你是谁？")
    ]
    response = model.invoke(message)
    print(type(response), response.content[:80] if response.content else "")

def demo_tuple_list():
    message = [
        ("system", "你是一个专业的数学助手，回答要简短。"),
        ("human", "你好，你是谁？")
    ]
    response = model.invoke(message)
    print(type(response), response.content[:80] if response.content else "")

def demo_dict_list():
    message = [
        {"role": "system", "content": "你是一个专业的数学助手，回答要简短。"},
        {"role": "user", "content": "你好，你是谁？"}
    ]
    response = model.invoke(message)
    print(type(response), response.content[:80] if response.content else "")

async def demo_ainvoke_tuple():
    response = await model.ainvoke(["user", "用一句话说明什么是素数"])
    print(type(response), response.content[:80] if response.content else "")

if __name__ == "__main__":
    print("--- Message 对象列表 ---")
    demo_message_objects()
    print("--- 元组列表 ---")
    demo_tuple_list()
    print("--- 字典列表 ---")
    demo_dict_list()
    print("--- ainvoke + 元组 ---")
    asyncio.run(demo_ainvoke_tuple())