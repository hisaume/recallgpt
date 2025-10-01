# Backend: FastAPI App

This folder contains the FastAPI backend for RecallGPT.

## Setup
1. Create a Python virtual environment:
   python3 -m venv venv
2. Activate the environment:
   source venv/bin/activate
3. Install dependencies:
   pip install fastapi uvicorn chromadb sqlite3 openai
4. Run the server:
   uvicorn main:app --reload

## Files
- main.py: FastAPI app entry point
- db.py: SQLite database logic
- api.py: API endpoints
- memory.py: MemoryStore integration

---
See README.md in project root for overall architecture.