import unittest
from unittest.mock import patch, MagicMock
from memory.chroma_store import ChromaMemoryStore

class TestChromaMemoryStore(unittest.TestCase):

    @patch("memory.chroma_store.openai.Embedding.create")
    def test_generate_embedding(self, mock_openai_embedding):
        # Mock OpenAI API response
        mock_openai_embedding.return_value = {
            'data': [{'embedding': [0.1, 0.2, 0.3]}]
        }

        store = ChromaMemoryStore()
        text = "Test input"
        embedding = store.generate_embedding(text)

        # Assertions
        mock_openai_embedding.assert_called_once_with(input=text, model="text-embedding-ada-002")
        self.assertEqual(embedding, [0.1, 0.2, 0.3])

    @patch("memory.chroma_store.chromadb.Client")
    def test_add(self, mock_chroma_client):
        # Mock Chroma collection
        mock_collection = MagicMock()
        mock_chroma_client.return_value.create_collection.return_value = mock_collection

        store = ChromaMemoryStore()
        content = "Test content"
        embedding = [0.1, 0.2, 0.3]
        store.add(content, embedding)

        # Assertions
        mock_collection.add.assert_called_once_with(documents=[content], embeddings=[embedding])

    @patch("memory.chroma_store.openai.Embedding.create")
    @patch("memory.chroma_store.chromadb.Client")
    def test_search(self, mock_chroma_client, mock_openai_embedding):
        # Mock OpenAI API response
        mock_openai_embedding.return_value = {
            'data': [{'embedding': [0.1, 0.2, 0.3]}]
        }

        # Mock Chroma collection
        mock_collection = MagicMock()
        mock_collection.query.return_value = {
            "documents": ["Result 1", "Result 2"]
        }
        mock_chroma_client.return_value.create_collection.return_value = mock_collection

        store = ChromaMemoryStore()
        query = "Test query"
        results = store.search(query)

        # Assertions
        mock_openai_embedding.assert_called_once_with(input=query, model="text-embedding-ada-002")
        mock_collection.query.assert_called_once_with(query_embeddings=[[0.1, 0.2, 0.3]], n_results=5)
        self.assertEqual(results, [{"content": "Result 1"}, {"content": "Result 2"}])

if __name__ == "__main__":
    unittest.main()