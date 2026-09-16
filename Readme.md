# Airline Loyalty Analytics: Customer Churn Prediction, Segmentation and Smart Retention

## Project Overview

This project aims to help an airline identify customers who are likely to disengage from the loyalty program, understand different customer segments, and recommend targeted retention strategies.

The solution combines customer segmentation and machine learning to provide actionable business insights for non-technical users.

---

## Objectives

1. Predict customer churn.
2. Identify meaningful customer segments.
3. Recommend segment-specific retention actions.
4. Provide an interactive dashboard for business users.

---

## Technologies Used

* Python
* Pandas
* NumPy
* Scikit-Learn
* XGBoost
* Matplotlib
* Seaborn
* Streamlit

---

## Folder Structure

```
Airline_Project/
│
├── app.py
├── data_main.csv
├── retention_dashboard.csv
├── feature_importance.csv
├── relative_segment_profile.csv
├── xgb_model.pkl
├── requirements.txt
├── README.md
└── Airline_Loyalty_Analytics_Technical_Report.pdf
```

---

## Working Prototype

The project includes an interactive Streamlit dashboard designed for non-technical users.

The dashboard contains:

* Home Page
* Customer Segmentation
* Churn Prediction
* Smart Retention Dashboard
* Business Insights

The interface enables a marketing manager to identify customers requiring attention and understand the recommended actions without referring to technical documentation.

---

## Running the Application

### Step 1: Install dependencies

```bash
pip install -r requirements.txt
```

### Step 2: Launch the dashboard

```bash
streamlit run app.py
```

---

## Features

### Customer Segmentation

Customers are divided into four behavioral segments:

* Champions / Premium Travelers
* Active Regular Customers
* Occasional Flyers
* Dormant Customers

---

### Churn Prediction

Three machine learning models were evaluated:

* Logistic Regression
* Random Forest
* XGBoost

XGBoost achieved the best performance and was selected as the final model.

---

### Smart Retention

The system assigns customers to risk categories and recommends specific actions based on their segment and churn probability.

Examples include:

* Reactivation campaigns
* Bonus mileage offers
* Personalized discounts
* Premium rewards for high-value customers

---

## Key Findings

* Customer behavior is a stronger indicator of churn than demographic characteristics.
* Total Bookings, Booking Trend, and Recency Months are the strongest drivers of churn.
* Four meaningful customer segments were identified.
* XGBoost achieved the highest predictive performance with an ROC-AUC score of 0.963.

---

## Deliverables

### Working Prototype

Interactive Streamlit Dashboard

### Technical Report

Airline_Loyalty_Analytics_Technical_Report.pdf

### Source Code

Python notebooks and application files

---

## Author

Tanishq Gupta

Project: Unlocking Behavioral Intelligence in Airline Loyalty Programs
