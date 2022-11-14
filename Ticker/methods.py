from .models import Ticker


def get_current_price(ticker_name):
    ticker = Ticker(ticker_name)
    ticker_price = ticker.info['currentPrice']
    pretty_price = f"{ticker.ticker_name} current price is {ticker_price} {ticker.ticker_currency}"
    return pretty_price


def get_day_low(ticker_name):
    ticker = Ticker(ticker_name)
    day_low = ticker.info['dayLow']
    pretty_day_low = f"{ticker.ticker_name} day low is {day_low} {ticker.ticker_currency}"
    return pretty_day_low


def get_day_high(ticker_name):
    ticker = Ticker(ticker_name)
    day_high = ticker.info['dayHigh']
    pretty_day_high = f"{ticker.ticker_name} day high is {day_high} {ticker.ticker_currency}"
    return pretty_day_high


def get_premarket_price(ticker_name):
    ticker = Ticker(ticker_name)
    price = ticker.info['preMarketPrice']
    pretty_price = f"{ticker.ticker_name} preMarket price is {price} {ticker.ticker_currency}"
    return pretty_price


def get_regular_market_price(ticker_name):
    ticker = Ticker(ticker_name)
    price = ticker.info['dayHigh']
    pretty_price = f"{ticker.ticker_name} regular market price is {price} {ticker.ticker_currency}"
    return pretty_price

def get_stat(ticker_name):
    ticker = Ticker(ticker_name)
    stats = [
        get_current_price(ticker_name),
        get_regular_market_price(ticker_name),
        get_premarket_price(ticker_name),
        get_day_low(ticker_name),
        get_day_high(ticker_name)
    ]
    ticker_len = len(ticker.ticker_name)
    pretty_stat = f'{ticker.ticker_name}:\n'
    for stat in stats:
        pretty_stat += f' -{stat[ticker_len:]}\n'

    return pretty_stat
