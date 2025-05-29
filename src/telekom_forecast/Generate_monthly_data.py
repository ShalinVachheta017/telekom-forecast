import pandas as pd
import numpy as np

# Load the revenue-enhanced dataset
df = pd.read_csv("telecom_revenue_with_pricing.csv")

# Simulate 24 months of data
np.random.seed(42)
months = pd.date_range(start="2022-01-01", periods=24, freq='MS')
df['Month'] = np.random.choice(months, size=len(df))

# Aggregate monthly revenue and plan counts
monthly_revenue = df.groupby('Month').agg({
    'MonthlyRevenue': 'sum',
    'CustomerID': 'count',
    'SubscriptionPlan': lambda x: x.value_counts().to_dict()
}).reset_index()

# Extract plan counts into columns
plan_counts = monthly_revenue['SubscriptionPlan'].apply(pd.Series).fillna(0)
plan_counts.columns = [f"Plan_{col}_Count" for col in plan_counts.columns]

# Merge plan counts back into main DataFrame
monthly_data = pd.concat([monthly_revenue[['Month', 'MonthlyRevenue', 'CustomerID']], plan_counts], axis=1)
monthly_data.rename(columns={'CustomerID': 'CustomerCount'}, inplace=True)

# Save result
monthly_data.to_csv("monthly_revenue_kpis.csv", index=False)

# Print summary
print(monthly_data.head())
