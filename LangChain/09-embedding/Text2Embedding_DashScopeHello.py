import os
import dashscope
from http import HTTPStatus
from dotenv import load_dotenv
load_dotenv()

dashscope.api_key = os.getenv("QWEN_API_KEY")

input_text = "衣服的质量杠杠的"

resp = dashscope.TextEmbedding.call(
    model="qwen3.7-text-embedding",
    input=input_text
)

if resp.status_code == HTTPStatus.OK:
    print(resp)