import sqlite3
from tabulate import tabulate

class DatabaseConnection():

    def __init__(self):
        self.con = sqlite3.connect("test.db")
        print("Database created.")
        self.cur = self.con.cursor()

        self.cur.execute(
            """Create table IF NOT EXISTS myroutine
            (t_id INTEGER primary key AUTOINCREMENT, task TEXT)""" 
        )
        self.con.commit()
        print("Table created.")

    def add_task(self, task):
        self.task = task
        self.cur.execute(
            """INSERT INTO myroutine(task) VALUES(?)""",
            (self.task,))
        self.con.commit()
        print("task added successfully.")

    def show_task(self):
        self.cur.execute(
            """SELECT * FROM myroutine""")
        fat = self.cur.fetchall()
        # for task in fat:
        #     print(task)
        s = tabulate(fat,headers= ['ID', 'Task'],tablefmt='fancy_grid')
        print(s)