import click

from mytask.database import DatabaseConnection

dc = DatabaseConnection()


@click.command(help="Add the task.")
@click.option("--add", "-a")
def add(add):
    if add:
        task_added = dc.add_task(add)
        if task_added:
            print("Task added successfully.")
    else:
        print("Please provide a Task")


@click.command(help="Show the task.")
@click.option("--show", "-s")
def show(show):
    view = dc.show_task()


@click.command(help="Update the task.")
@click.option("--update", "-u")
def update(update):
    update_task_id = int(click.prompt("Enter task_id which you want to modify"))
    new_task = click.prompt("Enter new task")
    dc.update_task(task_id=update_task_id, task=new_task)


@click.command(help="Delete the task.")
@click.option("--delete", "-d")
def delete(delete):
    delete_task_id = int(click.prompt("Enter task_id which you want to delete"))
    dc.delete_task(task_id=delete_task_id)


@click.command(help="Sort the task.")
@click.option("--sort", "-o")
def sort(sort):
    order_by = click.prompt("Enter the date to sort the tasks [yyyy-mm-dd]")
    dc.sort_task(date = order_by)

@click.command(help="Provide tag to the task.")
@click.option("--tag", "-t")
def tag(tag):
    tag_task_id = int(click.prompt("Enter task_id which you want to labelled"))
    tags = click.prompt("Could you complete the task [complete/In process]?")
    dc.tag_add(task_id = tag_task_id, tag = tags)