import sqlite3
from datetime import datetime
import os

DB_PATH = os.path.abspath(os.path.join(os.path.dirname(__file__), "../recallgpt.db"))

def get_logs(limit=10):
    conn = sqlite3.connect(DB_PATH)
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM logs ORDER BY timestamp DESC LIMIT ?", (limit,))
    logs = cursor.fetchall()
    conn.close()
    return logs

def add_log(user_input, ai_response):
    conn = sqlite3.connect(DB_PATH)
    cursor = conn.cursor()
    cursor.execute("INSERT INTO logs (timestamp, user_input, ai_response) VALUES (?, ?, ?)",
                   (datetime.utcnow(), user_input, ai_response))
    conn.commit()
    conn.close()
