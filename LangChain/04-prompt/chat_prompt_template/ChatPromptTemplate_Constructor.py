from langchain_core.prompts import ChatPromptTemplate
import os
from dotenv import load_dotenv
from langchain.chat_models import init_chat_model

load_dotenv()

chatPromptTemplate = ChatPromptTemplate.from_messages([
    ("system", "你是一个AI开发工程师，你的名字是{name}。"),
    ("human", "你能帮我做什么?"),
    ("ai", "我能开发很多{thing}。"),
    ("human", "{user_input}"),
])

prompt = chatPromptTemplate.format_messages(
    **{"name": "小谷AI", "thing": "AI", "user_input": "7 + 5等于多少"}
)
print(prompt)

llm = init_chat_model(
    model="qwen3.8-2.4t-a95b",
    model_provider="openai",
    api_key=os.getenv("QWEN_API_KEY"),
    base_url="https://dashscope.aliyuncs.com/compatible-mode/v1",
)
print()
print("======================")

response = llm.invoke(prompt)
print(response)
print(response.content)
