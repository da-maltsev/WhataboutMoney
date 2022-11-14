import re
import yfinance as yf


def input_ticker():
    ticker_name = input().upper()
    if not re.fullmatch(r'[A-Z]{2,4}', ticker_name):
        raise Exception('Incorrect ticker name (should be less or equal to 4)')
    return ticker_name


class Ticker:
    def __init__(self):
        self.ticker_name = input_ticker()
        self.ticker = yf.Ticker(self.ticker_name)

    def get_info(self):
        if self.ticker.info['logo_url'] == '':
            raise Exception('Such ticker does not exist')
        return self.ticker.info

    def get_current_price(self):
        ticker_price = self.ticker.info['currentPrice']
        ticker_currency = self.ticker.info['currency']
        pretty_price = f"{self.ticker_name} current price is {ticker_price} {ticker_currency}"
        return pretty_price

    def __str__(self):
        return f"{self.ticker_name}"
