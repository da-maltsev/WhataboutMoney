from .model import Currency
import click


@click.command()
@click.argument('main_currency')
@click.option('--exchangeable_currencies', '-e', default=None, help='List of currencies like "XXX,YYY,ZZZ".')
def rate(main_currency, exchangeable_currencies):
    """Write <base> currency to see all exchange rates or add filter of currencies with flag -e"""
    try:
        currency = Currency(main_currency)
        click.echo(currency.get_exchange_rate(symbols=exchangeable_currencies))
    except Exception as e:
        click.echo(e)
