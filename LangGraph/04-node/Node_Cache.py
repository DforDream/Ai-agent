import time
from typing_extensions import TypedDict
from langgraph.graph import StateGraph
from langgraph.cache.memory import InMemoryCache
from langgraph.types import CachePolicy

class State(TypedDict):
    x: int
    result: int

builder = StateGraph(State)

def expensive_node(state: State) -> dict[str, int]:
    """模拟耗时计算（sleep 3 秒），用于观察缓存命中时不再执行。"""
    time.sleep(3)
    return {"result": state["x"] * 2}

builder.add_node(
    node="expensive_node",
    action=expensive_node,
    cache_policy=CachePolicy(ttl=8),
)
builder.set_entry_point("expensive_node")
builder.set_finish_point("expensive_node")

app = builder.compile(cache=InMemoryCache())

print("第一次执行（无缓存，耗时 3 秒）：")
print(app.invoke({"x": 5}))

print("\n第二次运行利用缓存并快速返回：")
print(app.invoke({"x": 5}))

print("\n等待 8 秒，缓存过期...")
time.sleep(8)
print("8 秒后第三次执行（重新计算，耗时 3 秒）：")
print(app.invoke({"x": 5}))
