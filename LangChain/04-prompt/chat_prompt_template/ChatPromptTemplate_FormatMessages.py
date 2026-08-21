from langchain_core.prompts import ChatPromptTemplate

chat_prompt_template = ChatPromptTemplate(
    [("system", "你是一个{role}，请回答我提出的问题"), ("human", "请回答:{question}")]
)

# ** 表示把字典「解包」成 key=value 的形式传入，适合参数已经在 dict 里的场景。
prompt_value = chat_prompt_template.format_messages(
    **{"role": "python开发工程师", "question": "堆排序怎么写"}
)
print(prompt_value)

prompt_value2 = chat_prompt_template.invoke(
    {"role": "python开发工程师", "question": "堆排序怎么写"}
)
print(prompt_value2.to_string())
print(prompt_value2.to_messages())
print()

prompt_value3 = chat_prompt_template.format(
    **{"role": "python开发工程师", "question": "堆排序怎么写"}
)
print(prompt_value3)