import streamlit as st
import requests

st.title("Linear Regression Prediction App")

feature1 = st.number_input("Enter Feature 1")
feature2 = st.number_input("Enter Feature 2")

if st.button("Predict"):

    data = {
        "feature1": feature1,
        "feature2": feature2
    }

    response = requests.post(
        "http://127.0.0.1:8000/predict",
        json=data
    )

    result = response.json()

    st.success(f"Prediction: {result['prediction']}")