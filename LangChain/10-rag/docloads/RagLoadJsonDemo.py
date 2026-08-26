from langchain_community.document_loaders import JSONLoader

docs = JSONLoader(
    file_path="assets/sample.json",
    jq_schema=".",  # 提取所有字段
    text_content=False,  # 是否按字符串处理内容
).load()
print(docs)
