from fastapi import FastAPI
from pydantic import BaseModel
import joblib
import pandas as pd

# Create FastAPI application
app = FastAPI()

# Load trained model
model = joblib.load("model.pkl")


# Input schema
class InputData(BaseModel):
    feature1: float
    feature2: float


# Home endpoint
@app.get("/")
def home():
    return {
        "message": "Linear Regression API is running"
    }


# Prediction endpoint
@app.post("/predict")
def predict(data: InputData):

    # Convert input object to DataFrame
    input_df = pd.DataFrame([data.model_dump()])

    # Predict
    prediction = model.predict(input_df)

    # Return result
    return {
        "input": data.model_dump(),
        "prediction": prediction[0]
    }