import re
import yfinance as yf


class Ticker:
    def __init__(self, ticker_name):
        self.ticker_name = self.validate_ticker(ticker_name)
        self.ticker = yf.Ticker(self.ticker_name)
        self.info = self.validate_info()
        self.ticker_currency = self.info['currency']

    def validate_ticker(self, ticker_name):
        ticker_name = ticker_name.upper()
        if not re.fullmatch(r'[A-Z]{2,4}', ticker_name):
            raise Exception('Incorrect ticker name. It should be less or equal to 4 and consist of letters')
        return ticker_name

    def validate_info(self):
        if self.ticker.info['logo_url'] == '':
            raise Exception('Such ticker does not exist')
        return self.ticker.info

    def __str__(self):
        return f"{self.ticker_name}"
