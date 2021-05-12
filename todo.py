import sys  # used to exit from system
import click 

from todo import database  # used to perform database operations.
from todo import view  # Used to show results to users

database_connection = database.DatabaseConnection()
output = view.ShowResults()


@click.command()
@click.option("--add", "-a", nargs=0, help="Add Tasks with space-separated")
@click.option("--delete", "-d", nargs=1, help="Remove a Task of particular ID")
@click.option("--clear", "-c", multiple=True, nargs=0, help="Clear Tasks")
@click.option("--update", "-u", nargs=2, help="Update a Task for specific ID")
@click.option("--search", "-s", nargs=1, help="Search all Tasks by ID")
@click.option("--view", "-v", multiple=True, nargs=0, help="Show Tasks")
@click.option("--version", "-V", is_flag=True, help="Check latest version")
@click.argument("insert", nargs=-1, required=False)
def main( 
    insert,
    add,
    delete,
    clear,
    update,
    search,
    view,
    version):

    """
    Todo command line task manager tool
    """

    if add:
        for task_to_add in add:
            task = task_to_add
        if task:
            is_task_added = database_connection.add_task(task)
            if is_task_added:
                print("New Task added.")
            else:
                print("Task is already added. Check Task information. See help")
    
    elif delete:
        is_task_deleted = database_connection.delete_task(delete)
        if is_task_deleted:
            print("Task deleted.")
        else:
            print("Task of this id is not present in database.")

    elif update:
        task_list = []
        for update_to_task in update:
            task_list.append(update_to_task)
        task_id = task_list[0]
        task = task_list[1]            
        if task:
            is_task_updated = database_connection.update_task(task_id, task)
            if is_task_updated:
                print("Task of this id updated.")
            else:
                print("Provided id is not present or same Task is already in available.")

    elif view:
        output.print_tasks(database_connection.show_task())

    elif search:
        output.print_tasks(database_connection.search_task(search))
    
    elif clear:
        is_db_clear = database_connection.delete_all_task()
        if is_db_clear:
            print("All tasks deleted.")
        else:
            print("Database does not have any data.")

    elif version:
        print("todo v0.1")

    sys.exit(0)        
                   

