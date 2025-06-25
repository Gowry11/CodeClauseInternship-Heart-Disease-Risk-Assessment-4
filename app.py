import streamlit as st
import numpy as np
import pickle

# Load the trained model
with open('model.pkl', 'rb') as f:
    model = pickle.load(f)

# Title of the app
st.title("❤️ Heart Disease Risk Assessment")

st.write("Enter your health details below to assess your risk.")

# Input fields
age = st.slider("Age", 18, 100, 25)
sex = st.selectbox("Sex", ["Male", "Female"])
cp = st.selectbox("Chest Pain Type (0-3)", [0, 1, 2, 3])
trestbps = st.slider("Resting Blood Pressure (mm Hg)", 80, 200, 120)
chol = st.slider("Cholesterol (mg/dL)", 100, 400, 200)
fbs = st.selectbox("Fasting Blood Sugar > 120 mg/dl?", [0, 1])
restecg = st.selectbox("Resting ECG Result", [0, 1, 2])
thalach = st.slider("Max Heart Rate Achieved", 70, 210, 150)
exang = st.selectbox("Exercise Induced Angina?", [0, 1])
oldpeak = st.slider("Oldpeak (ST depression)", 0.0, 6.0, 1.0)
slope = st.selectbox("Slope of Peak Exercise ST", [0, 1, 2])
ca = st.selectbox("Number of Major Vessels (0–3)", [0, 1, 2, 3])
thal = st.selectbox("Thal (0 = normal, 1 = fixed defect, 2 = reversible defect)", [0, 1, 2, 3])

# Convert sex to numeric
sex = 1 if sex == "Male" else 0

# When user clicks "Predict"
if st.button("Predict"):
    # Put all input into an array for the model
    input_data = np.array([[age, sex, cp, trestbps, chol, fbs, restecg,
                            thalach, exang, oldpeak, slope, ca, thal]])

    # Use model to predict
    prediction = model.predict(input_data)

    # Show result
    if prediction[0] == 1:
        st.error("⚠️ High risk of heart disease.")
    else:
        st.success("✅ Low risk of heart disease.")
