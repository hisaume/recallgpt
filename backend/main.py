
import os
from fastapi import FastAPI
from fastapi.staticfiles import StaticFiles
from . import api

import sqlite3

app = FastAPI()

# Initialize SQLite database and create logs table if needed
DB_PATH = os.path.abspath(os.path.join(os.path.dirname(__file__), "../recallgpt.db"))
conn = sqlite3.connect(DB_PATH)
cursor = conn.cursor()
cursor.execute("""
CREATE TABLE IF NOT EXISTS logs (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    timestamp TEXT,
    user_input TEXT,
    ai_response TEXT
)
""")
conn.commit()
conn.close()

# Mount frontend static files
#app.mount("/static", StaticFiles(directory="../frontend"), name="static")
# Absolute path
frontend_path = os.path.abspath(os.path.join(os.path.dirname(__file__), "../frontend"))
app.mount("/static", StaticFiles(directory=frontend_path), name="static")

# Include API routes
app.include_router(api.router)

# Root endpoint
@app.get("/")
def read_root():
    return {"message": "RecallGPT backend is running."}
