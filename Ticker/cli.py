from .methods import *
import click


@click.group()
def cli():
    pass


@click.command()
@click.argument('ticker_name')
def price(ticker_name):
    click.echo(get_current_price(ticker_name))


@click.command()
@click.argument('ticker_name')
def stat(ticker_name):
    click.echo(get_stat(ticker_name))


cli.add_command(stat)
cli.add_command(price)
