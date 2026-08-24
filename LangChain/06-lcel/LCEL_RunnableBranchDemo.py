import os
from langchain.chat_models import init_chat_model
from langchain_core.output_parsers import StrOutputParser
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.runnables import RunnableBranch
from loguru import logger
from dotenv import load_dotenv
load_dotenv(encoding="utf-8")

english_prompt = ChatPromptTemplate.from_messages(
    [("system", "你是一个英语翻译专家，你叫小英"), ("human", "{query}")]
)

japanese_prompt = ChatPromptTemplate.from_messages(
    [("system", "你是一个日语翻译专家，你叫小日"), ("human", "{query}")]
)

korean_prompt = ChatPromptTemplate.from_messages(
    [("system", "你是一个韩语翻译专家，你叫小韩"), ("human", "{query}")]
)

def determine_language(inputs):
    query = inputs["query"]
    if "日语" in query:
        return "japanese"
    elif "韩语" in query:
        return "korean"
    else:
        return "english"

model = init_chat_model(
    model="qwen3.8-2.4t-a95b",
    model_provider="openai",
    api_key=os.getenv("QWEN_API_KEY"),
    base_url="https://dashscope.aliyuncs.com/compatible-mode/v1",
)

parser = StrOutputParser()

chain = RunnableBranch(
    (lambda x: determine_language(x) == "japanese", japanese_prompt | model | parser),
    (lambda x: determine_language(x) == "korean", korean_prompt | model | parser),
    (english_prompt | model | parser),
)

test_queries = [
    {"query": '请你用韩语翻译这句话:"见到你很高兴"'},
    {"query": '请你用日语翻译这句话:"见到你很高兴"'},
    {"query": '请你用英语翻译这句话:"见到你很高兴"'},
]

for query_input in test_queries:
    lang = determine_language(query_input)
    logger.info(f"检测到语言类型: {lang}")

    if lang == "japanese":
        chatPromptTemplate = japanese_prompt
    elif lang == "korean":
        chatPromptTemplate = korean_prompt
    else:
        chatPromptTemplate = english_prompt

    #  手动
    formatted_messages = chatPromptTemplate.invoke({"query": query_input})
    logger.info(f"格式化后的提示: {formatted_messages}")
    
    # 自动
    result = chain.invoke(query_input)
    logger.info(f"输出结果: {result}\n")
