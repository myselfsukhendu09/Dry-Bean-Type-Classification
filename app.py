import streamlit as st
import numpy as np
import joblib

# Load trained objects .
model = joblib.load("model.pkl")
scaler = joblib.load("scaler.pkl")
label_encoder = joblib.load("lebel.pkl")

st.set_page_config(page_title="Dry Bean Classifier", layout="centered")

st.title("🌱 Dry Bean Type Classification")
st.write("Enter physical measurements of a dry bean to predict its class.")

st.divider()

# Feature input fields .
features = []

feature_names = [
    "Area",
    "Perimeter",
    "Major Axis Length",
    "Minor Axis Length",
    "Aspect Ratio",
    "Eccentricity",
    "Convex Area",
    "Equivalent Diameter",
    "Extent",
    "Solidity",
    "Roundness",
    "Compactness",
    "ShapeFactor1",
    "ShapeFactor2",
    "ShapeFactor3",
    "ShapeFactor4"
]

for feature in feature_names:
    value = st.number_input(
        label=feature,
        min_value=0.0,
        value=0.0,
        step=0.01
    )
    features.append(value)

st.divider()

# Prediction button.
if st.button("Predict Bean Type"):
    input_array = np.array(features).reshape(1, -1)
    input_scaled = scaler.transform(input_array)
    prediction = model.predict(input_scaled)
    predicted_class = label_encoder.inverse_transform(prediction)[0]

    st.success(f"✅ Predicted Bean Type: **{predicted_class}**")
