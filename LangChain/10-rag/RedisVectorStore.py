from langchain_redis import RedisConfig, RedisVectorStore
from langchain_community.embeddings import DashScopeEmbeddings
import os
from dotenv import load_dotenv

load_dotenv()

embeddingsModel = DashScopeEmbeddings(
    model="qwen3.7-text-embedding",
    dashscope_api_key=os.getenv("QWEN_API_KEY"),
)

texts = [
    "我喜欢吃苹果",
    "苹果是我最喜欢吃的水果",
    "我喜欢用苹果手机",
]

embeddings = embeddingsModel.embed_documents(texts)
for i, vec in enumerate(embeddings,1):
    print(f"文本 {i}: {texts[i-1]}")
    print(f"向量长度: {len(vec)}")
    print(f"前5个向量值: {vec[:10]}\n")

metadata = [{ "segment_id": str(i)} for i in range(1, len(texts)+ 1)]

config = RedisConfig(
    index_name="newsgroups",
    redis_url="redis://localhost:26379",
)

vector_store = RedisVectorStore(
    embeddingsModel,
    config,
)

ids = vector_store.add_texts(texts, metadata)
print(ids[0:5])

