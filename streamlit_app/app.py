import streamlit as st
import pandas as pd
import plotly.express as px

# Load datasets
monthly_data = pd.read_csv("monthly_revenue_kpis.csv")
forecast_data = pd.read_csv("revenue_forecast.csv")

# Title and description
st.title("📊 Telecom Revenue Forecast Dashboard")
st.markdown("This dashboard visualizes historical telecom KPIs and revenue forecasts using Prophet.")

# Monthly Revenue Chart
st.subheader("Monthly Revenue")
fig_revenue = px.line(monthly_data, x='Month', y='MonthlyRevenue', title='Monthly Revenue (Historical)')
st.plotly_chart(fig_revenue)

# Forecast Chart
st.subheader("Revenue Forecast")
fig_forecast = px.line(forecast_data, x='ds', y='yhat', title='Revenue Forecast (Prophet)')
fig_forecast.add_scatter(x=forecast_data['ds'], y=forecast_data['yhat_lower'], mode='lines', name='Lower Bound')
fig_forecast.add_scatter(x=forecast_data['ds'], y=forecast_data['yhat_upper'], mode='lines', name='Upper Bound')
st.plotly_chart(fig_forecast)

# Plan Distribution
st.subheader("Plan Distribution Over Time")
plan_cols = [col for col in monthly_data.columns if col.startswith("Plan_")]
fig_plans = px.area(monthly_data, x='Month', y=plan_cols, title='Plan Distribution')
st.plotly_chart(fig_plans)
