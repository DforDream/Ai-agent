from dotenv import load_dotenv
load_dotenv(encoding="utf-8")

from langchain.chat_models import init_chat_model
from langchain_core.chat_history import InMemoryChatMessageHistory
from loguru import logger
import os

llm = init_chat_model(
    model="qwen3.8-2.4t-a95b",
    model_provider="openai",
    api_key=os.getenv("QWEN_API_KEY"),
    base_url="https://dashscope.aliyuncs.com/compatible-mode/v1",
)

history = InMemoryChatMessageHistory()

history.add_user_message("我叫张三，我的爱好是学习")
ai_message = llm.invoke(history.messages)
logger.info(f"第一次回答\n{ai_message.content}")
history.add_message(ai_message)

history.add_user_message("我叫什么？我的爱好是什么？")
ai_message2 = llm.invoke(history.messages)
logger.info(f"第二次回答\n{ai_message2.content}")
history.add_message(ai_message2)

for index,message in enumerate(history.messages, start=1):
    logger.info(f"第{index}条[{message.type}] {message.content}")
