import pandas as pd
from prophet import Prophet
import matplotlib.pyplot as plt

# Load the monthly revenue data
df = pd.read_csv("monthly_revenue_kpis.csv")

# Prepare data for Prophet
df_prophet = df[['Month', 'MonthlyRevenue']].copy()
df_prophet.columns = ['ds', 'y']
df_prophet['ds'] = pd.to_datetime(df_prophet['ds'])

# Initialize and train Prophet model
model = Prophet()
model.fit(df_prophet)

# Forecast for the next 12 months
future = model.make_future_dataframe(periods=12, freq='MS')
forecast = model.predict(future)

# Plot the forecast
fig = model.plot(forecast)
plt.title("Monthly Revenue Forecast")
plt.xlabel("Date")
plt.ylabel("Revenue")
plt.tight_layout()
plt.show()

# Save forecast
forecast.to_csv("revenue_forecast.csv", index=False)
