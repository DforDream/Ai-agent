import json
import os
from typing import Annotated, List, TypedDict
from langgraph.graph import StateGraph, START, END
from langgraph.graph.message import add_messages
from langchain.chat_models import init_chat_model
from langchain_core.messages import BaseMessage, HumanMessage, message_to_dict
from dotenv import load_dotenv

load_dotenv()

# 1. 定义状态 State：messages 使用 add_messages 规约器，节点返回的每条新消息会自动追加到列表
class DiliState(TypedDict):
    # add_messages 是 LangGraph 提供的「规约器」（Reducer），来自 langgraph.graph.message。
    # 含义：该字段不是「覆盖」更新，而是「追加」——节点只返回新增的消息（如 [reply]），
    # 框架会把它们合并到当前消息列表末尾，适合多轮对话、多节点共同往同一列表写消息。
    # 若不用 add_messages，节点返回 {"messages": [reply]} 会直接覆盖掉之前的对话历史。
    messages: Annotated[List[BaseMessage], add_messages]

llm = init_chat_model(
    model="qwen3.8-2.4t-a95b",
    model_provider="openai",
    api_key=os.getenv("QWEN_API_KEY"),
    base_url="https://dashscope.aliyuncs.com/compatible-mode/v1",
)

def model_node(state: DiliState):
    reply = llm.invoke(state["messages"])
    return {"messages": [reply]}

graph = StateGraph(DiliState)
graph.add_node("model_node", model_node)

graph.add_edge(START, "model_node")
graph.add_edge("model_node", END)

app = graph.compile()

result = app.invoke({
    "messages": [HumanMessage(content="请用一句话解释什么是 LangGraph。")]
})

print("模型回答：", result["messages"][-1].content)

print("\n--- result 格式化输出 ---")
print(
    json.dumps(
        result,
        ensure_ascii=False,
        indent=2,
        default=lambda o: message_to_dict(o) if isinstance(o, BaseMessage) else str(o),
    )
)

print(app.get_graph().print_ascii())
print("=" * 50)
print(app.get_graph().draw_mermaid())
print("=" * 50)
