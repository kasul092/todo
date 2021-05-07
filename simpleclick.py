import click
# Python click simple program

@click.command()
def hello():
    click.echo('Hello there')

if __name__ == '__main__':
    hello()


# Python click default argument
'''
@click.command()
@click.argument('name', default='guest')
def hello(name):
    click.echo(f'Hello {name}')

if __name__=='__main__':
    hello()'''

# Python click argument types
'''
@click.command()
@click.argument('name', default='guest')
@click.argument('age', type=int)
def hello(name, age):
    click.echo(f'{name} is {age} years old')

if __name__=='__main__':
    hello()'''

# Python click variable number of arguments
'''
from operator import mul
from functools import reduce

@click.command()
@click.argument('vals', type=int, nargs=-1)
def process(vals):
    print(f'The sum is {sum(vals)}')
    print(f'The product is {reduce(mul, vals, 1)}')

if __name__=='__main__':
    process()'''

# Python click simple option
'''
@click.command()
@click.option('--n', type=int, default=1)
def dots(n):
    click.echo('SUMIT '* n)

if __name__=='__main__':
    dots()'''

# Python click option names
'''
@click.command()
@click.option('-s', '--string')
def output(string):
    click.echo(string)

if __name__ == '__main__':
    output()'''