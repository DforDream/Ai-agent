import os
from dotenv import load_dotenv
load_dotenv(encoding="utf-8")

from langchain.chat_models import init_chat_model
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import JsonOutputKeyToolsParser, StrOutputParser
from loguru import logger
from QueryWeatherTool import get_weather

llm = init_chat_model(
    model="qwen3.8-2.4t-a95b",
    model_provider="openai",
    api_key=os.getenv("QWEN_API_KEY"),
    base_url="https://dashscope.aliyuncs.com/compatible-mode/v1",
)

llm_with_tools = llm.bind_tools([get_weather])

parser = JsonOutputKeyToolsParser(key_name=get_weather.name, first_tool_only=True)

get_weather_chain = llm_with_tools | parser | get_weather

output_prompt = PromptTemplate.from_template(
    """你将收到一段 JSON 格式的天气数据{weather_json}，请用简洁自然的方式将其转述给用户。
    以下是天气 JSON 数据：
    请将其转换为中文天气描述，例如：
    "北京现在天气：多云，气温 28℃，体感有点闷热（约 32℃），湿度 75%，微风（东南风 2 米/秒），
    能见度很好，大约 10 公里。建议穿短袖短裤。适合做户外运动。"
    """
)
output_parser = StrOutputParser()
output_chain = output_prompt | llm | output_parser

full_chain = get_weather_chain | (lambda x: {"weather_json": x}) | output_chain

result = full_chain.invoke("请问北京今天的天气如何？")
logger.info(result)
