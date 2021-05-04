import click

@click.command()
@click.option('--name','-n', prompt='Your name', help='Provide Your Name')
@click.option('--number','-na', type = int , prompt='Your number', help='Provide Your Mobile Number')
def hello(name, number):
    click.echo(f'my name is {name} a number {number}')

if __name__=='__main__':
    hello()