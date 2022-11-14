import re
import yfinance as yf


class Ticker:
    def __init__(self, ticker_name):
        self.ticker_name = self.validate_ticker(ticker_name)
        self.ticker = yf.Ticker(self.ticker_name)
        self.info = self.get_info()
        self.ticker_currency = self.info['currency']

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
        ticker_price = self.info['currentPrice']
        pretty_price = f"{self.ticker_name} current price is {ticker_price} {self.ticker_currency}"
        return pretty_price

    def get_day_low(self):
        day_low = self.info['dayLow']
        pretty_day_low = f"{self.ticker_name} day low is {day_low} {self.ticker_currency}"
        return pretty_day_low

    def get_day_high(self):
        day_high = self.info['dayHigh']
        pretty_day_high = f"{self.ticker_name} day high is {day_high} {self.ticker_currency}"
        return pretty_day_high

    def get_premarket_price(self):
        price = self.info['preMarketPrice']
        pretty_price = f"{self.ticker_name} preMarket price is {price} {self.ticker_currency}"
        return pretty_price

    def get_regular_market_price(self):
        price = self.info['dayHigh']
        pretty_price = f"{self.ticker_name} regular market price is {price} {self.ticker_currency}"
        return pretty_price

    def get_stat(self):
        stats = [
            self.get_current_price(),
            self.get_regular_market_price(),
            self.get_premarket_price(),
            self.get_day_low(),
            self.get_day_high()
        ]
        ticker_len = len(self.ticker_name)
        pretty_stat = f'{self.ticker_name}:\n'
        for stat in stats:
            pretty_stat += f' -{stat[ticker_len:]}\n'

        return pretty_stat

    def __str__(self):
        return f"{self.ticker_name}"
