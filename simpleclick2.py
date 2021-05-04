import click

@click.command()
@click.argument('name', default ='junior')
@click.argument('age', type=int)
def hello(name, age):
    click.echo(f'I m {age} years old and my name is {name}')

if __name__=='__main__':
    hello()