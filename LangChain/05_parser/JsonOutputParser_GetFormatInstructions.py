from langchain_core.output_parsers import JsonOutputParser
from langchain_core.prompts import ChatPromptTemplate
import os
from dotenv import load_dotenv
from langchain.chat_models import init_chat_model
from loguru import logger
from pydantic import BaseModel, Field

load_dotenv(encoding="utf-8")

class Person(BaseModel):
    time: str = Field(description="时间")
    person:str = Field(description="人物")
    event: str = Field(description="事件")

parser = JsonOutputParser(pydantic_object=Person)
format_instructions = parser.get_format_instructions()

chat_prompt_template = ChatPromptTemplate.from_messages([
    ("system", "你是一个AI助手，你只能输出结构化JSON数据。"),
    ("human", "请生成一个关于{topic}的新闻。{format_instructions}"),
])

prompt = chat_prompt_template.invoke(
    {"topic": "小米su7跑车", "format_instructions": format_instructions}
)
logger.info(prompt)

model = init_chat_model(
    model="qwen3.8-2.4t-a95b",
    model_provider="openai",
    api_key=os.getenv("QWEN_API_KEY"),
    base_url="https://dashscope.aliyuncs.com/compatible-mode/v1",
)

result = model.invoke(prompt)
logger.info(f"模型原始输出:\n{result}")

response = parser.invoke(result)
logger.info(f"解析后的结构化结果:\n{response}")
logger.info(f"结果类型: {type(response)}")
