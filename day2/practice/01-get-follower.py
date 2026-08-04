import requests
import json

def main() -> None:
    url = "https://api.github.com/users/torvalds"
    response = requests.get(url, timeout=10)
    if response.status_code == 200:
        data = json.loads(response.text)
        print(data.get("followers"))
    else:
        print(f"请求失败，状态码：{response.status_code}")


if __name__ == "__main__":
    main()

# 314535