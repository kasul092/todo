import click

@click.command()
@click.option('--blue', is_flag=True, help='message in blue colour')
def hello(blue):

    if blue:
        click.secho(f'hello there', fg='blue')
    else:
        click.secho(f'hello there')

if __name__=='__main__':
    hello()