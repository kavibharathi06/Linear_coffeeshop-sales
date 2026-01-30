☕ Coffee Shop Daily Revenue Prediction
📌 Project Overview

This project focuses on building an end-to-end machine learning solution to predict the daily revenue of a coffee shop using operational and customer-related data. The goal is to help business owners make data-driven decisions by estimating revenue under different scenarios.

🎯 Problem Statement

Estimating daily revenue can be challenging due to multiple influencing factors such as customer count, marketing spend, operating hours, and foot traffic. This project aims to build a predictive model that accurately estimates Daily Revenue based on historical data.

🧠 Solution Approach

The project follows a complete machine learning workflow:

Data loading and exploration

Data preprocessing and feature scaling

Feature selection

Model training and evaluation

Model deployment using Streamlit

📊 Dataset Description

The dataset contains operational data with the following features:

Number_of_Customers_Per_Day

Average_Order_Value

Operating_Hours_Per_Day

Number_of_Employees

Marketing_Spend_Per_Day

Location_Foot_Traffic

Daily_Revenue (Target variable)

🤖 Machine Learning Model

Model Used: Linear Regression

Feature Scaling: StandardScaler

Feature Selection: SelectKBest (F-regression)

📈 Model Evaluation Metrics

R² Score

RMSE (Root Mean Squared Error)

MAE (Mean Absolute Error)

MAPE (Mean Absolute Percentage Error)

The model demonstrates good generalization with minimal overfitting.

🚀 Deployment

The trained model is deployed as an interactive Streamlit web application, allowing users to input daily operational parameters and receive real-time revenue predictions.

Saved components:

Trained model

Scaler

Feature selector

All saved using joblib.

🛠️ Technologies Used

Python

Pandas

NumPy

Matplotlib

Seaborn

Scikit-learn

Streamlit

Joblib

▶️ How to Run the Project
# Install required libraries
pip install -r requirements.txt

# Run the Streamlit application
streamlit run apps.py

📂 Project Structure
coffee-shop-revenue-prediction/
│
├── coffee_shop_revenue.csv
├── coffee_sales_model.pkl
├── scaler.pkl
├── feature_selector.pkl
├── apps.py
├── requirements.txt
└── README.md

🌟 Key Learnings

Implemented an end-to-end machine learning pipeline

Applied feature scaling and feature selection techniques

Evaluated regression models using standard metrics

Deployed ML models using Streamlit for real-time use

🔮 Future Enhancements

Experiment with advanced models like Random Forest or XGBoost

Add data visualizations to the Streamlit app

Deploy the application on cloud platforms
