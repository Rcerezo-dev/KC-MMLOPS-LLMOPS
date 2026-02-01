import torch
from fastapi import FastAPI
from transformers import pipeline
from typing import List
from fastapi import HTTPException

app = FastAPI(title="FastAPI + Hugging Face API")
tts_pipe = None

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

@app.post("/calculadora")
def calculadora(
    operacion: str,
    numeros: List[float]
):
    if operacion == "suma":
        return sum(numeros)
    elif operacion == "resta":
        resultado = numeros[0]
        for n in numeros[1:]:
            resultado -= n
        return resultado
    elif operacion == "multiplicacion":
        resultado = 1
        for n in numeros:
            resultado *= n
        return resultado
    elif operacion == "division":
        resultado = numeros[0]
        for n in numeros[1:]:
            if n == 0:
                return {"error": "División por cero"}
            resultado /= n
        return resultado
    else:
        return {"error": "Operación no válida"}

@app.get("/IMC")
def calcular_imc(peso: float, altura: float):
    """
    Calcula el Índice de Masa Corporal (IMC).
    """
    if altura <= 0:
        raise HTTPException(status_code=400, detail="La altura debe ser mayor que cero.")

    imc = peso / (altura ** 2)
    return {"IMC": imc}