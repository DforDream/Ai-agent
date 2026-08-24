from typing import Annotated
from pydantic import BaseModel, Field, ValidationError

Age = Annotated[int, Field(ge=0, le=150, description="年龄，范围0-150")]

class Person(BaseModel):
    name: str
    age: int
    age2: Age

try:
    p = Person(name="张三", age=111, age2=10)
except ValidationError as e:
    print("数据校验失败：")
    print(e)
