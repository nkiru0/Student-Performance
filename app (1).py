
import pickle
import streamlit as st
import numpy as np
import pandas as pd

# Load your model file
with open('model.pkl','rb') as f:
  model = pickle.load(f)

st.title('Exam Scoring Predictor')

# Add input widgets for user inputs
Attendance = st.slider("Attendance", min_value=1, max_value=5, value=2)
Previous_Scores = st.slider("Previous Score (percent)", min_value=3, max_value=53, value=26)
Tutoring_Sessions = st.slider("Tutoring Sessions", min_value=1, max_value=5, value=2)

# When the 'Predict' button is clicked
if st.button("Predict"):
    # Prepare the input data as a DataFrame (since pipelines often expect a DataFrame)
    input_data = pd.DataFrame({
        'Attendance': [Attendance],
        'Previous_Scores': [Previous_Scores],
        'Tutoring_Sessions': [Tutoring_Sessions]
    })
    prediction = model.predict(input_data)[0].round(2)
    st.write(f'The predicted Score is: {prediction} Percent')
