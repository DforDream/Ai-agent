from langchain_core.prompts import PromptTemplate

template = PromptTemplate.from_template(
    "你是一个专业的{role}工程师，请回答我的问题给出回答，我的问题是：{question}"
)

prompt = template.format(role="pathon开发", question="快速排序怎么写？")
print(prompt)
print("\n\n")

template = PromptTemplate.from_template("请给我一个关于{topic}的{type}解释。")
prompt = template.format(topic="量子力学", type="详细")
print(prompt) 
print(type(prompt))