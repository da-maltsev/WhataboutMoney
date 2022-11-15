import re

import requests


class Currency:
    def __init__(self, currency_name: str):
        self.currency_name = self.validate_currency(currency_name)

    def validate_currency(self, currency_name: str):
        currency_name = currency_name.upper()
        if not re.fullmatch(r'[A-Z]{3}', currency_name):
            raise Exception('Incorrect currency name. It should be equal to 3 and consist of letters')
        return currency_name

    def get_exchange_rate(self, symbols: str = None):
        url = 'https://api.exchangerate.host/latest'
        symbols = self.validate_symbols(symbols)
        response = requests.get(url, {'base': self.currency_name, 'symbols': symbols})
        if response.status_code != 200:
            raise Exception('Bad request. Exchange rate server is not available.')
        data = response.json()
        rates = data['rates']
        pretty_data = ''
        i = 0
        for key, value in rates.items():
            i += 1
            pretty_data += f' {self.currency_name}/{key} = {round(value, 2)}'.ljust(25) + '|'
            if i % 3 == 0:
                pretty_data += '\n'
        return pretty_data

    def validate_symbols(self, symbols: str):
        symbols = symbols.upper()
        if not re.fullmatch(r'([A-Z]{3},?){1,}', symbols):
            raise Exception('Incorrect currency name. It should be equal to 3 and '
                            'consist of letters. Each currency should be separeted by comma')
        return symbols

    def __str__(self):
        return f"{self.currency_name}"
