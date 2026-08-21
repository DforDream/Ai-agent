from langchain_core.prompts import ChatPromptTemplate
from langchain_core.messages import HumanMessage, SystemMessage

chat_prompt_template = ChatPromptTemplate([
    SystemMessage(content="你是AI助手，你的名字叫{name}。"),
    HumanMessage(content="请问：{question}"),
])

message = chat_prompt_template.format_messages(name="亮仔", question="什么是LangChain")
print(message)

chat_prompt_template2 = ChatPromptTemplate.from_messages([
    SystemMessage(content="你是AI助手，你的名字叫{name}。"),
    HumanMessage(content="请问：{question}"),
])

message2 = chat_prompt_template2.format_messages(name="亮仔", question="什么是LangChain")
print(message2)

# chat_prompt_template2.from_messages 我要的是“消息列表”
# chat_prompt_template2.invoke 我要的是“PromptValue 对象”
# chat_prompt_template.format 我要的是“纯字符串”
#  推荐使用 from_messages 和 invoke 获取 prompt
