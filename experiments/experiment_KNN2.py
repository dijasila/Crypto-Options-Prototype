import os
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.neighbors import KNeighborsClassifier
from sklearn.metrics import accuracy_score, confusion_matrix
import matplotlib.pyplot as plt
import seaborn as sns

# Load the dataset
file_path = 'data/knn.csv'
data = pd.read_csv(file_path)

# Prepare features (X) and target (y)
X = data.drop(columns=['Unnamed: 0', 'TARGET CLASS'])  # Adjust columns based on your dataset
y = data['TARGET CLASS']

# Split data into training and test sets
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3, random_state=42)

# Standardize the feature data
scaler = StandardScaler()
X_train = scaler.fit_transform(X_train)
X_test = scaler.transform(X_test)

# Initialize and train the KNN classifier
knn = KNeighborsClassifier(n_neighbors=5)
knn.fit(X_train, y_train)

# Make predictions on the test set
y_pred = knn.predict(X_test)

# Calculate accuracy and confusion matrix
accuracy = accuracy_score(y_test, y_pred)
conf_matrix = confusion_matrix(y_test, y_pred)

# Ensure 'results' directory exists
results_dir = 'results'
if not os.path.exists(results_dir):
    os.makedirs(results_dir)

# Save accuracy to a text file
with open(os.path.join(results_dir, 'accuracy.txt'), 'w') as f:
    f.write(f'Accuracy: {accuracy:.2f}')

# Visualize and save the confusion matrix
plt.figure(figsize=(8, 6))
sns.heatmap(conf_matrix, annot=True, fmt='d', cmap='Blues', xticklabels=[0, 1], yticklabels=[0, 1])
plt.xlabel('Predicted Class')
plt.ylabel('True Class')
plt.title(f'Confusion Matrix (Accuracy: {accuracy:.2f})')

# Save the confusion matrix plot as an image
plt.savefig(os.path.join(results_dir, 'confusion_matrix.png'))