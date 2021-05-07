import click

@click.command()
@click.argument('number1',type=int)
@click.argument('number2',type=int)
@click.argument('method', default='add')

def main(number1, number2, method):
    click.secho('the addition is:',fg='black', bg='white', bold=True)
    method=number1 + number2
    click.echo(method)

    click.secho('the subctration is:',fg='yellow', bg='red', bold=True)
    method=number1 - number2
    click.echo(method)

    click.secho('the multiplication is:', fg='black', bg='white', bold=True)
    method=number1 * number2
    click.echo(method)

if __name__=='__main__':
    main()