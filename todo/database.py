import sqlite3

con= sqlite3.connect("store.db")
print("Database created")

cur = con.cursor()

class DatabaseConnection():

    def table(self):

        cur.execute("""Create table IF NOT EXISTS myroutine
                        (t_id INTEGER Primary Key AUTOINCREMENT, task TEXT, date TEXT, status TEXT)""")
        con.commit()
        print("Table created successfully.")

    def add_task(self):

        cur.execute("""INSERT INTO myroutine(task, date, status)
                        VALUES("?", "?", "?")""")
        con.commit()
        print("Task added successful.")

    def show_task(self):

        cur.execute("""SELECT * from myroutine""")
        rows = cur.fetchall()
        for row in rows:
            print(row)


dc = DatabaseConnection()
table_object = dc.table()
add_task_obj = dc.add_task()
show_task_obj = dc.show_task()
