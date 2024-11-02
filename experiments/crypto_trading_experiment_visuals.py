import os
import pandas as pd
import matplotlib.pyplot as plt

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

    # Visualization
    plt.figure(figsize=(14, 7))

    # Plot the closing prices and moving averages
    plt.plot(data['Date'], data['Close'], label='Close Price', color='blue', alpha=0.5)
    plt.plot(data['Date'], data['SMA_10'], label='10-Day SMA', color='orange')
    plt.plot(data['Date'], data['SMA_50'], label='50-Day SMA', color='red')

    # Plot buy signals
    buy_signals = data[data['Position'] == 1]
    plt.plot(buy_signals['Date'], buy_signals['Close'][buy_signals['Position'] == 1],
             '^', markersize=10, color='g', label='Buy Signal', alpha=1)

    # Plot sell signals
    sell_signals = data[data['Position'] == -1]
    plt.plot(sell_signals['Date'], sell_signals['Close'][sell_signals['Position'] == -1],
             'v', markersize=10, color='r', label='Sell Signal', alpha=1)

    plt.title('Cryptocurrency Trading Strategy Visualization')
    plt.xlabel('Date')
    plt.ylabel('Price')
    plt.legend()
    plt.grid()
    plt.xticks(rotation=45)
    
    # Save the plot
    plot_path = os.path.join("results", "crypto_trading_strategy_plot.png")
    plt.tight_layout()
    plt.savefig(plot_path)
    plt.show()
    print(f"Plot saved to {plot_path}")

if __name__ == "__main__":
    run_experiment()