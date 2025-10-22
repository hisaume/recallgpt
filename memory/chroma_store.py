from .memory_store import MemoryStore
import chromadb

class ChromaMemoryStore(MemoryStore):
    def __init__(self):
        self.client = chromadb.Client()
        self.collection = self.client.create_collection("recallgpt")

    def add(self, content: str, embedding: list):
        self.collection.add(documents=[content], embeddings=[embedding])

    def search(self, query: str):
        # For demo: return last 5 documents
        results = self.collection.get(limit=5)
        return [{"content": doc} for doc in results["documents"]]
