import os
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.neighbors import KNeighborsClassifier
from sklearn.metrics import accuracy_score, classification_report, confusion_matrix
import seaborn as sns
import matplotlib.pyplot as plt

# Debugging: Check current working directory
print("Current working directory:", os.getcwd())

# Define the path to the dataset
data_path = 'data/crypto_trading_data.csv'

# Check if the file exists before attempting to load it
if not os.path.exists(data_path):
    raise FileNotFoundError(f"The file {data_path} was not found. Please ensure the correct path.")

# Load the dataset
df = pd.read_csv(data_path)

# Encode the target variable (Signal) for KNN
df['Signal'] = df['Signal'].map({'buy': 1, 'sell': 0})

# Define features (X) and target (y)
X = df[['Price', 'Volume', 'Volatility']]
y = df['Signal']

# Split the dataset into training and test sets
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3, random_state=42)

# Initialize the KNN model with k=5
knn = KNeighborsClassifier(n_neighbors=5)

# Fit the model to the training data
knn.fit(X_train, y_train)

# Predict on the test set
y_pred = knn.predict(X_test)

# Evaluate the model's performance
accuracy = accuracy_score(y_test, y_pred)
class_report = classification_report(y_test, y_pred)

# Ensure results folder exists
results_folder = "results"
os.makedirs(results_folder, exist_ok=True)

# Save accuracy and classification report
results_path = os.path.join(results_folder, 'experiment_knn_results.txt')
with open(results_path, 'w') as f:
    f.write(f"Model Accuracy: {accuracy * 100:.2f}%\n\n")
    f.write("Classification Report:\n")
    f.write(class_report)

print(f"Results saved in {results_folder}/experiment_knn_results.txt")

# Confusion Matrix Visualization
conf_matrix = confusion_matrix(y_test, y_pred)
plt.figure(figsize=(8, 6))
sns.heatmap(conf_matrix, annot=True, fmt='d', cmap='Blues', xticklabels=['Sell', 'Buy'], yticklabels=['Sell', 'Buy'])
plt.xlabel('Predicted')
plt.ylabel('Actual')
plt.title('Confusion Matrix of KNN Trading Signal Classifier')

# Save the confusion matrix plot
conf_matrix_path = os.path.join(results_folder, 'confusion_matrix_knn.png')
plt.savefig(conf_matrix_path)
print(f"Confusion matrix plot saved as {conf_matrix_path}")
