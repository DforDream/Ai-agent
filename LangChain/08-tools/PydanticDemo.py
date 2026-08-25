from pydantic import BaseModel, ValidationError, StrictInt

class User(BaseModel):
    id: StrictInt # 严格整数：不接受字符串等，必须已是 int，否则报错
    name: str
    age: int = 0 # 可选字段，默认 0；传入值会被校验并转换

try:
    u = User(id=42, name="z3")
except ValidationError as e:
    print(e)
print(u.id, type(u.id))
print()
print()

try:
    User(id="abc", name="z3")
except ValidationError as e:
    print(e)