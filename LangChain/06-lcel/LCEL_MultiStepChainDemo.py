import os
from langchain.chat_models import init_chat_model
from langchain_core.output_parsers import StrOutputParser
from langchain_core.prompts import ChatPromptTemplate
from loguru import logger
from dotenv import load_dotenv

load_dotenv(encoding="utf-8")

model = init_chat_model(
    model="qwen3.8-2.4t-a95b",
    model_provider="openai",
    api_key=os.getenv("QWEN_API_KEY"),
    base_url="https://dashscope.aliyuncs.com/compatible-mode/v1",
)

prompt_template1 = ChatPromptTemplate.from_messages([
    ("system", "你是一个知识渊博的计算机专家，请用中文简短回答"),
    ("human", "请简短介绍什么是{topic}"),
])
parser1 = StrOutputParser()
chain1 = prompt_template1 | model | parser1
result1 = chain1.invoke({"topic": "langchain"})
logger.info(result1)

prompt_template2 = ChatPromptTemplate.from_messages(
    [("system", "你是一个翻译助手，将用户输入内容翻译成英文"), ("human", "{input}")]
)
parser2 = StrOutputParser()
chain2 = prompt_template2 | model | parser2

full_chain = chain1 | (lambda content: {"input": content}) | chain2
result = full_chain.invoke({"topic": "langchain"})
logger.info(result)
