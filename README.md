# RecallGPT

RecallGPT is a lightweight app that layers persistent, curated memory onto ChatGPT. It logs interactions, stores embeddings, and retrieves relevant context to improve continuity and relevance.

## Architecture
- **Backend:** Python (FastAPI)
- **Frontend:** Static HTML/CSS/JS served by backend
- **Database:** SQLite for logs
- **Vector Store:** Chroma for embeddings

## Folder Structure
- `backend/` — FastAPI app, REST endpoints, database logic
- `frontend/` — HTML, CSS, JS files
- `memory/` — MemoryStore abstraction, Chroma integration

## Data Flow
1. User input sent from frontend to backend
2. Backend queries memory (SQLite + Chroma)
3. Relevant logs/context retrieved
4. OpenAI API called for reasoning
5. Response returned to frontend
6. User input, AI response, and embedding stored in database

## Setup Instructions
1. Install Python 3.x and Node.js (if needed for frontend tooling)
2. Create a Python virtual environment in `backend/`
3. Install dependencies (FastAPI, Chroma, SQLite, OpenAI)
4. Run backend server
5. Access frontend via backend server

## No authentication included during the proof-of-concept. Manual local development only.

---
For detailed setup and usage, see instructions in each folder.