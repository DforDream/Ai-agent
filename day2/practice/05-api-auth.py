from dotenv import load_dotenv
import requests
import os

load_dotenv()

def get_url() -> str:
    return 'https://api.github.com/user'
url = get_url()

def get_print(response: requests.Response) -> str:
    return print(response.status_code)

def main() -> None:
    response = requests.get(url)
    get_print(response)

def main2() -> None:
    headers = {
        'Authorization': f'Bearer {os.getenv("AUTH_TOKEN")}',
    }
    response = requests.get(
        url,
        headers=headers,
    )
    get_print(response)


if __name__ == "__main__":
    main()
    main2()
# 由于github 不让提交token .env 文件已删除
# main 401
# main2 200