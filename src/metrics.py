import numpy as np
import pandas as pd

def calculate_performance_metrics(returns, risk_free_rate=0):
    """
    Calculate performance and risk metrics from monthly portfolio returns.

    Parameters
    ----------
    returns : pd.Series
        Monthly portfolio returns expressed as decimals.
    risk_free_rate : float, default 0
        Annualized risk-free rate expressed as a decimal.

    Returns
    -------
    dict
        Dictionary containing:
        - CAGR: Compound Annual Growth Rate.
        - Annualized Volatility: Annualized standard deviation of returns.
        - Sharpe Ratio: Annualized risk-adjusted return.
        - Max Drawdown: Maximum loss relative to a previous portfolio peak.

    Notes
    -----
    - Assumes 12 monthly observations per year.
    - Uses monthly compounded returns for CAGR and drawdown.
    - Assumes an initial portfolio value of 1.
    - Metrics are calculated before transaction costs and slippage
      when gross returns are supplied.
    """

    cumulative_returns = (1 + returns).cumprod()
    cagr = (cumulative_returns.iloc[-1] / 1) ** (12 / len(returns)) - 1

    annualized_volatility = returns.std() * np.sqrt(12)
    annual_returns = returns.mean() * 12

    sharpe_ratio = (annual_returns - risk_free_rate) / annualized_volatility

    running_max = cumulative_returns.cummax().clip(lower=1)
    drawdown = (cumulative_returns / running_max) - 1
    max_drawdown = drawdown.min()

    return {
        "CAGR" : cagr,
        "Annualized Volatility" : annualized_volatility,
        "Sharpe Ratio" : sharpe_ratio,
        "Max Drawdown" : max_drawdown
    }
    