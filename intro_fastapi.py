from fastapi import FastAPI
from transformers import pipeline
import torch

# Inicializamos la app
app = FastAPI(title="HF + FastAPI Demo")

# Pipelines de Hugging Face )
sentiment_classifier = pipeline(
    "sentiment-analysis",
    model="distilbert-base-uncased-finetuned-sst-2-english"
)

text_generator = pipeline(
    "text-generation",
    model="gpt2"
)


@app.get("/entrada")
def home():
    return {"message": "API funcionando correctamente"}

@app.get("/health")
def health_check():
    return {"status": "ok"}

@app.get("/info")
def info():
    return {
        "framework": "FastAPI",
        "pipelines": 2,
        "endpoints": 5
    }

# ---- HF PIPELINE 1 ----
@app.get("/sentiment")
def sentiment_analysis(text: str):
    result = sentiment_classifier(text)[0]
    return {
        "label": result["label"],
        "score": result["score"]
    }

# ---- HF PIPELINE 2 ----
@app.get("/generate-text")
def generate_text(prompt: str):
    result = text_generator(prompt, max_length=50)
    return {
        "generated_text": result[0]["generated_text"]
    }
@app.get("/")
def entrada():
    return {"message": "API funcionando correctamente"}

@app.get("/health")
def health():
    return {"status": "ok"}

@app.get("/info")
def info():
    return {
        "framework": "FastAPI",
        "pipelines": 2,
        "endpoints": 5
    }

# ---------- PIPELINES HF ----------

# Pipeline 1: Sentiment Analysis (ligero, estable)
sentiment_pipeline = pipeline(
    "sentiment-analysis",
    model="distilbert-base-uncased-finetuned-sst-2-english"
)

@app.get("/sentiment")
def sentiment(text: str):
    result = sentiment_pipeline(text)[0]
    return {
        "label": result["label"],
        "score": result["score"]
    }

# Pipeline 2: Text Generation (modelo ligero)
text_generator = pipeline(
    "text-generation",
    model="distilgpt2"
)

@app.get("/generate-text")
def generate_text(prompt: str):
    result = text_generator(prompt, max_length=40)
    return {
        "generated_text": result[0]["generated_text"]
    }