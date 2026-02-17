import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
from prophet import Prophet

st.set_page_config(page_title="Electricity Bill Forecasting", layout="centered")

st.title("⚡ Electricity Bill Forecasting & Anomaly Detection")
st.write("Time Series Analysis using Facebook Prophet")

# Upload dataset
uploaded_file = st.file_uploader(
    "Upload Electricity Billing CSV File",
    type=["csv"]
)

if uploaded_file is not None:
    # Load data
    df = pd.read_csv(uploaded_file)
    df['Bill_Date'] = pd.to_datetime(df['Bill_Date'])
    df = df.sort_values("Bill_Date")

    st.subheader("📊 Raw Data Preview")
    st.dataframe(df.head())

    # Prepare data for Prophet
    df_prophet = df[['Bill_Date', 'Billed_amount']].rename(
        columns={'Bill_Date': 'ds', 'Billed_amount': 'y'}
    )

    # Plot original data
    st.subheader("📈 Monthly Electricity Bill Trend")
    fig1, ax1 = plt.subplots()
    ax1.plot(df_prophet['ds'], df_prophet['y'])
    ax1.set_xlabel("Date")
    ax1.set_ylabel("Billed Amount")
    st.pyplot(fig1)

    # Train Prophet model
    model = Prophet(
        yearly_seasonality=True,
        weekly_seasonality=False,
        daily_seasonality=False
    )
    model.fit(df_prophet)

    # Forecast period
    months = st.slider("Select Forecast Period (Months)", 3, 24, 12)

    future = model.make_future_dataframe(periods=months, freq='M')
    forecast = model.predict(future)

    # Forecast plot
    st.subheader("🔮 Forecasted Electricity Bills")
    fig2 = model.plot(forecast)
    st.pyplot(fig2)

    # Components plot
    st.subheader("🧩 Trend & Seasonality Components")
    fig3 = model.plot_components(forecast)
    st.pyplot(fig3)

    # Anomaly Detection
    merged = df_prophet.merge(
        forecast[['ds', 'yhat', 'yhat_upper', 'yhat_lower']],
        on='ds',
        how='left'
    )

    merged['Anomaly'] = (
        (merged['y'] > merged['yhat_upper']) |
        (merged['y'] < merged['yhat_lower'])
    )

    st.subheader("🚨 Detected Anomalies")
    st.dataframe(merged[merged['Anomaly'] == True])

else:
    st.info("Please upload a CSV file to start forecasting.")
