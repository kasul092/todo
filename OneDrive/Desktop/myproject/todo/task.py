import click
import sys

from todo import connection #used to perform database operation

database_connection = connection.databaseconnection() 

@click.command()
@click.option("--add",'-a', nargs = -1, help = "Add the task")
@click.option("--update",'-u', nargs = 1, help = "Update the task")
@click.option("--view",'-v', multiple  = True, help = "View the task")
@click.option("--search",'-r', nargs = 1, help = "Search the task")
@click.option("--delete",'-d', nargs = 1, help = "Delete the task")
@click.option("--sort",'-s', nargs = 1, help = "Sort the task")
@click.option("--version",'-e', is_flag = True, help = "Check latest version")
@click.argument("insert", nargs =-1, required = False)

def main(
    insert,
    add,
    update,
    view,
    search,
    delete,
    sort,
    version
):
    """
     Todo command line manager tool
    """
    if add:
        for task_to_add in add:
            task = task_to_add
            if task:
                is_task_added =database_connection.add_task(task)
                if is_task_added:
                    print("Task added successfully.")
            
    elif update:
        task_list = []
        for update_to_task in update:
            task_list.append(update_to_task)
        task_id = task_list[0]
        task = task_list[1]
        if task:
            is_task_updated =database_connection.update_task(task)
            if is_task_updated:
                print("Task updated successfully.")

    elif view:
        database_connection.show_task()

    elif search:
        database_connection.search_task()

    elif delete:
         task_deleted = database_connection.delete_task()
         if task_deleted:
             print("Delete the task successfully.")

    elif sort:
        is_task_sort = database_connection.sort_task()
        if is_task_sort:
            print(task_list = [])

    elif version:
        print("todo v0.1")

    else:
        for task_to_add in insert:
            task = task_to_add
            if task:
                is_task_added = database_connection.add_task(task)
                if is_task_added:
                    print("Task added successfully")

sys.exit()
