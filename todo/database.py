import sqlite3

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
        self.cur.execute(
            """INSERT INTO myroutine(task) VALUES(?)""",
            (task))
        self.con.commit()

    def show_task(self, task):
        self.cur.execute(
            """SELECT * FROM myroutine""")
        myroutine = self.cur.fetchall()
        for task in myroutine:
            print(task)