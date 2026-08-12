from fastapi import FastAPI

app = FastAPI(
    title="ALEX",
    description="Agentic AI Medical Research Assistant",
    version="0.1.0"
)


@app.get("/")
def home():
    return {
        "assistant": "ALEX",
        "status": "online",
        "message": "Hello Sir, how can I help you?"
    }