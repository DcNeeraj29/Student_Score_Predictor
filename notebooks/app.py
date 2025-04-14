import streamlit as st
import pandas as pd
import joblib

model = joblib.load('Student_Score_Predictor.pkl')

st.title("Student Final Score Predictor")
st.write("Predicting a Student's final score based on their study habits and performance.")

# Input fields

study_hours = st.slider("Study Hours", min_value = 0.1, max_value = 10.0, step= 0.5)
attendance = st.slider("Attendance (%)", min_value=1, max_value=100)
previous_score = st.slider("Previous Score (%)", 0, 100, 80)
participation = st.radio("Participation in class", [0,1], format_func = lambda x: "No" if x == 0 else "Yes")

if st.button("Predict Final Score"):
    input_df = pd.DataFrame([[study_hours, attendance, previous_score, participation]],columns=["StudyHours", "Attendance", "PreviousScore", "Participation"])
    prediction = model.predict(input_df)[0]
    prediction = max(0, min(100, prediction))
    st.success(f"Predict Final Score: {prediction:.2f}")

