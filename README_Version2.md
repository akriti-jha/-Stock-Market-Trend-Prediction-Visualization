# Stock Market Trend Prediction & Visualization

Stock Market Trend Prediction & Visualization uses deep learning (LSTM) and financial indicators to forecast stock prices from CSV data. It features an interactive dashboard with real-time charts and actionable trading signals for smarter investment decisions.

---

## 🖼️ Dashboard Preview

Below are some screenshots of the dashboard UI:

### Stock Search & Watchlist
![Stock Search & Watchlist](images/dashboard-1.png)

### Stock Details, Chart, RSI, MACD
![Stock Details, Chart, RSI, MACD](images/dashboard-2.png)

### Indicators, Moving Averages & Trading Signals
![Indicators, Moving Averages & Trading Signals](images/dashboard-3.png)

### Full Dashboard View
![Full Dashboard](images/dashboard-4.png)

---

## Features

- **Data Processing:** Computes SMA, EMA, RSI indicators from raw stock CSVs.
- **Sequential Prediction:** Trains an LSTM (TensorFlow) model for time series forecasting.
- **Interactive Visualization:** React frontend displays actual vs. predicted prices, plus trading signals.
- **Actionable Insights:** "Buy", "Sell", "Hold" signals based on model predictions.

---

## Project Structure

```
stock-market-predictor/
├── backend/
├── frontend/
├── docker-compose.yml
└── README.md
```

---

## Setup & Usage

1. **Clone the repo:**
   ```sh
   git clone https://github.com/akriti-jha/stock-market-predictor.git
   cd stock-market-predictor
   ```

2. **Prepare data:**  
   Use CSV files with columns: `Date, Open, High, Low, Close, Volume`.

3. **Run with Docker Compose:**
   ```sh
   docker-compose up --build
   ```
   - **Backend:** FastAPI, available at `http://localhost:8000`
   - **Frontend:** React app, available at `http://localhost:3000`

4. **Usage Steps:**
   - Upload your stock CSV file in the frontend.
   - Click "Train Model" (wait for success alert).
   - Click "Predict & Visualize" to see results.

5. **Manual Backend/Frontend Setup:**
   - **Backend:**
     ```sh
     cd backend
     pip install -r requirements.txt
     uvicorn main:app --reload
     ```
   - **Frontend:**
     ```sh
     cd frontend
     npm install
     npm start
     ```

---

## Customization

- Add more indicators in `data_processing.py` as needed.
- Adjust LSTM layers in `model.py` for experimentation.

---

## License

MIT

---

> **Note:** This project is for educational and research purposes only. Always do your own due diligence before making investment decisions.