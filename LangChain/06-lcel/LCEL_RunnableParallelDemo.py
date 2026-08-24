import os
from langchain.chat_models import init_chat_model
from langchain_core.output_parsers import StrOutputParser
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.runnables import RunnableParallel
from loguru import logger
from dotenv import load_dotenv

load_dotenv(encoding="utf-8")

model = init_chat_model(
    model="qwen3.8-2.4t-a95b",
    model_provider="openai",
    api_key=os.getenv("QWEN_API_KEY"),
    base_url="https://dashscope.aliyuncs.com/compatible-mode/v1",
)

prompt1 = ChatPromptTemplate.from_messages([
    ("system", "你是一个知识渊博的计算机专家，请用中文简短回答"),
    ("human", "请简短介绍什么是{topic}"),
])
parser1 = StrOutputParser()
chain1 = prompt1 | model | parser1

prompt2 = ChatPromptTemplate.from_messages([
    ("system", "你是一个知识渊博的计算机专家，请用英文简短回答"),
    ("human", "请简短介绍什么是{topic}"),
])
parser2 = StrOutputParser()
chain2 = prompt2 | model | parser2

parallel_chain = RunnableParallel({
    "chinese": chain1,
    "english": chain2,
})

result = parallel_chain.invoke({"topic": "langchain"})
logger.info(result)

# 可选：打印并行链的 ASCII 图结构，便于理解“并行节点 + 汇总输出”的数据流
parallel_chain.get_graph().print_ascii()