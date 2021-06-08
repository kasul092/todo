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

@click.command(help = "Update the task.")
@click.option("--update","-u")
def update(update):
    # task_list = []
    # for update_to_task in update:
    #     task_list.append(update_to_task)
    # t_id = task_list[0]
    # task = task_list[1]
    t_id = click.prompt("Enter t_id which you want to modify")
    mod_check = dc.show_task(t_id)
    if mod_check is None:
        print("No records found")
    else:
        mod = click.prompt("Enter new task", default="None")
        dc.update_task(t_id = t_id , task = mod)

    # task_updated = dc.update_task(update,"task")
    # if task_updated:
    #     print("Task updated successfully.")
    