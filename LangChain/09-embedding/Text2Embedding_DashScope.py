import os
from langchain_community.embeddings import DashScopeEmbeddings
from dotenv import load_dotenv
load_dotenv()

embeddings = DashScopeEmbeddings(
    model="qwen3.7-text-embedding",
    dashscope_api_key=os.getenv("QWEN_API_KEY"),
)

text = "this is a test text"

query_result = embeddings.embed_query(text)

print("文本向量长度：", len(query_result), sep="")

doc_results = embeddings.embed_documents([
    "Hi there!",
    "Oh, hello!",
    "What's your name?",
    "My friends call me World",
    "Hello World!",
])

print(doc_results)

print(
    "文本向量数量：", len(doc_results), "，文本向量长度：", len(doc_results[0]), sep=""
)
