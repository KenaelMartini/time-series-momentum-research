import numpy as np
import pandas as pd

from src.signals import calculate_momentum, generate_signals

def build_tsmom_positions(monthly_prices, lookback=12):
    momentum = calculate_momentum(monthly_prices, lookback=lookback)
    signals = generate_signals(momentum)
    positions = signals.shift(1)

    return signals, positions

def calculate_portfolio_weights(positions):
    n_tickers = len(positions.columns)
    weights = positions / n_tickers

    return weights

def calculate_portfolio_exposure(portfolio_weights):
    gross_exposure = portfolio_weights.abs().sum(axis=1, min_count=1)
    net_exposure = portfolio_weights.sum(axis=1, min_count=1)

    return gross_exposure, net_exposure

def calculate_gross_portfolio_returns(monthly_prices, weights):
    n_assets = len(weights.columns)
    asset_returns = monthly_prices.pct_change()
    weighted_returns = asset_returns * weights
    gross_portfolio_returns = weighted_returns.sum(axis=1, min_count=n_assets)

    return asset_returns, weighted_returns, gross_portfolio_returns