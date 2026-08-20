from langchain_openai import (ChatOpenAI)
import os
from dotenv import load_dotenv
load_dotenv(encoding="utf-8")  # encoding 指定 utf-8，避免 .env 中中文注释乱码

llm = ChatOpenAI(
    model="qwen3.8-2.4t-a95b",  # 模型名需与阿里百炼「模型广场」中的调用名一致
    api_key=os.getenv("QWEN_API_KEY"),
    base_url="https://dashscope.aliyuncs.com/compatible-mode/v1",  # 阿里百炼 OpenAI 兼容接口地址
)

# invoke：同步调用，传入用户问题字符串，返回 AIMessage 等消息对象
response = llm.invoke("你是谁")

# response 为 LangChain 消息对象，包含 content、additional_kwargs 等元数据
print(response)  # 打印完整对象（含 token 用量、finish_reason 等元数据，便于调试）
print()
print(response.content)  # 只取「正文」文本，即模型回复内容

print()