import os
from ingestion.document_parser import parse_document

folder = "test_documents"

documents = []

for file in os.listdir(folder):

    path = os.path.join(folder, file)

    doc = parse_document(path)

    documents.append(doc)


for doc in documents:

    print("\n========================")
    print("Source File:", doc["source_file"])
    print("Document Type:", doc["document_type"])
    print("========================\n")

    print(doc["content"][:500])