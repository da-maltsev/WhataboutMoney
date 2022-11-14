from .methods import *
import click


@click.group()
def cli():
    pass


@click.command()
@click.argument('ticker_name')
def price(ticker_name):
    try:
        click.echo(get_current_price(ticker_name))
    except Exception as e:
        click.echo(e)


@click.command()
@click.argument('ticker_name')
def stat(ticker_name):
    try:
        click.echo(get_stat(ticker_name))
    except Exception as e:
        click.echo(e)


cli.add_command(stat)
cli.add_command(price)
