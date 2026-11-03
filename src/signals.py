import numpy as np

def calculate_momentum(prices, lookback=12):
    momentum = prices.pct_change(periods=lookback)
    return momentum

def generate_signals(momentum):
    signals = np.sign(momentum)
    return signals

def clean_signals_and_targets(signals, targets):
    valid_signals = (signals != 0) & signals.notna()
    valid_targets = (targets != 0) & targets.notna()
    mask = valid_signals & valid_targets

    signals_clean = signals.where(mask)
    targets_clean = targets.where(mask)

    return signals_clean, targets_clean, mask

def generate_targets(prices, horizon=1):
    forward_returns = prices.pct_change(periods=horizon).shift(-horizon)
    targets = np.sign(forward_returns)
    return targets