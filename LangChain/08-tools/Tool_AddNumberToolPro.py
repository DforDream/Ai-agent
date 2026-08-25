from langchain_core.tools import tool
from pydantic import BaseModel, Field
from loguru import logger

class FieldInfo(BaseModel):
    a: int = Field(description="第一个整数")
    b: int = Field(description="第二个整数")

@tool(args_schema=FieldInfo)
def add_number(a: int, b:int) -> int:
    """计算两个整数之和"""
    return a + b

logger.info(f"name = {add_number.name}")
logger.info(f"description = {add_number.description}")
logger.info(f"args = {add_number.args}")
logger.info(f"return_direct = {add_number.return_direct}")

res = add_number.invoke({"a": 1, "b": 2})
logger.info(res)
