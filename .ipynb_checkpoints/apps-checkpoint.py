import streamlit as st
import pandas as pd
import joblib

# Load saved model, scaler, and selector
model = joblib.load('coffee_sales_model.pkl')
scaler = joblib.load('scaler.pkl')
selector = joblib.load('feature_selector.pkl')

st.set_page_config(page_title="Coffee Shop Revenue Predictor", page_icon="☕", layout="centered")
st.title("☕ Coffee Shop Daily Revenue Predictor")

# User inputs
num_customers = st.number_input("Number of Customers", value=100)
avg_order_value = st.number_input("Average Order Value (₹)", value=200)
operating_hours = st.number_input("Operating Hours", value=10)
num_employees = st.number_input("Number of Employees", value=5)
marketing_spend = st.number_input("Marketing Spend (₹)", value=2000)
foot_traffic = st.number_input("Location Foot Traffic", value=500)

if st.button("Predict Revenue"):
    input_df = pd.DataFrame([[num_customers, avg_order_value, operating_hours, num_employees, marketing_spend, foot_traffic]],
                            columns=['Number_of_Customers_Per_Day', 'Average_Order_Value', 'Operating_Hours_Per_Day', 'Number_of_Employees', 'Marketing_Spend_Per_Day', 'Location_Foot_Traffic'])
    scaled_input = scaler.transform(input_df)
    selected_input = selector.transform(scaled_input)
    prediction = model.predict(selected_input)[0]
    st.success(f"💰 Predicted Daily Revenue: ₹{prediction:.2f}")
