
import streamlit as st
import numpy as np
import pandas as pd
import pickle

# Load your model file
with open('model.pkl', 'rb') as f:
    model = pickle.load(f)
# Defining function to predict scores
def predict_score(features):
    prediction = model.predict([features])
    return prediction[0]

st.title('Exam Scoring Predictor')

# Add input widgets for user inputs
Hours_Studied = st.slider("Hours_studied", min_value=1, max_value=5, value=2)
Attendance = st.slider("Attendance", min_value=3, max_value=53, value=26)
Previous_Scores  = st.slider("Previous_Scores ", min_value=1, max_value=5, value=2)

# When the 'Predict' button is clicked
if st.button("Predict"):
    # Prepare the input data as a DataFrame (since pipelines often expect a DataFrame)
    input_data = pd.DataFrame({
        'Hours_Studied': [Hours_Studied],
        'Attendance': [Attendance],
        'Previous_Scores': [Previous_Scores]
    })
    prediction = model.predict(input_data)[0].round(2)
    st.write(f'The predicted Score is: {prediction} Percent')
