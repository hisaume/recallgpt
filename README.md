# RecallGPT

This project is intended for building, experimenting and testing the database, to be used in other LLM apps upon completion.

RecallGPT is a lightweight app that layers persistent, curated memory onto ChatGPT. It logs interactions, stores embeddings, and retrieves relevant context to improve continuity and relevance.

## Technology
- **Backend:** Python (FastAPI)
- **Database:** SQLite for logs
- **Vector Store:** Chroma for embeddings
- The placeholder frontend: A static web page served by backend

## Main Data Flow
Backend queries memory (SQLite + Chroma), Relevant logs/context retrieved
(interact with )OpenAI API for a response), User input, AI response, and embedding stored in database

