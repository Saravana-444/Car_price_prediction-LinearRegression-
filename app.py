import streamlit as st
import pickle
import numpy as np

# -------------------------------
# Load trained model
# -------------------------------
with open("LR.pkl", "rb") as file:
    LR = pickle.load(file)

st.set_page_config(page_title="Prediction App", layout="centered")

st.title("🚗 Prediction App")
st.write("Enter input values to get prediction")

# -------------------------------
# INPUTS (change based on dataset)
# Example: Car Price Prediction
# -------------------------------
feature1 = st.number_input("Year", min_value=0.0)
feature2 = st.number_input("Present_Price", min_value=0.0)
feature3 = st.number_input("Kms_Driven", min_value=0.0)
feature4 = st.number_input("Owner", min_value=0.0)

# -------------------------------
# Prediction
# -------------------------------
if st.button("Predict"):
    input_data = np.array([[Year, Present_Price, Kms_Driven, Owner]])
    prediction = model.predict(input_data)

    st.success(f"Predicted Value: {prediction[0]:.2f}")
