import click

from todo.task import add
from todo.task import show

@click.group()
def main():
    ''''Todo Manager'''''
    pass

main.add_command(add)
main.add_command(show)

if __name__ == "__main__":

    main()