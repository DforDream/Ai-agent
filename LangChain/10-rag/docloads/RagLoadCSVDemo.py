from langchain_community.document_loaders import CSVLoader

docs_all = CSVLoader("assets/sample.csv").load()
print("=== 方式一：整行作为 page_content ===")
print(
    "page_content 示例:",
    (
        docs_all[0].page_content[:80] + "..."
        if len(docs_all[0].page_content) > 80
        else docs_all[0].page_content
    ),
)
print("metadata 示例:", docs_all[0].metadata, "\n")

docs_split = CSVLoader(
    file_path="assets/sample.csv",
    metadata_columns=["title", "author"],
    content_columns=["content"],
).load()

print("=== 方式二：content 列作为正文，title/author 进 metadata ===")
print("page_content 示例:", docs_split[0].page_content)
print("metadata 示例:", docs_split[0].metadata)
