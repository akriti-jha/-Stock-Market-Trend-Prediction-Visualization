import pandas as pd
import numpy as np
from sklearn.preprocessing import MinMaxScaler

def add_indicators(df):
    df['SMA_10'] = df['Close'].rolling(window=10).mean()
    df['SMA_20'] = df['Close'].rolling(window=20).mean()
    df['EMA_10'] = df['Close'].ewm(span=10, adjust=False).mean()
    df['RSI_14'] = compute_rsi(df['Close'], 14)
    df.fillna(0, inplace=True)
    return df

def compute_rsi(series, period=14):
    delta = series.diff()
    gain = delta.clip(lower=0).rolling(window=period).mean()
    loss = -delta.clip(upper=0).rolling(window=period).mean()
    rs = gain / (loss + 1e-9)
    rsi = 100 - (100 / (1 + rs))
    return rsi

def preprocess_df(df):
    df = add_indicators(df)
    scaler = MinMaxScaler()
    features = ['Close', 'SMA_10', 'SMA_20', 'EMA_10', 'RSI_14']
    df[features] = scaler.fit_transform(df[features])
    return df, scaler

def create_sequences(df, seq_len=30):
    data = df.values
    X = []
    y = []
    for i in range(seq_len, len(data)):
        X.append(data[i-seq_len:i])
        y.append(data[i, 0])  # Predicting 'Close'
    X, y = np.array(X), np.array(y)
    return X, y