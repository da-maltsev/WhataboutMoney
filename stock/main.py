import click

from .currency.cli import rate
from .ticker.cli import price, stat
from .crypto.cli import crypto


@click.group()
def entry_point():
    pass

commands = [rate, stat, price, crypto]
for func in commands:
    entry_point.add_command(func)
