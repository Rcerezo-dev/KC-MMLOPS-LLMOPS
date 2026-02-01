# KC-MMLOPS-LLMOPS

Esta práctica está hecha para el módulo de KeepCoding **"MLOPS - LLMOPS"**.

Hay dos partes muy diferenciadas en el proyecto:

---

##  Parte 1. Modelos NLP y MLflow

Por un lado, introduzco dos modelos que ya creé en el módulo de NLP dentro de MLflow, con el objetivo de registrar sus métricas y parámetros.

Los resultados pueden observarse mediante capturas de pantalla en la carpeta **Capturas MLFLOW**.

La idea de esta práctica no es repetir todo el proceso de creación del modelo, ya que se realizó en un módulo anterior.  
No obstante, el proceso completo puede consultarse en el siguiente repositorio:

🔗 https://github.com/Rcerezo-dev/NLP

Para entender esta parte, es importante revisar los siguientes archivos:

- **1. Exploración_de_datos.ipynb**
- **2. Preprocesado.ipynb**
- **3. Uso_de_mlflow.ipynb**
- **Capturas MLFLOW/** (carpeta)

---

##  Parte 2. FastAPI

En la segunda parte de la práctica se requería crear **5 funciones** y convertirlas en **endpoints de FastAPI**.

Para revisar esta parte del proyecto, deben consultarse:

- **4. script.py**
- **Capturas FastAPI/**

---

##  Estructura del proyecto

Dentro del repositorio se encuentran los siguientes archivos:
## Estructura del proyecto

```text
KC-MMLOPS-LLMOPS/
│
├── 1.Exploración_de_datos.ipynb
├── 2.Preprocesado.ipynb
├── 3.Uso_de_mlflow.ipynb
├── 4.script.py
│
├── conda.yaml
├── mlflow.db
├── requirements.txt
├── README.md
│
├── reviews_Video_Games_5_balanced_preprocessed.csv
├── reviews_Video_Games_5_balanced_preprocessed_0-1.csv
│
├── .vscode/
│   └── settings.json
│
├── Capturas FastAPI/
│   ├── calculadora.jpg
│   ├── captura IMC.jpg
│   ├── cifrado césar.jpg
│   ├── Entrada.jpg
│   ├── Generate-text.jpg
│   ├── health.jpg
│   ├── info.jpg
│   ├── Main menu.jpg
│   └── Sentiment.jpg
│
├── Capturas MLFLOW/
│   ├── Captura comparativa metrics.jpg
│   ├── captura pantalla models.jpg
│   ├── Captura run 1.jpg
│   ├── Captura run 2.jpg
│   └── captura runs.jpg
│
├── mlartifacts/
│   └── 1/
│       ├── <run_id>/
│       │   └── artifacts/
│       │       └── vectorizer/
│       │           └── vectorizer.pkl
│       └── models/
│           └── <model_id>/
│               └── artifacts/
│                   ├── model.pkl
│                   ├── MLmodel
│                   ├── conda.yaml
│                   ├── python_env.yaml
│                   └── requirements.txt
│
├── modelos/
│   ├── Logistic_regression_tf_idf0-1/
│   │   ├── model.pkl
│   │   ├── vectorizer.pkl
│   │   ├── test_data.pkl
│   │   └── archivo_dummy.py
│   │
│   └── Logistic_regression_tf_idf0-5/
│       ├── model.pkl
│       ├── vectorizer.pkl
│       ├── test_data.pkl
│       └── archivo_dummy.py
│
└── __pycache__/
    ├── intro_fastapi.cpython-310.pyc
    └── script.cpython-311.pyc
```
