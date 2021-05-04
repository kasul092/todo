import click

@click.command()
def hello():
    click.secho(f'hello there', fg='red', bold=True)

if __name__=='__main__':
    hello()