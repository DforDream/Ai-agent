from typing import TypedDict
from langgraph.graph import StateGraph, START, END
import uuid

class HelloState(TypedDict):
    name: str
    greeting: str

def greet(helloState: HelloState) -> dict:
    name = helloState["name"]
    return {"greeting": f"你好,{name}"}

def add_emoji(helloState: HelloState) -> dict:
    greeting = helloState["greeting"]
    return {"greeting": greeting + "  。。。😄"}

graph = StateGraph(HelloState)
graph.add_node("greeting", greet)
graph.add_node("add_emoji", add_emoji)
graph.add_edge(START, "greeting")
graph.add_edge("greeting", "add_emoji")
graph.add_edge("add_emoji", END)

app = graph.compile()

result = app.invoke({"name": "Lucas"}) 
print(result)
print(result["greeting"])

print(app.get_graph().print_ascii())
print("=" * 50)
print(app.get_graph().draw_mermaid())
print("=" * 50)

png_bytes = app.get_graph().draw_mermaid_png(max_retries=2, retry_delay=2.0)
output_path = "langgraph" + str(uuid.uuid4())[:8] + ".png"
with open(output_path, "wb") as f:
    f.write(png_bytes)
print(f"图片已生成：{output_path}")