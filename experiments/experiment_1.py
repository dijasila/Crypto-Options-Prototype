# experiments/experiment_1.py

import os
import pandas as pd

def run_experiment():
    # Hypothesis: Testing Moving Average Crossover Strategy
    print("Experiment 1: Testing Moving Average Crossover Strategy")
    
    # Load sample data
    data_path = os.path.join("data", "sample_data.csv")
    data = pd.read_csv(data_path)

    # Simple analysis: Calculate moving averages
    data['SMA_5'] = data['Close'].rolling(window=5).mean()
    data['SMA_20'] = data['Close'].rolling(window=20).mean()

    # Strategy: Buy when SMA_5 crosses above SMA_20
    data['Signal'] = 0
    data['Signal'][data['SMA_5'] > data['SMA_20']] = 1

    # Save results
    results_path = os.path.join("results", "experiment_1_results.txt")
    data.to_csv(results_path)
    print(f"Results saved to {results_path}")