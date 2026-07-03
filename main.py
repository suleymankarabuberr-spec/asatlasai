from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_methods=["*"],
    allow_headers=["*"],
)
@app.get("/")
def home():
    return {
        "name": "asATLASAI",
        "status": "online",
        "message": "Merhaba! asATLASAI çalışıyor. 🚀"
    }
@app.post("/chat")
def chat():
    return {"response": "asATLASAI canlıda çalışıyor 🚀"}
