import os
from langchain_community.embeddings import DashScopeEmbeddings
from langchain_community.vectorstores import Redis
from langchain_core.documents import Document
from dotenv import load_dotenv

load_dotenv()

embeddings = DashScopeEmbeddings(
    model="qwen3.7-text-embedding",
    dashscope_api_key=os.getenv("QWEN_API_KEY"),
)

texts = [
    "通义千问是阿里巴巴研发的大语言模型。",
    "Redis 是一个高性能的键值存储系统，支持向量检索。",
    "LangChain 可以轻松集成各种大模型和向量数据库。",
]

documents = [
    Document(page_content=text, metadata={"source": "manual"})
    for text in texts
]

vector_store = Redis.from_documents(
    documents,
    embeddings,
    redis_url="redis://localhost:26379",
    index_name="my_index11",
)

retriever = vector_store.as_retriever(search_kwargs={"k": 2})
results = retriever.invoke("LangChain 和 Redis 怎么结合？")
for res in results:
    print(res.page_content)