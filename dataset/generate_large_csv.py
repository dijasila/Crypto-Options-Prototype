
import pandas as pd
import numpy as np

# Set random seed for reproducibility
np.random.seed(42)

# Generate a date range
dates = pd.date_range(start='2020-01-01', end='2023-12-31', freq='D')

# Generate random stock prices
prices = np.random.normal(loc=100, scale=10, size=len(dates)).cumsum()

# Create a DataFrame
data = pd.DataFrame({
    'Date': dates,
    'Close': prices
})

# Save DataFrame to CSV
data.to_csv('data/sample_data.csv', index=False)

print("Large dataset has been generated and saved as data/sample_data.csv")