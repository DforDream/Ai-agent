from langchain_core.prompts import PromptTemplate

template = PromptTemplate.from_template(
  "你是一个专业的{role}工程师，请回答我的问题给出回答，我的问题是：{question}"
)

partial = template.partial(role="pathon开发")
print(partial)
print(type(partial))
print()

prompt = partial.invoke("二分查找算法怎么写？")
print(prompt)
print(type(prompt))
print()