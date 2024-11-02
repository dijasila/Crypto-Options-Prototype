# experiments/utils.py

import pandas as pd

def load_data(filename):
    return pd.read_csv(filename)

def save_results(data, filename):
    data.to_csv(filename, index=False)
    print(f"Results saved to {filename}")