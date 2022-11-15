import requests


class CryptoCurrency:
    def __init__(self, currency_name: str):
        self.currency_name = currency_name

    def get_exchange_rate(self):
        url = "https://api.coincap.io/v2/assets"
        response = requests.get(url, {'search': self.currency_name})
        if response.status_code != 200:
            raise Exception('Bad request. Exchange rate server is not available.')
        data = response.json()
        if not data['data']:
            raise Exception(f'{self.currency_name} does not exist.')
        first_result = data['data'][0]
        pretty_data = f'{first_result["name"]} price is {round(float(first_result["priceUsd"]), 4)} USD'
        return pretty_data

    def __str__(self):
        return f"{self.currency_name}"
