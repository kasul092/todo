import click
import sys

from todo import database

@click.command()
@click.option("--add", "-a", nargs = -1, help = "Add the tasks.")

def main(
    insert,
    add
):

    if add:
        add_to_task = click.prompt("Please enter the task", type = str)
        for add_to_task in add:
            task  = add_to_task
            if task:
                is_task_added = database.DatabaseConnection.add_task()
                if is_task_added:
                    print("Task added successfully")

sys.exit(0)