# Electricity-Time-SeriesREADME.md — Professional GitHub Version
# ⚡ Electricity Bill Forecasting & Anomaly Detection

## 📌 Project Overview
This project performs **time series forecasting** on monthly electricity billing data using
**Facebook Prophet**. It helps forecast future electricity bills, analyze seasonal patterns,
and detect abnormal billing months.

---

## 🎯 Real-World Use Case
- Power distribution companies
- Smart city energy monitoring
- Household electricity bill planning
- Anomaly detection in billing systems

---

## 📊 Dataset Description
The dataset contains monthly electricity billing records with the following columns:

| Column | Description |
|------|------------|
| Bill_Date | Billing month |
| On_peak | Peak hour usage |
| Off_peak | Off-peak usage |
| Usage_charge | Energy charge |
| Billed_amount | Total monthly bill |
| Billing_days | Number of billing days |

---

## 🧠 Methodology
1. Data loading & cleaning  
2. Exploratory Data Analysis (EDA)  
3. Trend & seasonality analysis  
4. Time series forecasting using Prophet  
5. Anomaly detection using confidence intervals  
6. Model evaluation (MAE, RMSE)  
7. Deployment using Streamlit  

---

## 📈 Model Performance
- **MAE:** ~32  
- **RMSE:** ~41  

These results indicate reliable forecasting for real-world electricity billing data.

---

## 🖥️ Web Application
A Streamlit web app allows users to:
- Upload billing data
- Visualize historical trends
- Forecast future bills
- Detect anomalous months
