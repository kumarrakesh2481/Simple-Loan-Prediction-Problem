# 🏦 Loan Prediction System

A simple machine learning web app to predict loan approval status using user input data. Built with Python, Streamlit, and scikit-learn, this project uses a supervised learning model trained on a public dataset (`train.csv`).

---

## 📌 Project Overview

This application helps determine whether a loan should be approved based on various features like income, credit history, loan amount, and more. The ML model is trained using historical data and deployed with Streamlit for a user-friendly interface.

---

## 🚀 Features

- Upload and process `train.csv` dataset
- Clean and preprocess data using Pandas & NumPy
- Train and test a classification model using scikit-learn
- Predict loan approval for new applicants
- Interactive Streamlit web UI

---

## 🔧 Tech Stack

- Python 3.9+
- NumPy
- Pandas
- scikit-learn
- Streamlit

---

## 📂 Dataset

- **Source:** `train.csv` (from [Loan Prediction Dataset - Analytics Vidhya](https://datahack.analyticsvidhya.com/contest/practice-problem-loan-prediction-iii/))
- **Target Column:** `Loan_Status`
- **Features include:**
  - Gender, Married, Dependents, Education, Self_Employed
  - ApplicantIncome, CoapplicantIncome, LoanAmount, Loan_Amount_Term, Credit_History
  - Property_Area

---

## 📦 Installation and Setup
pip install -r requirements.txt
streamlit run app.py

### 1. Clone the repository
loan-prediction-app/
├── train.csv
├── app.py
├── model.pkl
├── scaler.pkl
├── requirements.txt
└── README.md

