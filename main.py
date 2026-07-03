from fastapi import FastAPI, Request
from fastapi.middleware.cors import CORSMiddleware
from fastapi.responses import HTMLResponse
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates

app = FastAPI(title="asATLASAI")

# CORS
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Static dosyalar
app.mount("/static", StaticFiles(directory="static"), name="static")

# HTML şablonları
templates = Jinja2Templates(directory="templates")


# Ana sayfa
@app.get("/", response_class=HTMLResponse)
async def home(request: Request):
    return templates.TemplateResponse(
        "index.html",
        {"request": request}
    )


# Sohbet API
@app.post("/chat")
async def chat():
    return {
        "response": "Merhaba Süleyman 👋 Ben asATLASAI. Artık canlı çalışıyorum! 🚀"
    }


# Sağlık kontrolü
@app.get("/health")
async def health():
    return {
        "status": "online",
        "ai": "asATLASAI",
        "version": "1.0.0"
    }
