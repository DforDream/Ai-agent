import os
from dotenv import load_dotenv
from langchain.chat_models import (
    init_chat_model,
)  # 1.0 统一入口：根据 model + model_provider 创建聊天模型

load_dotenv(encoding="utf-8")

model = init_chat_model(
    model="qwen3.8-2.4t-a95b", # 模型 ID，与平台模型广场一致
    model_provider="openai",  # 表示使用「OpenAI 兼容」的 API（阿里百炼、通义等均兼容，阿里百炼不支持直接调用，需要通过OpenAI 兼容的 API 调用）
    api_key=os.getenv("QWEN_API_KEY"),  # 需事先 export 或在下面 load_dotenv 之后再用
    base_url="https://dashscope.aliyuncs.com/compatible-mode/v1",
)

print(model.invoke("你是谁").content)

print("*" * 50)

# 同一个系统里面，可以同时存在多个模型，比如
model2 = init_chat_model(
    model="deepseek-v3",
    model_provider="openai",
    api_key=os.getenv("QWEN_API_KEY"),
    base_url="https://dashscope.aliyuncs.com/compatible-mode/v1",
)

print(model2.invoke("你是谁").content)