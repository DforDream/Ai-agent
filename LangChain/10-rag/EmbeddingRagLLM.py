from langchain.chat_models import init_chat_model
import os
from langchain_community.document_loaders import Docx2txtLoader
from langchain_core.prompts import PromptTemplate
from langchain_classic.text_splitter import CharacterTextSplitter
from langchain_core.runnables import RunnablePassthrough
from langchain_community.embeddings import DashScopeEmbeddings
from langchain_community.vectorstores  import Redis
from dotenv import load_dotenv

load_dotenv()

llm = init_chat_model(
    model="qwen3.8-2.4t-a95b",
    model_provider="openai",
    api_key=os.getenv("QWEN_API_KEY"),
    base_url="https://dashscope.aliyuncs.com/compatible-mode/v1",
)

prompt_template = """
    请使用以下提供的文本内容来回答问题。仅使用提供的文本信息，
    如果文本中没有相关信息，请回答"抱歉，提供的文本中没有这个信息"。

    文本内容：
    {context}

    问题：{question}

    回答：
    "
"""

prompt = PromptTemplate(
    template=prompt_template,
    input_variables=["context", "question"],
)

embeddingsModel = DashScopeEmbeddings(
    model="qwen3.7-text-embedding",
    dashscope_api_key=os.getenv("QWEN_API_KEY"),
)

loader = Docx2txtLoader("LangChain/10-rag/alibaba-java.docx")
documents = loader.load()

text_splitter = CharacterTextSplitter(
    chunk_size=1000,
    chunk_overlap=0,
    length_function=len,
)
texts = text_splitter.split_documents(documents)

print(f"文档个数:{len(texts)}")

vector_store = Redis.from_documents(
    documents=texts,
    embedding=embeddingsModel,
    redis_url="redis://localhost:26379",
    index_name="my_index3",
)

retriever = vector_store.as_retriever(search_kwargs={"k": 2})

rag_chain = {"context": retriever, "question": RunnablePassthrough()} | prompt | llm

question = "00000和A0001分别是什么意思"
result = rag_chain.invoke(question)
print("\n=== 有外挂知识库（RAG：从 alibaba-java.docx 检索）===")
print("问题:", question)
print("回答:", result.content)

no_rag_chain = (
    {
        "context": lambda _: "（未提供相关文档，模拟无外挂知识库）",
        "question": RunnablePassthrough(),
    }
    | prompt
    | llm
)
result_no_rag = no_rag_chain.invoke(question)
print("\n=== 无外挂知识库（模拟：不检索，仅靠模型自身知识）===")
print("问题:", question)
print("回答:", result_no_rag.content)

