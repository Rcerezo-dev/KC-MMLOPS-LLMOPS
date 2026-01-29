from fastapi import FastAPI
import pandas as pd 
app = FastAPI()

@app.get('/saluda')
def return_name(name, surname): 
    return {'Message': f'Hola mi nombre es {name}'}

@app.get('/patata')
def read_dataframe(): 
    df = pd.read_csv('https://raw.githubusercontent.com/mwaskom/seaborn-data/master/iris.csv')
    return {'Values': df}

@app.get('/read_sepal_lenght_positon')
def read_sepal_length(position: int):
    print(position)
    print(type(position))
    df = pd.read_csv('https://raw.githubusercontent.com/mwaskom/seaborn-data/master/iris.csv')
    value = df['sepal_length'][position]
    return {'Value': value}

from transformers import pipeline


@app.get('/text-classification')
def text_classification(text: str):
    pipe = pipeline("text-classification")
    response =  pipe(text)
    if response[0]['score'] > 0.8: 
        sentiment = 'positive'
    else: 
        sentiment = 'negative'
    return {'Value': sentiment}



