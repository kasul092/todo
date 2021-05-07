import click

# Python click prompt for value
'''
@click.command()
@click.option("--name", prompt='Your name', help='Provide your name')
def hello(name):
    click.echo(f'Hello, {name}')

if __name__=='__main__':
    hello()'''

# Python click colour output
'''
@click.command()
def coloured():
    click.secho('Hello there', fg="yellow", bold=True)

if __name__=='__main__':
    coloured()'''

# Python click flags
'''
@click.command()
@click.option('--blue', is_flag=True, help='message in blue colour')
def hello(blue):

    if blue:
        click.secho('Hello there', fg='blue')
    else:
        click.secho('Hello there')

if __name__=='__main__':
    hello()
'''
# Flags second
'''
@click.command()
@click.argument('word')
@click.option('--shout/--no-shout', default=False)
def output(word, shout):
    if shout:
        click.echo(word.upper())
    else:
        click.echo(word)

if __name__=='__main__':
    output()'''

# Python click environment variables

import os
@click.argument('mydir', envvar='MYDIR', type= click.Path(exists=True))
@click.command()
def dolist(mydir):

    click.echo(os.listdir(mydir))

if __name__=='__main__':
    dolist()

# Python click option tuples
'''
@click.command()
@click.option('--data', required=True, type=(str, int))
def output(data):
    click.echo(f'name={data[0]} age={data[1]}')

if __name__=='__main__':
    output()'''

# Specifying options multiple times
'''
@click.command()
@click.option('--word','-w', multiple=True)
def words(word):
    click.echo('\n'.join(word))

if __name__=='__main__':
    words()'''

# The Click.File Type
'''
@click.command()
@click.argument('file_name', type=click.File('r'))
@click.argument('lines', default=-1, type=int)
def head(file_name, lines):

    counter=0

    for line in file_name:
        print(line.strip())
        counter +=1

        if counter==lines:
            break

if __name__=='__main__':
    head()'''

# The Click.Path Type
'''
@click.command()
@click.argument('file_name', type=click.Path(exists=True))
@click.argument('lines', default=-1, type=int)
def head(file_name, lines):
    with open(file_name, 'r')as f:
        counter=0
        for line in file_name:
            print(line.strip())
            counter+=1
            if counter == lines:
                break

if __name__=='__main__':
    head()'''

#Python click command groups
'''
@click.group()
def messages():
    pass

@click.command()
def generic():
    click.echo('hello there')

@click.command()
def welcome():
    click.echo('welcome')

messages.add_command(generic)
messages.add_command(welcome)

if __name__=='__main__':
    messages()'''


'''
@click.group()
def cli():
  pass


@cli.command(name='gen')
def generic():
    click.echo('Hello there')


@cli.command(name='wel')
def welcome():
    click.echo('Welcome')


if __name__ == '__main__':
    cli()'''