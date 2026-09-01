import os
from typing import TypedDict
from langchain.chat_models import init_chat_model
from langgraph.graph import StateGraph, START
from dotenv import load_dotenv

load_dotenv()

class State(TypedDict):
    query: str
    answer: str

def node(state: State):
    print("开始调用 node 节点")

    model = init_chat_model(
        model="qwen3.8-2.4t-a95b",
        model_provider="openai",
        api_key=os.getenv("QWEN_API_KEY"),
        base_url="https://dashscope.aliyuncs.com/compatible-mode/v1",
    )

    llm_result = model.invoke([("user", state["query"])])
    print("llm invoke 结束", end="\n\n")

    return {"answer": llm_result}

def main():
    graph = (
        StateGraph(state_schema=State).add_node(node).add_edge(START, "node").compile()
    )

    inputs = {"query": "帮我生成一个200字的小学生作文，主题为我的一天"}

    # messages：从图内触发的大模型调用处流式输出；(chunk, metadata) 见官方文档
    for chunk, _metadata in graph.stream(inputs, stream_mode="messages"):
        # print(f"type of chunk:{type(chunk)}")  # 调试时可打开
        print(chunk.content, end="")
        # print(chunk, end="")


if __name__ == "__main__":
    main()
