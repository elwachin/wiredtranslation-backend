from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from fastapi.middleware.cors import CORSMiddleware

from app.translation import translate_text, to_jeringoza

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # Frontend dev server
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

class TranslationRequest(BaseModel):
    text: str
    target_language: str

@app.post("/translate")
def translate(request: TranslationRequest):
    if request.text.strip().lower() != "hello. how are you?":
        raise HTTPException(status_code=400, detail="Only 'Hello. How are you?' is supported.")
    
    translation = translate_text(request.text, request.target_language)
    if translation is None:
        raise HTTPException(status_code=400, detail="Unsupported language.")
    
    return {"translation": translation}

@app.post("/jeringoza")
def jeringoza(request: TranslationRequest):
    return {"translation": to_jeringoza(request.text)}
