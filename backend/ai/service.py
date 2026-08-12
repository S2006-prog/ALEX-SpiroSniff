class AIService:
    def __init__(self):
        self.name = "ALEX AI"

    def generate_response(self, message: str) -> str:
        return f"ALEX received: {message}"