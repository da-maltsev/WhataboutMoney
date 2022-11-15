from .models import Ticker


def get_current_price(ticker_name: str, ticker: Ticker = None) -> str:
    ticker = is_ticker(ticker_name, ticker)
    key = 'currentPrice'
    if key in ticker.info.keys():
        ticker_price = ticker.info[key]
        if ticker_price:
            return f"{ticker.ticker_name} current price is {ticker_price} {ticker.ticker_currency}"
    return f'There is no current price for {ticker.ticker_name}'


def get_day_low(ticker_name: str, ticker: Ticker = None) -> str:
    ticker = is_ticker(ticker_name, ticker)
    key = 'dayLow'
    if key in ticker.info.keys():
        day_low = ticker.info[key]
        if day_low:
            return f"{ticker.ticker_name} day low is {day_low} {ticker.ticker_currency}"
    return f'There is no day low for {ticker.ticker_name}'


def get_day_high(ticker_name: str, ticker: Ticker = None) -> str:
    ticker = is_ticker(ticker_name, ticker)
    key = 'dayHigh'
    if key in ticker.info.keys():
        day_high = ticker.info[key]
        if day_high:
            return f"{ticker.ticker_name} day high is {day_high} {ticker.ticker_currency}"
    return f'There is no day high for {ticker.ticker_name}'


def get_premarket_price(ticker_name: str, ticker: Ticker = None) -> str:
    ticker = is_ticker(ticker_name, ticker)
    key = 'preMarketPrice'
    if key in ticker.info.keys():
        price = ticker.info[key]
        if price:
            return f"{ticker.ticker_name} preMarket price is {price} {ticker.ticker_currency}"
    return f'There is no preMarket price for {ticker.ticker_name}'


def get_regular_market_price(ticker_name: str, ticker: Ticker = None) -> str:
    ticker = is_ticker(ticker_name, ticker)
    key = 'regularMarketPrice'
    if key in ticker.info.keys():
        price = ticker.info[key]
        if price:
            return f"{ticker.ticker_name} regular market price is {price} {ticker.ticker_currency}"
    return f'There is no regular market price for {ticker.ticker_name}'


def get_stat(ticker_name: str, ticker: Ticker = None) -> str:
    ticker = is_ticker(ticker_name, ticker)
    stats = [
        get_current_price(ticker_name, ticker),
        get_regular_market_price(ticker_name, ticker),
        get_premarket_price(ticker_name, ticker),
        get_day_low(ticker_name, ticker),
        get_day_high(ticker_name, ticker),
    ]
    ticker_len = len(ticker.ticker_name)
    pretty_stat = f'{ticker.ticker_name}:\n'
    for stat in stats:
        if 'There is no' in stat:
            pretty_stat += f' - {stat}\n'
        else:
            pretty_stat += f' -{stat[ticker_len:]}\n'

    return pretty_stat


def is_ticker(ticker_name: str, ticker: Ticker) -> Ticker:
    if not ticker:
        return Ticker(ticker_name)
    else:
        return ticker
