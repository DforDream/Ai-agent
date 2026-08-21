from langchain_ollama import ChatOllama

model = ChatOllama(
    model="qwen3:4b",
    base_url="http://localhost:11434",
)
response = model.invoke("什么是LangChain,100字以内回答")

print(response)
print('**'*50)
print(response.content)