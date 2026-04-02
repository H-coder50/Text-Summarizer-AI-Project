
from fastapi import FastAPI
from pydantic import BaseModel
import requests

app = FastAPI()

class TextRequest(BaseModel):
    text: str

@app.post("/summarize/")
def summarize(request: TextRequest):
    response = requests.post(
        "http://localhost:11434/api/generate",
        json={
            "model": "llama3",
            "prompt": f"Summarize this:\n\n{request.text}",
            "stream": False
        }
    )
    result = response.json()
    return {"summary": result.get("response", "No response")}