from langchain_community.document_loaders import UnstructuredWordDocumentLoader

docs = UnstructuredWordDocumentLoader(
    file_path="assets/alibaba-more.docx",
    mode="single",  # single 整篇一个 Document；elements 按元素切分
).load()
print(docs)