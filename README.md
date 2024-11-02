# Crypto-Options-Prototype

## Project Overview
This project provides a basic prototype of a trading algorithm for crypto and exchange options using moving averages.
![Project Diagram](https://github.com/dijasila/Crypto-Options-Prototype/blob/master/image/resp_struct.PNG)
## Folder Structure
- `data/`: Contains data files.
- `experiments/`: Contains scripts for running experiments.
- `models/`: Contains trading strategy models.
- `results/`: Stores results of experiments.

## Running the Project
1. Install dependencies with:
   ```bash
   pip install -r requirements.txt



## Results
![results on a dummy dataset](https://github.com/dijasila/Crypto-Options-Prototype/blob/master/image/crypto_trading_strategy_plot.png)

The visualization section includes:

Confusion Matrix: Shows how well the model predicted the "buy" and "sell" classes. This matrix is useful for understanding the model's performance on each class.

Performance Metrics:

Accuracy: Overall, how often the model correctly predicts.
Classification Report: Provides precision, recall, and F1-score for each class.
![KNN_experiment](https://github.com/dijasila/Crypto-Options-Prototype/blob/master/image/confusion_matrix_knn.png)
