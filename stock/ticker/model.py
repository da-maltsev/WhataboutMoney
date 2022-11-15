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
        if not re.fullmatch(r'[A-Z]{3,5}', ticker_name):
            raise Exception('Incorrect ticker name. It should be less or equal to 5 and consist of letters')
        return ticker_name

    def validate_info(self):
        if self.ticker.info['logo_url'] == '':
            raise Exception('Such ticker does not exist')
        return self.ticker.info

    def get_current_price(self) -> str:
        key = 'currentPrice'
        if key in self.info.keys():
            ticker_price = self.info[key]
            if ticker_price:
                return f"{self.ticker_name} current price is {ticker_price} {self.ticker_currency}"
        return f'There is no current price for {self.ticker_name}'

    def get_day_low(self) -> str:
        key = 'dayLow'
        if key in self.info.keys():
            day_low = self.info[key]
            if day_low:
                return f"{self.ticker_name} day low is {day_low} {self.ticker_currency}"
        return f'There is no day low for {self.ticker_name}'

    def get_day_high(self) -> str:
        key = 'dayHigh'
        if key in self.info.keys():
            day_high = self.info[key]
            if day_high:
                return f"{self.ticker_name} day high is {day_high} {self.ticker_currency}"
        return f'There is no day high for {self.ticker_name}'

    def get_premarket_price(self) -> str:
        key = 'preMarketPrice'
        if key in self.info.keys():
            price = self.info[key]
            if price:
                return f"{self.ticker_name} preMarket price is {price} {self.ticker_currency}"
        return f'There is no preMarket price for {self.ticker_name}'

    def get_regular_market_price(self) -> str:
        key = 'regularMarketPrice'
        if key in self.info.keys():
            price = self.info[key]
            if price:
                return f"{self.ticker_name} regular market price is {price} {self.ticker_currency}"
        return f'There is no regular market price for {self.ticker_name}'

    def get_stat(self) -> str:
        stats = [
            self.get_current_price(),
            self.get_regular_market_price(),
            self.get_premarket_price(),
            self.get_day_low(),
            self.get_day_high(),
        ]
        ticker_len = len(self.ticker_name)
        pretty_stat = f'{self.ticker_name}:\n'
        for stat in stats:
            if 'There is no' in stat:
                pretty_stat += f' - {stat}\n'
            else:
                pretty_stat += f' -{stat[ticker_len:]}\n'

        return pretty_stat

    def __str__(self):
        return f"{self.ticker_name}"
