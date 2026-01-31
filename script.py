import torch
from fastapi import FastAPI
from transformers import pipeline
from typing import List

app = FastAPI(title="FastAPI + Hugging Face Practice")
tts_pipe = None

@app.on_event("startup")
def load_model():
    global tts_pipe
    tts_pipe = pipeline("text-to-speech", model="suno/bark-small")
# -------------------------
# PIPELINES HUGGING FACE
# -------------------------

sentiment_pipeline = pipeline(
    "sentiment-analysis",
    model="distilbert-base-uncased-finetuned-sst-2-english"
)

text_generator = pipeline(
    "text-generation",
    model="distilgpt2"
)

@app.get("/tts")
def text_to_speech(text: str):
    output = tts_pipe(text)

    audio = output["audio"]
    sampling_rate = output["sampling_rate"]

    audio_bytes = (audio * 32767).astype(np.int16).tobytes()

    return Response(
        content=audio_bytes,
        media_type="audio/wav"
    )

# -------------------------
# ENDPOINTS SIMPLES
# -------------------------

@app.get("/")
def root():
    return {"message": "API funcionando correctamente"}

@app.get("/health")
def health():
    return {"status": "ok"}

@app.get("/info")
def info():
    return {
        "framework": "FastAPI",
        "endpoints": 5,
        "hf_pipelines": 2
    }

# -------------------------
# ENDPOINTS HUGGING FACE
# -------------------------

@app.get("/sentiment")
def sentiment_analysis(text: str):
    """
    Analiza el sentimiento de un texto.
    """
    return sentiment_pipeline(text)[0]

@app.get("/generate-text")
def generate_text(prompt: str):
    """
    Genera texto a partir de un prompt.
    """
    result = text_generator(prompt, max_length=40)
    return {"generated_text": result[0]["generated_text"]}

# -------------------------
# ENDPOINT LÓGICO (PYTHON)
# -------------------------

@app.get("/cesar-cipher")
def cesar_cipher(mensaje: str, clave: int):
    """
    Aplica cifrado César a un mensaje.
    """
    resultado = ""

    for caracter in mensaje:
        if caracter.isalpha():
            base = ord("a") if caracter.islower() else ord("A")
            resultado += chr((ord(caracter) - base + clave) % 26 + base)
        else:
            resultado += caracter

    return {"resultado": resultado}
