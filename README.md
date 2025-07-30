# Tech Challenge – Fase 4: LSTM Stock Price Predictor (CASH3)

This project creates a predictive model using neural network LSTM to predict the closing values of the stock CASH3, based on its last 60 days. The prediction is done through an API REST with FastAPI, packed on a Docker container.

---

## Libraries Used

- Python 3.10
- TensorFlow / Keras
- yfinance
- FastAPI
- Docker
- Jupyter Notebook

---

## Project Structure

```text
challenge_fase4/
├── app/
│   ├── model/
│   │   └── lstm_model.keras         # Trained model
│   └── predict_api.py               # FastAPI app
├── notebooks/
│   ├── cash3_lstm_model.ipynb       # Main notebook
│   └── cash3_lstm_model_30day_test.ipynb  # Bonus experiment
├── dashboard.py                     # Optional Streamlit app
├── test_predict.py                  # API test script
├── Dockerfile
├── requirements.txt
└── README.md
```

---

## How to Execute

### Locally (without Docker)

Run on terminal:
```bash
pip install -r requirements.txt
uvicorn app.predict_api:app --reload
```
- Access: http://localhost:8000/docs

### With Docker

Run on terminal:
```bash
docker build -t cash3-api .
docker run -p 8000:8000 cash3-api
```

## How to use the API

Input the record of the last 60 days closing value, or you can use the random generator on notebook cash3_lstm_model.ipynb

## Interactive interface (extra - not included on Docker)

A simple streamlit page was created to make the trials more user friendly. Like with the API, you have to input a 60-day value historic to calculate a predicted closing price.
Run on terminal:
```bash
streamlit run dashboard.py
```
