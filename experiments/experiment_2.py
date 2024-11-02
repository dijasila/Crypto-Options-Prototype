# experiment2.py

import pandas as pd

# Load the dataset
dataset = pd.read_csv('data/dataset.csv')

# Function to count words in each text entry
def count_words(text):
    return len(text.split())

# Apply the function to the dataset
dataset['word_count'] = dataset['text'].apply(count_words)

# Display the results
print("Dataset with word counts:")
print(dataset)

# Save the results to a new CSV file
dataset.to_csv('data/dataset_with_word_counts.csv', index=False)
print("Results saved as data/dataset_with_word_counts.csv")