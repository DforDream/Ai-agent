from typing import TypedDict
from langgraph.graph import StateGraph, START, END

class BasicState(TypedDict):
    """本图的 State Schema：字段名 + 类型共同定义这张图允许流转的状态结构。"""
    user_input: str
    response: str
    count: int
    process_data: dict

basicState = StateGraph(BasicState)
basicState.add_edge(START, END)
app = basicState.compile()

initial_state = {
    "user_input": "a",
    "response": "resp",
    "count": 25,
    "process_data": {"k1": "v1"},
}

result = app.invoke(initial_state)
print(f"最后的结果是:{result}")