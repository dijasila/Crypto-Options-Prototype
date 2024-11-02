# generate_dataset.py

import pandas as pd

# Sample data for the dataset
data = {
    'text': [
        "Once upon a time, in a land far, far away.",
        "The quick brown fox jumps over the lazy dog.",
        "To be, or not to be, that is the question.",
        "All that glitters is not gold.",
        "A journey of a thousand miles begins with a single step."
    ]
}

# Create a DataFrame
df = pd.DataFrame(data)

# Save DataFrame to CSV
df.to_csv('data/dataset.csv', index=False)

print("Dataset has been generated and saved as data/dataset.csv")