from dotenv import load_dotenv

load_dotenv(encoding="utf-8")

from langchain_core.output_parsers import StrOutputParser
from langchain_core.prompts import PromptTemplate
from langchain.chat_models import init_chat_model
import os

llm = init_chat_model(
    model="qwen3.8-2.4t-a95b",
    model_provider="openai",
    api_key=os.getenv("QWEN_API_KEY"),
    base_url="https://dashscope.aliyuncs.com/compatible-mode/v1",
)
prompt = PromptTemplate.from_template("请回答我的问题：{question}")
parser = StrOutputParser()
chain = prompt | llm | parser

print(chain.invoke({"question": "我叫张三，你叫什么?"}))

print(chain.invoke({"question": "你知道我是谁吗?"}))
