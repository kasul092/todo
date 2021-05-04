import click

@click.command()
@click.option('--name','-n')
def hello(name):
    click.echo(f'my name is {name}')

if __name__=='__main__':
    hello()