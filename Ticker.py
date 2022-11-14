import re
import yfinance as yf


class Ticker:
    def __init__(self, ticker_name):
        self.ticker_name = self.validate_ticker(ticker_name)
        self.ticker = yf.Ticker(self.ticker_name)

    def validate_ticker(self, ticker_name):
        ticker_name = ticker_name.upper()
        if not re.fullmatch(r'[A-Z]{2,4}', ticker_name):
            raise Exception('Incorrect ticker name. It should be less or equal to 4 and consist of letters')
        return ticker_name

    def get_info(self):
        if self.ticker.info['logo_url'] == '':
            raise Exception('Such ticker does not exist')
        return self.ticker.info

    def get_current_price(self):
        ticker_price = self.get_info()['currentPrice']
        ticker_currency = self.get_info()['currency']
        pretty_price = f"{self.ticker_name} current price is {ticker_price} {ticker_currency}"
        return pretty_price

    def __str__(self):
        return f"{self.ticker_name}"
