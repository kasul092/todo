import click

@click.command()
@click.argument('number1', type=int)
@click.argument('number2', type=int)
@click.argument('method', default='addition')

def main(number1, number2, method):
    method= number1 + number2
    click.echo(f'the addition is {method}')

    method = number1 * number2
    click.echo(f'the multiplication is {method}')

if __name__=='__main__':
    main()