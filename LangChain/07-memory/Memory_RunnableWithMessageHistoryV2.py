from dotenv import load_dotenv
load_dotenv(encoding="utf-8")

from langchain.chat_models import init_chat_model
from langchain_core.chat_history import InMemoryChatMessageHistory
from langchain_core.runnables.history import RunnableWithMessageHistory
from langchain_core.prompts import ChatPromptTemplate, MessagesPlaceholder
from langchain_core.output_parsers import StrOutputParser
import os

llm = init_chat_model(
    model="qwen3.8-2.4t-a95b",
    model_provider="openai",
    api_key=os.getenv("QWEN_API_KEY"),
    base_url="https://dashscope.aliyuncs.com/compatible-mode/v1",
)

store = {}

def get_session_history(session_id: str):
    if session_id not in store:
        store[session_id] = InMemoryChatMessageHistory()
    return store[session_id]

prompt = ChatPromptTemplate.from_messages([
    ("system", "你是一个友好的中文助理，会根据上下文回答问题。"),
    MessagesPlaceholder(variable_name="history"),
    ("human", "{question}"),
])

memory_chain = prompt | llm | StrOutputParser()

with_history = RunnableWithMessageHistory(
    memory_chain,
    get_session_history,
    input_messages_key="question",
    history_messages_key="history",
)

cfg_user_001 = {"configurable": {"session_id": "user-001"}}
cfg_user_002 = {"configurable": {"session_id": "user-002"}}

print("用户A（user-001）：我叫张三。")
print("AI：", with_history.invoke({"question": "我叫张三。"}, cfg_user_001))

print("\n用户B（user-002）：我叫李四。")
print("AI：", with_history.invoke({"question": "我叫李四。"}, cfg_user_002))

print("\n用户A（user-001）：我叫什么？")
print("AI：", with_history.invoke({"question": "我叫什么？"}, cfg_user_001))

print("\n用户B（user-002）：我叫什么？")
print("AI：", with_history.invoke({"question": "我叫什么？"}, cfg_user_002))

print("\n--- 当前 store 中的历史数据 ---")

for sid, history in store.items():
    print(f"[session_id={sid}] 共 {len(history.messages)} 条消息:")
    for i, msg in enumerate(history.messages):
        content = str(msg.content)
        content_preview = (content[:50] + "...") if len(content) > 50 else content
        print(f"  {i+1}. [{msg.type}] {content_preview}")

print("--- 以上 ---\n")