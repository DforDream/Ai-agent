import os
import json
from typing_extensions import TypedDict
from dotenv import load_dotenv
from langchain.agents import create_agent
from langchain_openai import ChatOpenAI

load_dotenv()

import importlib.util
from pathlib import Path

file_path = Path(r"LangChain\08-tools\QueryWeatherTool.py")
spec = importlib.util.spec_from_file_location("QueryWeatherTool", file_path)
module = importlib.util.module_from_spec(spec)
spec.loader.exec_module(module)

get_weather = module.get_weather

class WeatherCompareOutput(TypedDict):
    beijing_temp: float
    shanghai_temp: float
    hotter_city: str
    summary: str

model = ChatOpenAI(
    model="qwen3.8-2.4t-a95b",
    api_key=os.getenv("QWEN_API_KEY"),
    base_url="https://dashscope.aliyuncs.com/compatible-mode/v1",
)

agent = create_agent(
    model,
    tools=[get_weather],
    system_prompt=(
        "你是天气助手。"
        "当用户询问多个城市天气时，"
        "你需要分别调用工具获取数据，并进行比较分析。"
    ),
    response_format=WeatherCompareOutput,
)

result = agent.invoke({"input": "请问今天北京和上海的天气怎么样，哪个城市更热？"})
print(result)
print()
print(json.dumps(result["structured_response"], ensure_ascii=False, indent=2))

# 这个报错是模型不支持天气工具返回的格式