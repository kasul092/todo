import click
from operator import mul
from functools import reduce 

@click.command()
@click.argument('val', type = int, nargs=-1)
def hello(val):
    click.echo(f'The sum is {sum(val)}')
    click.echo(f'The product is {reduce(mul, val, 1)}')


if __name__=='__main__':
    hello()