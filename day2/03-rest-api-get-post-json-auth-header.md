# Day 2 学习目标 3：REST API、GET/POST、JSON 和 auth header

这份文件帮你准备 API 相关练习：发送 GET/POST 请求、解析 JSON、理解认证 header。不会直接写出截图中练习的完整答案。

## 1. API 是什么

API 是程序之间通信的接口。你写 Python 脚本访问一个网址，服务器返回数据，这就是常见的 API 调用。

REST API 常见特点：

- 使用 URL 表示资源。
- 使用 HTTP method 表示动作。
- 常用 JSON 作为请求和响应格式。

例子：

```text
GET https://api.example.com/users/123
```

可以理解为：获取 id 为 123 的用户信息。

## 2. HTTP method

常见方法：

- `GET`：读取数据。
- `POST`：创建数据或提交数据。
- `PUT`：整体更新数据。
- `PATCH`：部分更新数据。
- `DELETE`：删除数据。

Day 2 重点先掌握：

- `GET`
- `POST`

## 3. GET 请求

GET 用来获取数据。

Python 常见写法：

```python
import requests


response = requests.get("https://api.example.com/users/123", timeout=10)
print(response.status_code)
print(response.text)
```

关键点：

- `status_code` 是 HTTP 状态码。
- `text` 是原始响应文本。
- `timeout` 用来避免请求一直卡住。

## 4. POST 请求

POST 常用来提交数据。

```python
import requests


payload = {
    "name": "Alice",
    "age": 18,
}

response = requests.post(
    "https://api.example.com/users",
    json=payload,
    timeout=10,
)

print(response.status_code)
print(response.text)
```

注意：

- `json=payload` 会把 Python 字典转成 JSON 请求体。
- 不要把 JSON 字符串手动拼接出来。
- 优先使用结构化数据，也就是 `dict`。

## 5. HTTP 状态码

常见状态码：

- `200 OK`：请求成功。
- `201 Created`：创建成功。
- `204 No Content`：成功但没有响应体。
- `400 Bad Request`：请求格式或参数有问题。
- `401 Unauthorized`：没有认证，或认证失败。
- `403 Forbidden`：认证了，但没有权限。
- `404 Not Found`：资源不存在。
- `429 Too Many Requests`：请求太频繁。
- `500 Internal Server Error`：服务器内部错误。

练习 API 时，先看状态码，再看响应内容。

## 6. JSON

JSON 是一种通用数据格式。

JSON 示例：

```json
{
  "login": "example-user",
  "followers": 123,
  "active": true
}
```

JSON 和 Python 的对应关系：

- JSON object 对应 Python `dict`。
- JSON array 对应 Python `list`。
- JSON string 对应 Python `str`。
- JSON number 对应 Python `int` 或 `float`。
- JSON boolean `true` / `false` 对应 Python `True` / `False`。
- JSON `null` 对应 Python `None`。

## 7. 解析响应 JSON

使用 `requests` 时：

```python
import requests


response = requests.get("https://api.example.com/users/123", timeout=10)
data = response.json()

print(data.get("login"))
```

常见注意点：

- 只有响应内容真的是 JSON 时，`response.json()` 才能成功。
- 如果服务器返回错误页面 HTML，`response.json()` 可能报错。
- 可以先检查 `status_code`。

更稳一点的写法：

```python
if response.status_code == 200:
    data = response.json()
else:
    print(f"request failed: {response.status_code}")
```

## 8. header

Header 是 HTTP 请求里的附加信息。

常见 header：

- `Accept`：告诉服务器你希望收到什么格式。
- `Content-Type`：告诉服务器你发过去的内容是什么格式。
- `Authorization`：认证信息。
- `User-Agent`：客户端标识。

示例：

```python
headers = {
    "Accept": "application/json",
    "User-Agent": "day2-learning-script",
}
```

发送请求时带上 headers：

```python
response = requests.get(
    "https://api.example.com/users/123",
    headers=headers,
    timeout=10,
)
```

## 9. auth header

很多 API 需要认证。认证信息通常放在 `Authorization` header 里。

常见格式：

```python
headers = {
    "Authorization": "Bearer YOUR_TOKEN_HERE",
    "Accept": "application/json",
}
```

或者有些平台使用：

```python
headers = {
    "Authorization": "token YOUR_TOKEN_HERE",
}
```

具体用哪种格式，要看 API 文档。

## 10. 不要把 token 写死在代码里

不推荐：

```python
TOKEN = "real-token-value"
```

推荐从环境变量读取：

```python
import os


token = os.getenv("API_TOKEN")
```

然后构造 header：

```python
headers = {
    "Authorization": f"Bearer {token}",
}
```

这样做的好处：

- token 不容易被提交到 Git。
- 换 token 时不用改代码。
- 更接近真实项目写法。

## 11. 401 和 200 的区别

认证相关练习中常见对比：

- 没带 token：可能返回 `401`。
- 带了有效 token：可能返回 `200`。

但具体状态码取决于 API 的设计。

你需要观察：

- 请求 URL 是否正确。
- header 是否正确。
- token 是否有效。
- token 权限是否足够。
- 响应状态码是什么。
- 响应 JSON 里有没有错误信息。

## 12. requests 的基本脚本结构

建议结构：

```python
import os
import requests


def build_headers() -> dict[str, str]:
    token = os.getenv("API_TOKEN")
    headers = {
        "Accept": "application/json",
        "User-Agent": "day2-learning-script",
    }

    if token:
        headers["Authorization"] = f"Bearer {token}"

    return headers


def main() -> None:
    headers = build_headers()
    response = requests.get(
        "https://api.example.com/resource",
        headers=headers,
        timeout=10,
    )
    print(response.status_code)


if __name__ == "__main__":
    main()
```

这是学习结构示例，不是具体练习答案。

## 13. 常见调试方法

打印状态码：

```python
print(response.status_code)
```

打印响应文本：

```python
print(response.text)
```

打印响应 header：

```python
print(response.headers)
```

打印解析后的 JSON：

```python
print(response.json())
```

调试顺序建议：

1. URL 是否对。
2. method 是否对。
3. header 是否对。
4. 参数或 body 是否对。
5. token 是否存在。
6. token 权限是否够。

## 14. 自查清单

写 API 脚本时检查：

- 是否设置了 `timeout`。
- 是否检查了 `status_code`。
- 是否使用 `response.json()` 解析 JSON。
- 是否用 `.get()` 读取可能不存在的字段。
- 是否没有把真实 token 写入代码。
- 是否知道 `401` 和 `403` 的区别。
- 是否把 header 写成了字典。
