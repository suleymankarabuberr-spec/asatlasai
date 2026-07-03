from fastapi import FastAPI
from fastapi.responses import FileResponse
from fastapi.staticfiles import StaticFiles
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI(title="asATLASAI")

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.mount("/static", StaticFiles(directory="static"), name="static")


@app.get("/")
async def home():
    return FileResponse("templates/index.html")


@app.post("/chat")
async def chat():
    return {
        "response": "Merhaba! Ben asATLASAI 🚀 Yakında GPT destekli gerçek yapay zekâ olarak hizmet vereceğim."
    }


@app.get("/health")
async def health():
    return {
        "status": "online"
    }
