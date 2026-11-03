import yfinance as yf
import pandas as pd

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