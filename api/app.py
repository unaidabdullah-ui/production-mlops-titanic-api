from fastapi import FastAPI
import joblib
import pandas as pd

app = FastAPI()

model = joblib.load("model/model.pkl")  

@app.get("/")
def home():
    return {"message": "Welcome to the Titanic Survival Prediction API!"}


@app.post("/predict")
def predict(data:dict):
    df = pd.DataFrame([data])
    prediction = model.predict(df)
    return {"prediction": int(prediction[0])}
