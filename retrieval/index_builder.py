import os
import chromadb

from llama_index.core import VectorStoreIndex, Document, Settings
from llama_index.core.storage.storage_context import StorageContext
from llama_index.vector_stores.chroma import ChromaVectorStore

from llama_index.embeddings.ollama import OllamaEmbedding
from llama_index.llms.ollama import Ollama

from ingestion.document_parser import parse_document


# -------------------------------
# Configure Local Models
# -------------------------------

# Embedding model
Settings.embed_model = OllamaEmbedding(
    model_name="nomic-embed-text"
)

# LLM model (use phi3 for your 8GB laptop)
Settings.llm = Ollama(
    model="phi3:mini",
    request_timeout=300.0
)


# -------------------------------
# Build / Load Vector Index
# -------------------------------

def build_index(document_folder):

    documents = []

    # Parse all files in the folder
    for file in os.listdir(document_folder):

        path = os.path.join(document_folder, file)

        parsed_doc = parse_document(path)

        doc = Document(
            text=parsed_doc["content"],
            metadata={
                "source_file": parsed_doc["source_file"],
                "document_type": parsed_doc["document_type"]
            }
        )

        documents.append(doc)

    # Create Chroma client
    client = chromadb.Client()

    # Create or load collection
    collection = client.get_or_create_collection("rfp_documents")

    vector_store = ChromaVectorStore(chroma_collection=collection)

    storage_context = StorageContext.from_defaults(
        vector_store=vector_store
    )

    # Build index
    index = VectorStoreIndex.from_documents(
        documents,
        storage_context=storage_context
    )

    return index