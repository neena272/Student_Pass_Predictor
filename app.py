import streamlit as st
import pickle

# Load trained model
model = pickle.load(open("model.pkl", "rb"))

st.title("🎓 Student Performance Prediction")

st.write("Enter student details below.")

study_hours = st.number_input(
    "Study Hours",
    min_value=0,
    max_value=15
)

attendance = st.number_input(
    "Attendance (%)",
    min_value=0,
    max_value=100
)

previous_marks = st.number_input(
    "Previous Marks",
    min_value=0,
    max_value=100
)

if st.button("Predict"):

    prediction = model.predict(
        [[study_hours, attendance, previous_marks]]
    )

    st.success(f"Prediction: {prediction[0]}")