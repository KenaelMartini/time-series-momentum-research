import yfinance as yf
import pandas as pd
import numpy as np 

from src.signals import (calculate_momentum, generate_signals, generate_targets, clean_signals_and_targets)

def prepare_momentum_samples(monthly_prices, start_date, end_date, lookbacks=(3, 6, 12), horizon=1):
    """
    Prepare momentum signals and directional targets for a specified period.

    Compute signals for multiple lookbacks, align them with forward-return
    targets, and exclude missing or neutral observations.

    Generate individual validity masks and a common sample to ensure
    consistent comparisons across lookbacks.

    Parameters
    ----------
    monthly_prices : pd.DataFrame
        Monthly adjusted asset prices.
    start_date, end_date : str
        Evaluation period based on signal formation dates.
    lookbacks : tuple, default (3, 6, 12)
        Momentum lookback windows in months.
    horizon : int, default 1
        Forward prediction horizon in months.

    Returns
    -------
    dict
        Original signals and targets, individual validity masks,
        common mask, and common-sample signals and targets.
    """
    if len(lookbacks) == 0:
        raise ValueError("At least one lookback period must be provided")
    
    signals_by_lookback = {}

    for lb in lookbacks:
        momentum = calculate_momentum(monthly_prices, lookback=lb)
        signals = generate_signals(momentum)
        signals_by_lookback[lb] = signals

    targets = generate_targets(monthly_prices, horizon=horizon)
    targets = targets.loc[start_date:end_date]

    for lb, signals in signals_by_lookback.items():
        signals_by_lookback[lb] = signals.loc[start_date:end_date]

    mask_by_lookback = {}

    for lb, signals in signals_by_lookback.items():
        _, _, mask = clean_signals_and_targets(signals, targets)
        mask_by_lookback[lb] = mask
    
    common_mask = mask_by_lookback[lookbacks[0]].copy()

    for lb in lookbacks[1:]:
        common_mask &= mask_by_lookback[lb]

    signals_common_by_lookback = {}

    for lb, signals in signals_by_lookback.items():
        signals_common_by_lookback[lb] = signals.where(common_mask)

    targets_common = targets.where(common_mask)

    return {
        "signals" : signals_by_lookback,
        "targets" : targets,
        "individual_masks" : mask_by_lookback,
        "common_mask" : common_mask,
        "common_signals" : signals_common_by_lookback,
        "common_targets" : targets_common
    }

def calculate_predictive_metrics(signals, targets):
    """
    Calculate directional predictive performance metrics.

    Parameters
    ----------
    signals : pd.DataFrame
        Predicted return directions.
    targets : pd.DataFrame
        Realized return directions.

    Returns
    -------
    dict
        Dictionary containing predictive performance metrics.
    """

    valid_mask = signals.isin([1, -1]) & targets.isin([1, -1])
    n_observations = valid_mask.sum().sum()
    n_correct_predictions = ((valid_mask) & (signals == targets)).sum().sum()

    if n_observations > 0:
        accuracy = n_correct_predictions / n_observations
    else:
        accuracy = np.nan

    n_actual_positive = (valid_mask & (targets == 1)).sum().sum()
    n_true_positive = (valid_mask & ((signals == 1) & (targets == 1))).sum().sum()

    if n_actual_positive > 0:
        positive_recall = n_true_positive / n_actual_positive
    else:
        positive_recall = np.nan

    n_actual_negative = (valid_mask & (targets == -1)).sum().sum()
    n_true_negative = (valid_mask & ((signals == -1) & (targets == -1))).sum().sum()

    if n_actual_negative > 0:
        negative_recall = n_true_negative / n_actual_negative
    else:
        negative_recall = np.nan

    balanced_accuracy = (positive_recall + negative_recall) / 2

    if n_observations > 0:
        always_long_accuracy = n_actual_positive / n_observations
    else:
        always_long_accuracy = np.nan

    if n_observations > 0:
        always_short_accuracy = n_actual_negative / n_observations
    else:
        always_short_accuracy = np.nan

    excess_accuracy_long = accuracy - always_long_accuracy
    excess_accuracy_short = accuracy - always_short_accuracy
        
    return {"n_observations" : n_observations,
            "accuracy" : accuracy,
            "positive_recall" : positive_recall,
            "negative_recall" : negative_recall,
            "balanced_accuracy" : balanced_accuracy,
            "always_long_accuracy" : always_long_accuracy,
            "always_short_accuracy" : always_short_accuracy,
            "excess_accuracy_long" : excess_accuracy_long,
            "excess_accuracy_short" : excess_accuracy_short
            }