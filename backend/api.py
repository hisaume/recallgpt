from fastapi import APIRouter, Request
from .db import get_logs, add_log
from .memory import get_relevant_context
import openai
import os

router = APIRouter()

@router.post("/chat")
async def chat(request: Request):
    data = await request.json()
    user_input = data.get("input")
    # Retrieve relevant context from memory
    context = get_relevant_context(user_input)
    # Call OpenAI API
    openai.api_key = os.getenv("OPENAI_API_KEY")
    response = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=[{"role": "system", "content": context}, {"role": "user", "content": user_input}]
    )
    ai_response = response.choices[0].message["content"]
    # Log interaction
    add_log(user_input, ai_response)
    return {"response": ai_response, "context": context}
