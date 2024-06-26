
import pandas as pd
import sys
import sklearn
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score
import nltk
nltk.download("popular")
import numpy
import streamlit as st
from sklearn.metrics import confusion_matrix

with open('prediction_on_training_data.pkl', 'rb') as file:
    # Load the data from the file
    label, text = pickle.load(file)

model = LogisticRegression()

st.title ("Email Spam Prediction")
st.write("""
This app uses a Logistic Regression classifier to predict whether an email is spam or ham.
""")
email_text = st.text_area("Enter the email text here:")

if st.button('Predict'):
    prediction = model.predict([email_text])
    prediction_proba = model.predict_proba([email_text])

    st.write(f"Predicted Class: {'Spam' if prediction[0] == 1 else 'Ham'}")
    st.write("Prediction Probability:")
    st.write(f"Spam: {prediction_proba[0][1]:.2f}")
    st.write(f"Ham: {prediction_proba[0][0]:.2f}")

    # Display model evaluation metrics
    st.write("Model Evaluation Metrics:")
    st.write(f"Accuracy: {accuracy:.2f}")
    st.write("Classification Report:")
    st.text(report)
    st.write("Confusion Matrix:")
    st.write(confusion_matrix)
