import os
from retrieval.index_builder import build_index


def load_or_build_index(folder):

    if os.path.exists("vector_cache"):
        print("Loading existing vector index...")
        return build_index(folder)

    print("Building new vector index...")

    index = build_index(folder)

    os.makedirs("vector_cache", exist_ok=True)

    return index