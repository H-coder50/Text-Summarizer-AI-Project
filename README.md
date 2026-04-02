# LLaMA Text Summarizer

This project is a simple AI application that uses a locally hosted LLaMA model (via Ollama) to summarize text.

## Features
- FastAPI backend
- Streamlit frontend
- Local LLaMA inference using Ollama

## Setup Instructions
1. Clone the repository
2. Install dependencies:
   pip install -r requirements.txt
3. Start backend:
   uvicorn backend.main:app --reload
4. Start frontend:
   streamlit run frontend/app.py
