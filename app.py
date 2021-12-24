import uvicorn
from fastapi import FastAPI

import numpy as np
import pickle
import pandas as pd

import format

app = FastAPI()

diabetes_classifier=pickle.load(open("models/diabetes_classifier.pkl","rb"))
diabetes_scaler=pickle.load(open("scalers/diabetes_scaler.pkl","rb"))

@app.get('/')
def index():
    return {'message': 'Hello, World'}


@app.post('/predict/diabetes')
def predict_diabetes(data:format.diabetes):
    data = data.dict()
    
    input_data = (data['pregnancies'], 
    data['glucose'], 
    data['bloodPressure'], 
    data['skinThickness'], 
    data['insulin'], 
    data['bmi'], 
    data['diabetesPedigreeFunction'], 
    data['age'])

    input_data = np.asarray(input_data)

    input_data = input_data.reshape(1, -1)
    
    input_data = diabetes_scaler.transform(input_data)

    prediction = diabetes_classifier.predict(input_data)

    print(prediction)

    if(prediction == 0): prediction="Not diabetic"
    else: prediction="Diabetic"
    
    return {
        'prediction': prediction
    }


if __name__ == '__main__':
    uvicorn.run(app, host='127.0.0.1', port=8000)
    #uvicorn app:app --reload