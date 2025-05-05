
import streamlit as st
import joblib
import numpy as np

# Load saved model
model = joblib.load("fraud_model.pkl")

# Page config
st.set_page_config(page_title="AI Credit Card Fraud Detector", layout="centered")

# UI Design
st.title("**Credit Card Fraud Detection**")
st.markdown("Guard your transactions with AI-powered fraud prediction.")

st.image("https://cdn-icons-png.flaticon.com/512/1286/1286840.png", width=100)

# Input fields
profession = st.selectbox("Profession", ["Engineer", "Doctor", "Teacher", "Lawyer", "Other"])
income = st.number_input("Monthly Income", min_value=0)
credit_card_number = st.text_input("Credit Card Number")
expiry = st.text_input("Expiry Date (MM/YY)")
security_code = st.text_input("Security Code (CVV)")

# Predict button
if st.button("Check for Fraud"):
    # Encode profession manually
    profession_encoded = {
        "Doctor": 0,
        "Engineer": 1,
        "Lawyer": 2,
        "Teacher": 3,
        "Other": 4
    }[profession]

    # Build input array (without scaling)
    input_data = np.array([[profession_encoded, income]])

    # Predict
    prediction = model.predict(input_data)[0]
    probability = model.predict_proba(input_data)[0][1]

    if prediction == 1:
        st.error(f"**Fraud Detected!** (Confidence: {probability:.2%})")
    else:
        st.success(f"**Transaction is Safe.** (Confidence: {1 - probability:.2%})")
