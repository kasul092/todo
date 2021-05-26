import click

from todo.database import DatabaseConnection

dc = DatabaseConnection()

@click.command()
@click.option("--add", "-a", help = "Add the task.")
def add(add):
    task_added = dc.add_task(add)
    if task_added:
        print("Task added successfully.")


@click.command()
@click.option("--show", "-s", help = "Show the task.")
def show(show):
    print(dc.show_task(show))



