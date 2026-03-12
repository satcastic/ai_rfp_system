from retrieval.index_builder import build_index
from retrieval.query_engine import create_query_engine


folder = "test_documents"

index = build_index(folder)

query_engine = create_query_engine(index)


response = query_engine.query(
    "What is the required throughput?"
)

print("\nAnswer:\n")

print(response)