
import os
from fastapi import FastAPI
from fastapi.staticfiles import StaticFiles
from . import api

app = FastAPI()

# Use absolute path for frontend directory
frontend_path = os.path.abspath(os.path.join(os.path.dirname(__file__), "../frontend"))
app.mount("/static", StaticFiles(directory=frontend_path), name="static")

# Include API routes
app.include_router(api.router)

# Root endpoint
@app.get("/")
def read_root():
    return {"message": "RecallGPT backend is running."}
