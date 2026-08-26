from langchain_community.document_loaders import UnstructuredMarkdownLoader

docs = UnstructuredMarkdownLoader(
    file_path="assets/sample.md",
    mode="elements",  # single 整篇；elements 按元素切分
).load()
print(docs)
