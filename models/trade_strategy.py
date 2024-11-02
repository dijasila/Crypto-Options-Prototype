# models/trade_strategy.py

import pandas as pd

def moving_average_strategy(data, short_window=5, long_window=20):
    data['Short_MA'] = data['Close'].rolling(window=short_window).mean()
    data['Long_MA'] = data['Close'].rolling(window=long_window).mean()
    data['Signal'] = 0
    data['Signal'][data['Short_MA'] > data['Long_MA']] = 1  # 1 means Buy
    return data