### Para esta parte de la práctica teneis que generar un script con al menos 5 modulos app.get y dos de ellos tienen que ser pipelines de HF. 
from transformers import pipeline
@appget("/sentiment")
def sentiment_analysis(text: str):
    sentiment = pipeline("sentiment-analysis")
    