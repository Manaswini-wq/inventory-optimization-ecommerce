import pandas as pd

# Load synthetic sales data
sales_data = pd.read_csv('data/historical_sales_data.csv')

# Calculate average daily sales per SKU
average_daily_sales = sales_data.groupby('SKU')['Sales'].mean()

# Assume lead time in days
lead_time_days = 7

# Calculate reorder point = average daily sales * lead time
reorder_point = average_daily_sales * lead_time_days

# Save reorder points to CSV
reorder_point_df = reorder_point.reset_index()
reorder_point_df.columns = ['SKU', 'Reorder_Point']
reorder_point_df.to_csv('results/reorder_points_output.csv', index=False)

print("Reorder points calculated and saved!")
