from .model import CryptoCurrency
import click


@click.command()
@click.argument('crypto_currency')
def crypto(crypto_currency: str = 'BTC'):
    """Write <crypto_name> currency to see all exchange rate."""
    try:
        currency = CryptoCurrency(crypto_currency)
        click.echo(currency.get_exchange_rate())
    except Exception as e:
        click.echo(e)
