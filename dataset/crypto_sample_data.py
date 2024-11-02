import pandas as pd
import numpy as np

# Set random seed for reproducibility
np.random.seed(42)

# Generate a date range for the dataset
dates = pd.date_range(start='2021-01-01', end='2023-12-31', freq='D')

# Simulate random prices for a cryptocurrency
prices = np.random.normal(loc=200, scale=20, size=len(dates)).cumsum()

# Create a DataFrame
data = pd.DataFrame({
    'Date': dates,
    'Close': prices
})

# Save DataFrame to CSV
data.to_csv('data/crypto_sample_data.csv', index=False)

print("Crypto dataset has been generated and saved as data/crypto_sample_data.csv")