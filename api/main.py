from fastapi import FastAPI, HTTPException
import pandas as pd

from api.model_loader import load_model_from_s3
from api.schemas import PredictionRequest


app = FastAPI(
    title="Shipment Price Prediction API",
    description="API for predicting shipment cost",
    version="1.0.0"
)


# Load model when API starts
model = load_model_from_s3()


@app.get("/")
def home():

    return {
        "message": "Shipment Price Prediction API is running"
    }


@app.get("/health")
def health():

    return {
        "status": "healthy",
        "model_loaded": model is not None
    }


@app.post("/predict")
def predict(request: PredictionRequest):

    try:

        # Convert JSON to DataFrame
        input_data = pd.DataFrame([request.data])

        # Make prediction
        prediction = model.predict(input_data)

        return {
            "prediction": float(prediction[0])
        }

    except Exception as e:

        raise HTTPException(
            status_code=500,
            detail=str(e)
        )