from fastapi import FastAPI
import pandas as pd
from app.model import load_data
from app.schema import Cardio

# app = FastAPI ()

# @app.get('/')
# def home():
#     return 'welcome'

app = FastAPI()
 
model, scaler = load_data()

@app.get('/')
def home():
    return 'Welcome to Cardiovascular Disease Prediction Application'

@app.post('/predict-cardio')
def predict(data:Cardio):
    input_data = pd.DataFrame([
        data.model_dump()
    ])
    input_scaler = scaler.transform(input_data)
    prediction = model.predict(input_scaler)[0]
    return{
        'Prediction_Status': int(prediction),
        'Status':'Likely to be healthy'if prediction == 0 else'Likely to be unhealthy'
    }