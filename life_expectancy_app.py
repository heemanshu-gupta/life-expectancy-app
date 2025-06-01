import streamlit as st
import pandas as pd
import numpy as np
import joblib

# Load model
model = joblib.load("life_expectancy_model.pkl")

st.set_page_config(page_title="Life Expectancy Predictor", layout="centered")
st.title("🌍 Life Expectancy Prediction App")

st.write("Enter the details below to predict life expectancy.")

# User inputs
status = st.selectbox("Status of Country", ["Developing", "Developed"])
adult_mortality = st.number_input("Adult Mortality", min_value=0.0, value=150.0)
infant_deaths = st.number_input("Infant Deaths", min_value=0.0, value=10.0)
alcohol = st.number_input("Alcohol Consumption", min_value=0.0, value=4.5)
percentage_expenditure = st.number_input("Percentage Expenditure", min_value=0.0, value=100.0)
hepatitis_b = st.number_input("Hepatitis B (%)", min_value=0.0, value=85.0)
measles = st.number_input("Measles Cases", min_value=0.0, value=50.0)
bmi = st.number_input("BMI", min_value=0.0, value=22.0)
under_five_deaths = st.number_input("Under-Five Deaths", min_value=0.0, value=20.0)
polio = st.number_input("Polio (%)", min_value=0.0, value=90.0)
total_expenditure = st.number_input("Total Expenditure", min_value=0.0, value=5.5)
diphtheria = st.number_input("Diphtheria (%)", min_value=0.0, value=85.0)
hiv_aids = st.number_input("HIV/AIDS Rate", min_value=0.0, value=0.1)
gdp = st.number_input("GDP", min_value=0.0, value=1000.0)
population = st.number_input("Population", min_value=0.0, value=1000000.0)
thinness_1_19 = st.number_input("Thinness 10-19 yrs (%)", min_value=0.0, value=3.0)
thinness_5_9 = st.number_input("Thinness 5-9 yrs (%)", min_value=0.0, value=3.5)
income_composition = st.number_input("Income Composition of Resources", min_value=0.0, max_value=1.0, value=0.6)
schooling = st.number_input("Schooling (years)", min_value=0.0, value=12.0)

# Predict button
if st.button("Predict Life Expectancy"):
    input_data = np.array([[ 
        0 if status == "Developing" else 1,
        adult_mortality,
        infant_deaths,
        alcohol,
        percentage_expenditure,
        hepatitis_b,
        measles,
        bmi,
        under_five_deaths,
        polio,
        total_expenditure,
        diphtheria,
        hiv_aids,
        gdp,
        population,
        thinness_1_19,
        thinness_5_9,
        income_composition,
        schooling
    ]])

    prediction = model.predict(input_data)[0]
    st.success(f"✅ Predicted Life Expectancy: **{prediction:.2f} years**")
