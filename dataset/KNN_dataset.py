import pandas as pd
import numpy as np

# Set random seed for reproducibility
np.random.seed(42)

# Generate a large synthetic dataset
num_samples = 10000  # Adjust for size
data = {
    'Price': np.random.uniform(20000, 60000, num_samples),  # Simulated price range
    'Volume': np.random.uniform(100, 10000, num_samples),   # Simulated volume range
    'Volatility': np.random.uniform(0.1, 10, num_samples),  # Market volatility
    'Signal': np.random.choice(['buy', 'sell'], num_samples)  # Random buy/sell signal
}

# Create DataFrame
df = pd.DataFrame(data)

# Save the dataset to a CSV file
df.to_csv('crypto_trading_data.csv', index=False)
print("Dataset generated and saved as 'crypto_trading_data.csv'")