from memory.chroma_store import ChromaMemoryStore

# Initialize Chroma memory store
chroma = ChromaMemoryStore()

def get_relevant_context(query):
    # Embed query and search for relevant logs
    results = chroma.search(query)
    # Combine results into context string
    context = "\n".join([r["content"] for r in results])
    return context
