import sqlite3
from tabulate import tabulate


class DatabaseConnection:
    def __init__(self):
        self.conn = sqlite3.connect("test.db")
        self.cur = self.conn.cursor()

        self.cur.execute(
            """Create table IF NOT EXISTS myroutine
            (task_id INTEGER primary key AUTOINCREMENT, task TEXT)"""
        )
        self.conn.commit()

    def add_task(self, task):
        self.task = task
        self.cur.execute("""INSERT INTO myroutine(task) VALUES(?)""", (self.task,))
        self.conn.commit()
        print("task added successfully.")

    def show_task(self):
        self.cur.execute("""SELECT * FROM myroutine""")
        data_for_table = self.cur.fetchall()
        table = tabulate(data_for_table, headers=["ID", "Task"], tablefmt="fancy_grid")
        print(table)

    def update_task(self, task_id, task):
        self.task = task
        self.task_id = task_id
        self.cur.execute(
            """UPDATE myroutine
                SET task = ?
                WHERE task_id = ?""",
            (self.task, self.task_id),
        )
        self.conn.commit()
        print("Task updated successfully.")

    def delete_task(self, task_id):
        self.task_id = task_id
        self.cur.execute(
            """DELETE FROM myroutine
                WHERE task_id = ?""",
            (self.task_id,),
        )
        self.conn.commit()
        print("Task deleted successfully.")
