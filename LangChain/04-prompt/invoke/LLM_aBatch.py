import os
import asyncio
from dotenv import load_dotenv
from langchain.chat_models import init_chat_model

load_dotenv()

model = init_chat_model(
    model="qwen3.8-2.4t-a95b",
    model_provider="openai",
    api_key=os.getenv("QWEN_API_KEY"),
    base_url="https://dashscope.aliyuncs.com/compatible-mode/v1",
)

questions = [
    "什么是redis?简洁回答，字数控制在100以内",
    "Python的生成器是做什么的？简洁回答，字数控制在100以内",
    "解释一下Docker和Kubernetes的关系?简洁回答，字数控制在100以内",
]

async def async_batch_call():
    response = await model.abatch(questions)
    print(f"响应类型：{type(response)}")

    for q,r in zip(questions, response):
        print(f"问题：{q}\n回答：{r.content}\n")

if __name__ == "__main__":
    asyncio.run(async_batch_call())