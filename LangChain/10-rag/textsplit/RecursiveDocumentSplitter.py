from langchain_text_splitters import RecursiveCharacterTextSplitter
from langchain_unstructured import UnstructuredLoader

loader = UnstructuredLoader("rag.txt")
documents = loader.load()

text_splitter = RecursiveCharacterTextSplitter(
    chunk_size=100,
    chunk_overlap=30,
    length_function=len,
)

splitter_documents = text_splitter.split_documents(documents)

print(f"分割文档数量：{len(splitter_documents)}")
for splitter_document in splitter_documents:
    print(f"文档片段：{splitter_document.page_content}")
    print(
        f"文档片段大小：{len(splitter_document.page_content)}, 文档元数据：{splitter_document.metadata}"
    )
