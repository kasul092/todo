import sqlite3

con = sqlite3.connect("test.db")
print("database created.")

cur = con.cursor()

class database_connection():

    def table(self):

        cur.execute(""" Create table IF NOT EXISTS test1
                       (t_id INTEGER Primary key AUTOINCREMENT, task TEXT, date TEXT, status TEXT)""")
        print("table created")
        con.commit()

    def add_task(self):

        cur.execute("""INSERT INTO test1(task, date, status) 
                        VALUES("?", "?", "?")""")
        con.commit()
        print("Task added successfully.")


database_connectionc_object  = database_connection()
table_object = database_connectionc_object.table()
add_task_object = database_connectionc_object.add_task()