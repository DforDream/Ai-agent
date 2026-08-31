from typing import List
from typing_extensions import TypedDict
from langgraph.graph import StateGraph, START, END

class DefaultReducerState(TypedDict):
    foo: int
    bar: List[str]

def node_default_1(state: DefaultReducerState) -> dict:
    """节点1 只更新 foo，bar 保持原样（本示例中会被节点2 覆盖 bar）。"""
    print(state["foo"])
    print(state["bar"])
    return {"foo": 22}

def node_default_2(state: DefaultReducerState) -> dict:
    """节点2 只更新 bar；foo 保持为节点1 写入的 22。"""
    print(state["foo"])
    print(state["bar"])
    return {"bar": ["bye1", "bye2", "bye3"]}

def main():
    print("1. 默认 Reducer（覆盖更新）演示:\n")
    builder = StateGraph(DefaultReducerState)
    builder.add_node("node1", node_default_1)
    builder.add_node("node2", node_default_2)
    builder.add_edge(START, "node1")
    builder.add_edge("node1", "node2")
    builder.add_edge("node2", END)
    graph = builder.compile()

    result = graph.invoke(input={"foo": 1, "bar": ["hi"]})
    print(f"执行结果: {result}\n")



if __name__ == "__main__":
    main()
