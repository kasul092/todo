import sqlite3
import datetime
import sys

date = datetime.date.today()

class databaseconnection(object):

    def __init__(self):
        """
        Calls the function init_db().
        """
        self.con = sqlite3.connect("test.db")
        self.cur = self.con.cursor()
        self.init_db()
    
    def init_db(self):
        self.cur.execute('''CREATE TABLE IF NOT EXISTS
                        myroutine(p_id INTEGER PRIMARY KEY AUTOINCREMENT,
                        task text NOT NULL,date text,status text)''');
        print("table created")
        self.con.commit()

    def add_task(self, task):
        global date
        start = datetime.datetime.now()
        time = start.strftime('%H:%M')
        self.cur.execute("""INSERT INTO myroutine(task,date,status) 
                         VALUES('?','?','?')""",(self.task, "None", date, time),)

        print("data inserted")
        self.con.commit()

    def search_task(self, task):
        self.search = self.task
        myroutine = []
        if self.task:
            self.cur.execute("""Select id, task, date, status
                                FROM myroutine where task=? """, (self.search))
        myroutine = self.cur.fetchall()                        
    
    def show_task(self, task):
        self.cur.execute("SELECT * From myroutine")
        rows=self.cur.fetchall()
        for task in rows:
            print(task)

    def update_task(self, task_id, task):
        self.task_id = task_id
        self.task = task
        self.cur.execute("""SELECT task from myroutine where task_id is = ?""", (self.task_id))
        self.cur.execute("""Update myroutine SET task = ? where task_id is = ?""", (self.task, self.task_id))
        self.con.commit()
        return True

    def delete_task(self, task_id):
        self.task_id = task_id
        self.cur.execute("""SELECT task from myroutine where task_id is = ?""", (self.task_id))
        delete_task = self.cur.fetchone()
        self.cur.execute("""DELETE From myroutine where task_id = ?""", (self.task_id))
        self.con.commit()
        if delete_task:
            return True
      
    def sort_task(self, date, task):
        self.date = date
        self.cur.execute("""sort task from myroutine where date is = ?""", (self.date))
        rows = self.cur.fetchall(date)
        for task in rows:
            print(task)

database_connection = databaseconnection()

sys.exit(0)