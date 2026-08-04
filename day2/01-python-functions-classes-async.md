# Day 2 学习目标 1：Python 函数、类、async/await 基本用法

这份文件帮你准备 Python 相关练习：写函数、写类、理解 `async` / `await` 的基本结构。重点是看懂和会组织代码，不直接给练习答案。

## 1. 函数

函数用于把一段可以复用的逻辑封装起来。

基本格式：

```python
def function_name(param1: str, param2: int) -> str:
    result = f"{param1}: {param2}"
    return result
```

常见要点：

- `def` 用来定义普通函数。
- 参数写在括号里。
- `-> str` 是 type hint，表示函数预期返回字符串。
- `return` 把结果交回给调用方。
- 函数名建议用小写加下划线，例如 `get_user_info`。

示例：

```python
def add(a: int, b: int) -> int:
    return a + b


total = add(3, 5)
print(total)
```

练习时你需要能做到：

- 把重复逻辑提取成函数。
- 让函数接收参数。
- 让函数返回结果，而不是只在函数里 `print`。
- 用清晰的函数名表达功能。

## 2. 字典和 JSON 风格数据

调用 API 后，经常拿到类似 JSON 的数据。在 Python 中，解析后的 JSON 通常是 `dict` 或 `list`。

字典示例：

```python
user = {
    "login": "example-user",
    "followers": 123,
    "public_repos": 8,
}

print(user["login"])
print(user.get("followers"))
```

`dict["key"]` 和 `dict.get("key")` 的区别：

- `dict["key"]`：key 不存在会报错。
- `dict.get("key")`：key 不存在会返回 `None`，也可以指定默认值。

```python
followers = user.get("followers", 0)
```

处理 API 返回值时，推荐用 `.get()`，因为外部数据不一定稳定。

## 3. 类

类用于描述一类对象，把数据和相关行为放在一起。

基本格式：

```python
class User:
    def __init__(self, name: str, age: int) -> None:
        self.name = name
        self.age = age

    def say_hello(self) -> str:
        return f"Hello, I am {self.name}"
```

使用类：

```python
user = User("Alice", 18)
message = user.say_hello()
print(message)
```

关键点：

- `class User:` 定义类。
- `__init__` 是初始化方法，创建对象时自动执行。
- `self` 表示当前对象本身。
- `self.name = name` 把参数保存到对象上。
- 类里面的函数叫方法。

什么时候用类：

- 一组数据和操作经常一起出现。
- 你想把状态保存下来。
- 代码已经开始有多个相关函数和变量。

什么时候先不用类：

- 只是写一个很短的脚本。
- 只有一两个简单步骤。
- 普通函数已经足够清楚。

## 4. 同步函数和异步函数

普通函数：

```python
def get_message() -> str:
    return "hello"
```

异步函数：

```python
async def get_message_async() -> str:
    return "hello"
```

异步函数调用时通常需要 `await`：

```python
async def main() -> None:
    message = await get_message_async()
    print(message)
```

运行异步入口：

```python
import asyncio


async def main() -> None:
    print("start")


asyncio.run(main())
```

## 5. async/await 适合什么

`async` / `await` 常用于等待外部操作：

- 请求网络 API。
- 读写文件。
- 等数据库响应。
- 同时处理多个耗时任务。

它不是为了让 CPU 计算变快，而是为了在等待时不阻塞程序。

## 6. await 的基本规则

常见规则：

- `await` 只能写在 `async def` 函数里面。
- `async def` 函数调用后，不会马上得到普通结果，而是得到一个 coroutine。
- 要拿到结果，需要 `await` 或用 `asyncio.run()` 执行。

错误思路：

```python
result = get_message_async()
print(result)
```

这样通常打印出来的是 coroutine 对象，不是最终结果。

正确结构：

```python
import asyncio


async def get_message_async() -> str:
    return "hello"


async def main() -> None:
    result = await get_message_async()
    print(result)


asyncio.run(main())
```

## 7. 脚本入口

Python 文件常见入口写法：

```python
def main() -> None:
    print("run script")


if __name__ == "__main__":
    main()
```

异步版本：

```python
import asyncio


async def main() -> None:
    print("run async script")


if __name__ == "__main__":
    asyncio.run(main())
```

这样写的好处：

- 文件被直接运行时，会执行 `main()`。
- 文件被别的代码导入时，不会自动执行主逻辑。

## 8. 写 Python 脚本的建议结构

建议顺序：

```python
import json
from pathlib import Path


def helper_function() -> None:
    pass


def main() -> None:
    pass


if __name__ == "__main__":
    main()
```

结构清楚比一开始写得很复杂更重要。

## 9. 自查清单

写完 Python 文件后检查：

- 文件名是否清楚。
- 函数名是否表达了用途。
- 是否把主要逻辑放进了 `main()`。
- 是否给函数加了必要的 type hint。
- 是否避免把所有代码堆在文件最外层。
- 处理外部数据时是否考虑 key 不存在的情况。
- 如果用了 `async`，是否正确使用了 `await` 和 `asyncio.run()`。
