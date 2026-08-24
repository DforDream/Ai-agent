import os
from langchain.chat_models import init_chat_model
from langchain_core.output_parsers import StrOutputParser
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.runnables import RunnableLambda
from loguru import logger
from dotenv import load_dotenv

load_dotenv(encoding="utf-8")

model = init_chat_model(
    model="qwen3.8-2.4t-a95b",
    model_provider="openai",
    api_key=os.getenv("QWEN_API_KEY"),
    base_url="https://dashscope.aliyuncs.com/compatible-mode/v1",
)

def debug_print(x):
    logger.info(f"中间结果：{x}")
    return {"input": x}

prompt1 = ChatPromptTemplate.from_messages([
    ("system", "你是一个知识渊博的计算机专家，请用中文简短回答"),
    ("human", "请简短介绍什么是{topic}"),
])
parser1 = StrOutputParser()
chain1 = prompt1 | model | parser1

prompt2 = ChatPromptTemplate.from_messages(
    [("system", "你是一个翻译助手，将用户输入内容翻译成英文"), ("human", "{input}")]
)
parser2 = StrOutputParser()
chain2 = prompt2 | model | parser2

# 方式一：直接把函数放在 | 之间，LCEL 会自动包装成 Runnable
full_chain = chain1 | debug_print | chain2
result1 = full_chain.invoke({"topic": "langchain"})
logger.info(f"最终结果111:{result1}")

# 方式二：显式使用 RunnableLambda(函数)，效果相同
debug_node = RunnableLambda(debug_print)
full_chain = chain1 | debug_node | chain2
result2 = full_chain.invoke({"topic": "langchain"})
logger.info(f"最终结果222:{result2}")