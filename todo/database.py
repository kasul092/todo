import sqlite3
from tabulate import tabulate

class DatabaseConnection():

    def __init__(self):
        self.con = sqlite3.connect("test.db")
        self.cur = self.con.cursor()

        self.cur.execute(
            """Create table IF NOT EXISTS myroutine
            (t_id INTEGER primary key AUTOINCREMENT, task TEXT)""" 
        )
        self.con.commit()

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
        s = tabulate(fat,headers= ['ID', 'Task'],tablefmt='fancy_grid')
        print(s)

    def update_task(self,t_id,task):
        self.task = task
        self.t_id = t_id
        self.cur.execute(
            """UPDATE myroutine
                SET task = ?
                WHERE t_id = ?""",
                (self.task,self.t_id))
        self.con.commit()
        print("Task updated successfully.")
                  
    def delete_task(self,t_id):
        self.t_id = t_id
        self.cur.execute(
            """DELETE FROM myroutine
                WHERE t_id = ?""",
                (self.t_id,))
        self.con.commit()
        print("Task deleted successfully.")
                  