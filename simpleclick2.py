import click

@click.command()
@click.option('--word','-w', multiple = True)
def hello(word):
        click.echo('\n'.join(word)) 
    
if __name__=='__main__':
    hello()