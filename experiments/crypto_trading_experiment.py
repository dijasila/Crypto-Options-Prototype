import os
import pandas as pd

def run_experiment():
    # Hypothesis: Testing a Simple Trading Strategy Based on Moving Averages
    print("Crypto Trading Experiment: Testing a Simple Trading Strategy")
    
    # Load simulated cryptocurrency data
    data_path = os.path.join("data", "crypto_sample_data.csv")
    data = pd.read_csv(data_path)

    # Convert Date to datetime
    data['Date'] = pd.to_datetime(data['Date'])

    # Calculate moving averages
    data['SMA_10'] = data['Close'].rolling(window=10).mean()
    data['SMA_50'] = data['Close'].rolling(window=50).mean()

    # Generate trading signals: Buy when SMA_10 crosses above SMA_50, sell otherwise
    data['Signal'] = 0
    data['Signal'][data['SMA_10'] > data['SMA_50']] = 1
    data['Position'] = data['Signal'].diff()

    # Analyze returns: Assuming we buy at the close price when we signal a buy
    data['Returns'] = data['Close'].pct_change()
    data['Strategy_Returns'] = data['Returns'] * data['Signal'].shift(1)

    # Save results
    results_path = os.path.join("results", "crypto_trading_experiment_results.csv")
    data.to_csv(results_path, index=False)
    print(f"Results saved to {results_path}")

if __name__ == "__main__":
    run_experiment()