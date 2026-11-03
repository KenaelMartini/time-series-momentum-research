import yfinance as yf
import pandas as pd

def download_prices(tickers, start_date, end_date, auto_adjust=True, progress=False):
    prices = yf.download(tickers, start=start_date, end=end_date, auto_adjust=auto_adjust, progress=progress)["Close"]
    return prices


def to_monthly_prices(prices):
    monthly_prices = prices.resample("ME").last()
    return monthly_prices

def validate_monthly_prices(monthly_prices, tickers, start_date, end_date):
    if set(monthly_prices.columns) != set(tickers):
        raise ValueError("Unexpected columns or missing tickers")
    if monthly_prices.isna().sum().sum() > 0:
        raise ValueError("Missing values in monthly prices")
    if monthly_prices.index.has_duplicates:
        raise ValueError("Duplicate dates in monthly prices")
    if not monthly_prices.index.is_monotonic_increasing:
        raise ValueError("Dates are not in chronological order")

    start_date = pd.Timestamp(start_date)
    end_date = pd.Timestamp(end_date)
    expected_dates = pd.date_range(start=start_date, end=end_date, freq="ME")
    if not monthly_prices.index.equals(expected_dates):
        raise ValueError("Monthly prices do not cover the entire date range with expected monthly frequency")