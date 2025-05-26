import streamlit as st
import pandas as pd
import joblib

# Load the trained model and vectorizer
model = joblib.load("spam_model.pkl")
vectorizer = joblib.load("vectorizer.pkl")

st.title("📧 Spam Detector")
st.write("Enter a message to predict if it's spam:")

message = st.text_area("Message")

if st.button("Predict"):
    if message.strip() == "":
        st.warning("Please enter a message.")
    else:
        message_vector = vectorizer.transform([message])
        prediction = model.predict(message_vector)[0]
        result = "🚫 Spam" if prediction == 1 else "✅ Not Spam"
        st.success(f"Prediction: {result}")
