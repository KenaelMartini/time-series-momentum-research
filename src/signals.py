import numpy as np

def calculate_momentum(prices, lookback=12):
    momentum = prices.pct_change(periods=lookback)
    return momentum

def generate_signals(momentum):
    signals = np.sign(momentum)
    return signals
