from langchain_core.tools import tool

@tool
def add_number(a:int, b:int) -> int:
    """两个整数相加"""
    return a + b

result = add_number.invoke({"a": 1, "b": 2})
print(result)

print()

print(f"{add_number.name=}\n{add_number.description=}\n{add_number.args=}\n{add_number.return_direct=}")
