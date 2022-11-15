from .model import Ticker
import click


@click.command()
@click.argument('ticker_name')
def price(ticker_name):
    """Simple current price check"""
    try:
        ticker = Ticker(ticker_name)
        click.echo(ticker.get_current_price())
    except Exception as e:
        click.echo(e)


@click.command()
@click.argument('ticker_name')
def stat(ticker_name):
    """Show some short stats about your ticker"""
    try:
        ticker = Ticker(ticker_name)
        click.echo(ticker.get_stat())
    except Exception as e:
        click.echo(e)
