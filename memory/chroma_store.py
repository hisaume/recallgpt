from .memory_store import MemoryStore
import chromadb
import openai

class ChromaMemoryStore(MemoryStore):
    def __init__(self):
        self.client = chromadb.Client()
        self.collection = self.client.create_collection("recallgpt")

    def add(self, content: str, embedding: list):
        # Store content and its embedding in the Chroma collection
        self.collection.add(documents=[content], embeddings=[embedding])

    def generate_embedding(self, text: str) -> list:
        """
        Generate an embedding for the given text using OpenAI's embeddings API.
        """
        response = openai.Embedding.create(
            input=text,
            model="text-embedding-ada-002"  # Example embedding model
        )
        return response['data'][0]['embedding']

    def search(self, query: str):
        # Generate embedding for the query
        query_embedding = self.generate_embedding(query)

        # Perform a vector search in the Chroma collection
        results = self.collection.query(query_embeddings=[query_embedding], n_results=5)

        # Return the top results
        return [{"content": doc} for doc in results["documents"]]
