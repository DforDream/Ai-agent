from langchain_core.messages import HumanMessage, AIMessage
from langchain_core.prompts import ChatPromptTemplate, MessagesPlaceholder

chat_prompt_template = ChatPromptTemplate.from_messages([
    ("system", "你是一个资深的Python应用开发工程师，请认真回答我提出的Python相关的问题"),
    MessagesPlaceholder("memory"), # 变量名可自取，如 "history"、"chat_history" 等，invoke 时键与之一致即可
    ("human", "{question}"),
])

prompt = chat_prompt_template.invoke({
    "memory": [
        HumanMessage("我的名字叫亮仔，是一名程序员111"),
        AIMessage("好的，亮仔你好222"),
    ],
    "question": "请问我的名字叫什么？"
})

print(prompt.to_string())
print(prompt.to_messages())