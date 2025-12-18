import streamlit as st
import pickle
import numpy as np

# Load model
with open("model.pkl", "rb") as file:
    LR = pickle.load(file)

st.set_page_config(page_title="Car Price Prediction", layout="centered")

st.title("🚗 Car Price Prediction App")
st.write("Enter car details to predict selling price")

# -------- INPUTS --------
Year = st.number_input("Year", min_value=1990, max_value=2025, step=1)
Present_Price = st.number_input("Present Price (in lakhs)", min_value=0.0)
Kms_Driven = st.number_input("Kms Driven", min_value=0)

Fuel_Type = st.selectbox("Fuel Type", ["Petrol", "Diesel"])
Seller_Type = st.selectbox("Seller Type", ["Dealer", "Individual"])
Transmission = st.selectbox("Transmission", ["Manual", "Automatic"])

# -------- ENCODING (must match training) --------
Fuel_Type = 0 if Fuel_Type == "Petrol" else 1
Seller_Type = 0 if Seller_Type == "Dealer" else 1
Transmission = 0 if Transmission == "Manual" else 1

# -------- PREDICTION --------
if st.button("Predict Price"):
    input_data = np.array([[Year, Present_Price, Kms_Driven,
                            Fuel_Type, Seller_Type, Transmission]])

    prediction = LR.predict(input_data)

    st.success(f"💰 Estimated Car Price: ₹ {prediction[0]:.2f} lakhs")
