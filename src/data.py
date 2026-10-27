import yfinance as yf

def download_prices(tickers, start_date, end_date, auto_adjust=True, progress=False):
    prices = yf.download(tickers, start=start_date, end=end_date, auto_adjust=auto_adjust, progress=progress)["Close"]
    return prices


def to_monthly_prices(prices):
    monthly_prices = prices.resample("ME").last()
    return monthly_prices