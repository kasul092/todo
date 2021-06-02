import click


from todo.database import DatabaseConnection

dc = DatabaseConnection()

@click.command(help = "Add the task.")
@click.option("--add","-a")
def add(add):
    task_added = dc.add_task(add)
    if task_added:
        print("Task added successfully.")


@click.command(help = "Show the task.")
@click.option("--show", "-s")
def show(show):
    view = dc.show_task()
    