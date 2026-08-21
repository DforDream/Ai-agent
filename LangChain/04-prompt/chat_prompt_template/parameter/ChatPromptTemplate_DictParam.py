from langchain_core.prompts import ChatPromptTemplate

chat_prompt_template = ChatPromptTemplate.from_messages([
    {"role": "system", "content": "你是AI助手，你的名字叫{name}。"},
    {"role": "user", "content": "请问：{question}"},
])

message = chat_prompt_template.format_messages(name="小问", question="什么是LangChain")
print("from_messages:", message)

chat_prompt_template2 = ChatPromptTemplate([
    {"role": "system", "content": "你是AI助手，你的名字叫{name}。"},
    {"role": "user", "content": "请问：{question}"},
])

message2 = chat_prompt_template2.format_messages(name="小问", question="什么是LangChain")
print("构造函数:", message2)
