from fastapi import FastAPI
from backend.ai.service import AIService

app = FastAPI(
    title="ALEX",
    description="Agentic AI Medical Research Assistant",
    version="0.2.0"
)

ai = AIService()


@app.get("/")
def home():
    return {
        "assistant": "ALEX",
        "status": "online",
        "message": "Hello Sir, how can I help you?"
    }


@app.get("/chat")
def chat(message: str):
    response = ai.generate_response(message)

    return {
        "assistant": "ALEX",
        "user_message": message,
        "response": response
    }