from fastapi import FastAPI, File, UploadFile, Form
from fastapi.middleware.cors import CORSMiddleware
from fastapi.responses import JSONResponse
import pandas as pd
from data_processing import preprocess_df, create_sequences
from model import train_model, predict
import numpy as np

app = FastAPI()
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

model = None
scaler = None
seq_len = 30
features = ['Close', 'SMA_10', 'SMA_20', 'EMA_10', 'RSI_14']

@app.post("/train")
async def train(file: UploadFile = File(...)):
    df = pd.read_csv(file.file)
    df, scaler_local = preprocess_df(df)
    X, y = create_sequences(df[features], seq_len)
    split = int(0.8 * len(X))
    X_train, X_val = X[:split], X[split:]
    y_train, y_val = y[:split], y[split:]
    global model, scaler
    scaler = scaler_local
    model, history = train_model(X_train, y_train, X_val, y_val, epochs=30)
    return {"message": "Model trained", "val_mae": float(history.history['val_mae'][-1])}

@app.post("/predict")
async def get_predictions(file: UploadFile = File(...)):
    df = pd.read_csv(file.file)
    df, _ = preprocess_df(df)
    X, y = create_sequences(df[features], seq_len)
    preds = predict(model, X)
    # Unscale predictions for output
    close_min = scaler.data_min_[0]
    close_max = scaler.data_max_[0]
    preds_unscaled = preds * (close_max - close_min) + close_min
    actuals_unscaled = y * (close_max - close_min) + close_min
    dates = df['Date'].values[seq_len:]
    return JSONResponse({
        "dates": dates.tolist(),
        "predicted": preds_unscaled.flatten().tolist(),
        "actual": actuals_unscaled.flatten().tolist(),
        "insights": generate_insights(preds_unscaled, actuals_unscaled)
    })

def generate_insights(preds, actuals):
    # Simple trading signals: Buy if next predicted > actual, Sell if < actual
    signals = []
    for p, a in zip(preds, actuals):
        if p > a:
            signals.append("Buy")
        elif p < a:
            signals.append("Sell")
        else:
            signals.append("Hold")
    return signals