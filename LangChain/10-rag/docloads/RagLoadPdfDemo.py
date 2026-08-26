from langchain_community.document_loaders import PyPDFLoader

docs = PyPDFLoader(
    file_path="assets/sample.pdf",
    extraction_mode="plain" # plain 纯文本；layout 按版面
).load()
print(docs)
