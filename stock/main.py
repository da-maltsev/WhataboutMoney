import click

from .currency.cli import rate
from .ticker.cli import price, stat


@click.group()
def entry_point():
    pass

commands = [rate, stat, price]
for func in commands:
    entry_point.add_command(func)
