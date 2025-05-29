import pandas as pd

# Load your dataset
df = pd.read_csv("telecom_revenue_assurance_dataset.csv")

# Define subscription plan pricing
plan_pricing = {
    'Basic': 20,
    'Standard': 40,
    'Premium': 60
}

# Map plan to revenue
df['MonthlyRevenue'] = df['SubscriptionPlan'].map(plan_pricing)

# Save output to new CSV
df.to_csv("telecom_revenue_with_pricing.csv", index=False)

# Show summary
print(df['MonthlyRevenue'].describe())
print(df.groupby('SubscriptionPlan')['MonthlyRevenue'].agg(['count', 'mean']))
