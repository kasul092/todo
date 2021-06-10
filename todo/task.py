import click


from todo.database import DatabaseConnection

dc = DatabaseConnection()

@click.command(help = "Add the task.")
@click.option("--add","-a")
def add(add):
    if add:
        task_added = dc.add_task(add)
        if task_added:
            print("Task added successfully.")
    else:
        print("Please provide a Task")


@click.command(help = "Show the task.")
@click.option("--show", "-s")
def show(show):
    view = dc.show_task()

@click.command(help = "Update the task.")
@click.option("--update","-u")
def update(update):
    task_id = int(click.prompt("Enter t_id which you want to modify"))
    updated_task = click.prompt("Enter new task")
    dc.update_task(t_id = task_id , task = updated_task)
    
    