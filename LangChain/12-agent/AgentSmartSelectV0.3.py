import json
import os
from langchain_openai import ChatOpenAI
from dotenv import load_dotenv

load_dotenv()

from langchain_classic.agents import create_tool_calling_agent
from langchain_classic.agents import AgentExecutor
from langchain_core.prompts import ChatPromptTemplate
import importlib.util
from pathlib import Path

file_path = Path(r"LangChain\08-tools\QueryWeatherTool.py")
spec = importlib.util.spec_from_file_location("QueryWeatherTool", file_path)
module = importlib.util.module_from_spec(spec)
spec.loader.exec_module(module)

get_weather = module.get_weather

llm = ChatOpenAI(
    model="qwen3.8-2.4t-a95b",
    api_key=os.getenv("QWEN_API_KEY"),
    base_url="https://dashscope.aliyuncs.com/compatible-mode/v1",
)

prompt = ChatPromptTemplate.from_messages([
    ("system", "你是天气助手，请根据用户的问题，给出相应的天气信息"),
    ("human", "{input}"),
    (
        "placeholder",
        "{agent_scratchpad}",
    ),  # V0.3 必备：Agent 的「草稿本」，记录多轮推理与工具输出
])

tools = [get_weather]

agent = create_tool_calling_agent(llm, tools, prompt)

agent_executor = AgentExecutor(
    agent=agent,
    tools=tools,
    verbose=True,
)

result = agent_executor.invoke(
    {"input": "请问今天北京和上海的天气怎么样，哪个城市更热？"}
)

print(result)

