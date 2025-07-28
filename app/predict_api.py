from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
import numpy as np
import tensorflow as tf
from sklearn.preprocessing import MinMaxScaler

# model load
model = tf.keras.models.load_model('app/model/lstm_model.keras')

# initialize
app = FastAPI(title="CASH3 Price Predictor")

class PriceSequence(BaseModel):
    prices: list[float]

scaler = MinMaxScaler()
scaler.min_, scaler.scale_ = 0, 1

@app.post("/predict")
def predict_price(data: PriceSequence):
    if len(data.prices) != 60:
        raise HTTPException(status_code=400, detail="Input must contain exactly 60 closing prices.")
    
    input_data = np.array(data.prices).reshape(-1, 1)
    scaled = scaler.fit_transform(input_data)

    X = scaled.reshape(1, 60, 1)
    prediction = model.predict(X)

    predicted_price = scaler.inverse_transform(prediction)[0][0]

    return {"predicted_price": float(predicted_price)}
