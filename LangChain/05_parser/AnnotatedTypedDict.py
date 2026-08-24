from typing import Annotated, TypedDict

Age = Annotated[int, "年龄，范围0-150"]

class Person(TypedDict):
    name: str
    age: int
    age2: Age

p = Person(name="张三", age=111, age2=188)

print(p)
