import os
from dotenv import load_dotenv
from langchain.chat_models import init_chat_model
from langchain_core.output_parsers import PydanticOutputParser
from langchain_core.prompts import ChatPromptTemplate
from loguru import logger
from pydantic import BaseModel, Field, field_validator

load_dotenv(encoding="utf-8")

class Product(BaseModel):
    name: str = Field(description="产品名称")
    category: str = Field(description="产品分类")
    description: str = Field(description="产品描述")

    @field_validator("description")
    def validate_description(cls, value):
        if len(value) < 10:
            raise ValueError("产品描述长度必须大于等于10个字符")
        return value

parser = PydanticOutputParser(pydantic_object=Product)
format_instructions = parser.get_format_instructions()

chat_prompt_template = ChatPromptTemplate.from_messages([
    ("system", "你是一个AI助手，你只能输出结构化的json数据\n{format_instructions}"),
    ("human", "请你输出标题为：{topic}的新闻内容"),
])

prompt = chat_prompt_template.invoke({"topic": "华为Mate X7", "format_instructions": format_instructions})
logger.info(prompt)

model = init_chat_model(
    model="qwen3.8-2.4t-a95b",
    model_provider="openai",
    api_key=os.getenv("QWEN_API_KEY"),
    base_url="https://dashscope.aliyuncs.com/compatible-mode/v1",
)

result = model.invoke(prompt)
logger.info(f"模型原始输出:\n{result.content}")

response = parser.invoke(result)
logger.info(f"解析后的结构化结果:\n{response}")
logger.info(f"结果类型: {type(response)}")

