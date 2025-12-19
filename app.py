import streamlit as st
import pickle
import numpy as np

st.title("🚗 Car Price Prediction")

# Load model
with open("LR (1).pkl", "rb") as f:
    LR = pickle.load(f)

# Get number of features model expects
n_features = LR.n_features_in_

st.write(f"Model expects {n_features} input features")

# Create inputs dynamically
inputs = []
for i in range(n_features):
    val = st.number_input(f"Feature {i+1}", value=0.0)
    inputs.append(val)

# Prediction
if st.button("Predict Price"):
    input_data = np.array(inputs).reshape(1, -1)
    prediction = LR.predict(input_data)
    st.success(f"💰 Predicted Price: {prediction[0]:.2f}")
