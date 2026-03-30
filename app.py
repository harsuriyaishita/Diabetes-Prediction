import streamlit as st
import pickle
import numpy as np

# Load model
model = pickle.load(open("model.pkl", "rb"))

# Page config
st.set_page_config(page_title="Diabetes AI System", layout="centered")

# Title
st.markdown("<h1 style='text-align: center; color: #4CAF50;'>Diabetes Prediction System</h1>", unsafe_allow_html=True)

st.write("Enter patient details to predict diabetes risk")

# Inputs
age = st.slider("Age", 1, 100)
bmi = st.number_input("BMI", value=25.0)
glucose = st.number_input("Blood Glucose Level", value=120.0)
hba1c = st.number_input("HbA1c Level", value=5.5)

# Predict button
if st.button("🔍 Predict"):

    data = np.array([[0, age, 0, 0, 0, bmi, hba1c, glucose]])

    pred = model.predict(data)
    prob = model.predict_proba(data)[0][1]

    st.subheader("Result:")

    # Prediction result
    if pred[0] == 1:
        st.error("⚠️ Diabetic")
    else:
        st.success("✅ Non-Diabetic")

    # Risk score
    st.write(f"### Risk Score: {round(prob*100,2)}%")

    # Risk level
    if prob < 0.3:
        st.success("🟢 Low Risk")
    elif prob < 0.7:
        st.warning("🟡 Medium Risk")
    else:
        st.error("🔴 High Risk")

    # Health insights
    st.subheader("Health Insights")

    if glucose > 180:
        st.warning("High Glucose Level detected")
    if hba1c > 6.5:
        st.warning("High HbA1c - Possible Diabetes")
    if bmi > 30:
        st.warning("High BMI - Obesity Risk")