import streamlit as st
import numpy as np
import tensorflow as tf
from sklearn.preprocessing import MinMaxScaler

# Load model
model = tf.keras.models.load_model('app/model/lstm_model.keras')

st.title("Predicted CASH3 Value")
st.write("Input the **last 60 closing prices** to predict future closing value.")

# Input prices
prices_input = st.text_area("Input the 60-day historic, with numers separated by comma, and decimals by dot:")

if st.button("Predict"):
    try:
        prices = [float(p.strip()) for p in prices_input.split(',')]
        if len(prices) != 60:
            st.error("You must give 60 numbers for prediction.")
        else:
            # Scale and reshape
            scaler = MinMaxScaler()
            input_scaled = scaler.fit_transform(np.array(prices).reshape(-1, 1))
            X = input_scaled.reshape(1, 60, 1)

            # Predict
            prediction = model.predict(X)
            predicted_price = scaler.inverse_transform(prediction)[0][0]

            st.success(f"Predicted price: **R${predicted_price:.2f}**")
    except Exception as e:
        st.error(f"Error processing: {e}")
