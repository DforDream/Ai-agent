import os
from langchain.chat_models import init_chat_model
from dotenv import load_dotenv
load_dotenv(encoding="utf-8")

model = init_chat_model(
    model="qwen3.8-2.4t-a95b",
    model_provider="openai",
    api_key=os.getenv("QWEN_API_KEY"),
    base_url="https://dashscope.aliyuncs.com/compatible-mode/v1",
    temperature=0,
)

print(model.invoke("写一句关于春天的词，14字以内"))
# <class 'langchain_openai.chat_models.base.ChatOpenAI'>
print(type(model))
# <class 'str'>
print(type(model.invoke("写一句关于春天的词，14字以内").content))
# <class 'langchain_core.messages.ai.AIMessage'>
print(type(model.invoke("写一句关于春天的词，14字以内")))

for i in range(3):
    print(f"---第{i+1}次调用---")
    print(model.invoke("写一句关于春天的词，14字以内").content)
