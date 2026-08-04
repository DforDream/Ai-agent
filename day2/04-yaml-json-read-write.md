# Day 2 学习目标 4：读写 YAML 和 JSON

这份文件帮你准备配置文件相关练习：读取 JSON、写 JSON、读取 YAML、修改值后再写回。不会直接给具体练习文件的答案。

## 1. JSON 是什么

JSON 是一种常见数据格式，常用于 API 响应和配置文件。

JSON 示例：

```json
{
  "app_name": "demo",
  "debug": true,
  "port": 8000,
  "features": ["api", "cli"]
}
```

特点：

- key 必须用双引号。
- 字符串必须用双引号。
- 布尔值是 `true` / `false`。
- 空值是 `null`。
- 不支持注释。

## 2. Python 读取 JSON

使用标准库 `json`。

```python
import json
from pathlib import Path


path = Path("config.json")
content = path.read_text(encoding="utf-8")
data = json.loads(content)

print(data.get("app_name"))
```

也可以：

```python
with open("config.json", "r", encoding="utf-8") as file:
    data = json.load(file)
```

区别：

- `json.loads()` 读取字符串。
- `json.load()` 读取文件对象。

## 3. Python 写 JSON

```python
import json
from pathlib import Path


data = {
    "app_name": "demo",
    "debug": False,
    "port": 8000,
}

path = Path("config.json")
path.write_text(
    json.dumps(data, ensure_ascii=False, indent=2),
    encoding="utf-8",
)
```

重要参数：

- `ensure_ascii=False`：保留中文，不转成 unicode 编码。
- `indent=2`：格式化输出，方便阅读。

## 4. 修改 JSON 中的值

基本流程：

1. 读取文件。
2. 解析成 Python 字典。
3. 修改字典里的值。
4. 写回文件。

示例结构：

```python
import json
from pathlib import Path


path = Path("config.json")
data = json.loads(path.read_text(encoding="utf-8"))

data["debug"] = False

path.write_text(
    json.dumps(data, ensure_ascii=False, indent=2),
    encoding="utf-8",
)
```

注意：

- 写回会覆盖原文件内容。
- 写回前确认你修改的是正确 key。
- JSON 不保留注释，因为 JSON 本身不支持注释。

## 5. YAML 是什么

YAML 也是配置文件常用格式。

YAML 示例：

```yaml
app_name: demo
debug: true
port: 8000
features:
  - api
  - cli
```

特点：

- 可读性比 JSON 更强。
- 支持注释。
- 对缩进敏感。
- 常用于配置文件，例如 CI、Docker Compose、Kubernetes。

## 6. YAML 和 JSON 的区别

JSON：

- 更常用于 API 数据交换。
- 格式严格。
- 不支持注释。
- Python 标准库内置支持。

YAML：

- 更常用于配置文件。
- 更适合人手动编辑。
- 支持注释。
- Python 需要安装第三方库，例如 `PyYAML`。

## 7. 安装 PyYAML

如果没有安装：

```bash
pip install pyyaml
```

导入时名字是：

```python
import yaml
```

包名和导入名不完全一样：

- 安装包名：`pyyaml`
- 代码导入名：`yaml`

## 8. Python 读取 YAML

```python
from pathlib import Path

import yaml


path = Path("config.yaml")
content = path.read_text(encoding="utf-8")
data = yaml.safe_load(content)

print(data.get("app_name"))
```

推荐使用：

```python
yaml.safe_load()
```

不要随便使用：

```python
yaml.load()
```

因为不安全的 YAML 加载方式可能执行非预期内容。

## 9. Python 写 YAML

```python
from pathlib import Path

import yaml


data = {
    "app_name": "demo",
    "debug": False,
    "port": 8000,
}

path = Path("config.yaml")
path.write_text(
    yaml.safe_dump(data, allow_unicode=True, sort_keys=False),
    encoding="utf-8",
)
```

重要参数：

- `allow_unicode=True`：保留中文。
- `sort_keys=False`：尽量保持字典原有顺序。

## 10. 修改 YAML 中的值

基本流程和 JSON 类似：

```python
from pathlib import Path

import yaml


path = Path("config.yaml")
data = yaml.safe_load(path.read_text(encoding="utf-8"))

data["debug"] = False

path.write_text(
    yaml.safe_dump(data, allow_unicode=True, sort_keys=False),
    encoding="utf-8",
)
```

## 11. Path 的基本用法

推荐使用 `pathlib.Path` 处理路径。

```python
from pathlib import Path


path = Path("day2") / "config.yaml"
```

读取文本：

```python
text = path.read_text(encoding="utf-8")
```

写入文本：

```python
path.write_text("hello", encoding="utf-8")
```

判断文件是否存在：

```python
if path.exists():
    print("exists")
```

## 12. 文件编码

建议始终写：

```python
encoding="utf-8"
```

这样可以减少中文乱码问题。

## 13. 配置文件设计建议

好的配置：

```yaml
app_name: demo
debug: false
api:
  base_url: https://api.example.com
  timeout: 10
```

不太好的配置：

```yaml
app_name: demo
api_base_url_timeout_debug: something
```

建议：

- 相关配置放在一起。
- key 名清楚。
- 不要把多个含义塞进一个 key。
- 布尔值用 true/false。
- 数字就写数字，不要写成字符串。

## 14. 常见错误

YAML 缩进错误：

```yaml
app:
name: demo
```

更合理：

```yaml
app:
  name: demo
```

JSON 使用单引号：

```json
{
  'name': 'demo'
}
```

这是错误 JSON。JSON 必须用双引号：

```json
{
  "name": "demo"
}
```

## 15. 自查清单

写读写配置文件脚本时检查：

- 是否使用 `encoding="utf-8"`。
- JSON 是否用 `json.loads()` / `json.dumps()`。
- YAML 是否用 `yaml.safe_load()` / `yaml.safe_dump()`。
- 写回文件前是否确认修改了正确字段。
- 是否理解写回会覆盖原文件内容。
- YAML 缩进是否正确。
- JSON 字符串是否使用双引号。
