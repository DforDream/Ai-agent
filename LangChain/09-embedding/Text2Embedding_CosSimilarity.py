import dashscope
import os
import numpy as np
from http import HTTPStatus
from dotenv import load_dotenv
load_dotenv()

texts = ["我喜欢吃苹果", "苹果是我最喜欢吃的水果", "我喜欢用苹果手机"]

embeddings = []

for text in texts:
    print(text)
    input_data = text
    resp = dashscope.TextEmbedding.call(
        model="qwen3.7-text-embedding",
        api_key=os.getenv("QWEN_API_KEY"),
        input=input_data
    )
    print(resp)
    if resp.status_code == HTTPStatus.OK:
        embedding = resp.output["embeddings"][0]["embedding"]
        embeddings.append(embedding)

print(len(embeddings))
def cosine_similarity(v1, v2):
    dot_product = np.dot(v1, v2)
    norm1 = np.linalg.norm(v1)
    norm2 = np.linalg.norm(v2)
    return dot_product / (norm1 * norm2)

print("文本相似度比较结果:")
print("=" * 60)

for i in range(len(texts)):
    for j in range(i + 1, len(texts)):
        similarity = cosine_similarity(embeddings[i], embeddings[j])
        print(f"文本{i+1} vs 文本{j+1}:")
        print(f"  文本{i+1}: {texts[i]}")
        print(f"  文本{j+1}: {texts[j]}")
        print(f"  余弦相似度: {similarity:.4f}")
        print("-" * 40)