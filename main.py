import yfinance as yf
import pprint

pp = pprint.PrettyPrinter(indent=4)

ticker_name = input()
if len(ticker_name) > 4:
    raise Exception('Incorrect ticker name')

ticker = yf.Ticker(ticker_name)
if ticker.info['logo_url'] == '':
    raise Exception('Such ticker does not exist')

ticker_price = ticker.info['currentPrice']
ticker_currency = ticker.info['currency']
pretty_price = f"{ticker_name} current price is {ticker_price} {ticker_currency}"

pp.pprint(pretty_price)
