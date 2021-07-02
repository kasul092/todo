import click

from mytask.task import add
from mytask.task import show
from mytask.task import update
from mytask.task import delete
from mytask.task import sort


@click.group()
def main():
    """""MyTask Manager"""""
    pass


main.add_command(add)
main.add_command(show)
main.add_command(update)
main.add_command(delete)
main.add_command(sort)

if __name__ == "__main__":

    main()
