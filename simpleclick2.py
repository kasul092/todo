import click

@click.command()
@click.argument('word')
@click.option('--shout/--no-shout', default=False, help='message in upper case')
def hello(word, shout):
    

    if shout:
        click.secho(word.upper(), fg='yellow', bold=True)
    else:
        click.secho(word, fg='yellow', bold=True)
    
if __name__=='__main__':
    hello()