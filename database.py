import datetime
import os
import sqlite3
import sys

date = datetime.date.today()

class DatabaseConnection(object):
    """Class to perform database operations."""

    def __init__(self):
        """
        Calls the function init_db().
        """
        self.config_path = os.path.expanduser("~/.config/readit")
        self.databasefile = os.path.join(self.config_path, "test.db")
        self._check_conf_dir()
        self.db = sqlite3.connect(self.databasefile)
        self.cursor = self.db.cursor()
        self.init_db()

    def _check_conf_dir(self):
        if not os.path.exists(self.config_path):
            os.mkdir(self.config_path)
            return True
        elif os.path.exists(self.config_path):
            return True
        return False

    def init_db(self):
        """Create database connection.
        creates or opens file mydatabase with sqlite3 Database.
        get cursor object.
        create table.
        """

        try:
            if self._check_conf_dir():
                self.cursor.execute(
                    """CREATE TABLE IF NOT EXISTS products
                    (id INTEGER PRIMARY KEY AUTOINCREMENT NOT NULL,
                    url TEXT NOT NULL, date TEXT, time TEXT, status TEXT)"""
                )
                self.db.commit()
            else:
                raise IOError("Directory does not exists")

        except sqlite3.OperationalError as e:
            print("ERROR: Failed to create table.")
            print(e)
            sys.exit(1)

    def add_task(self, task):
        """
    task will be adding to database.
        """

        try:
            self.task = task
            global date
            start = datetime.datetime.now()
            time = start.strftime("%H:%M:%S")
            self.cursor.execute(
                """
                INSERT INTO tags(task), date, time, status) VALUES (?, ?, ?, ?)
                """,
                (self.task, "None", date, time),
            )
            self.db.commit()
            return True
        except Exception:
            raise sqlite3.OperationalError
    
    def delete_task(self, task_id):
        """
        tasks can deleted as per id number provided.
        """
        try:
            self.task_id = task_id
            self.cursor.execute(""" SELECT task FROM product where id=? """, (self.task_id,))
            deleted_task = self.cursor.fetchone()
            self.cursor.execute(""" DELETE FROM product WHERE id=? """, (self.task_id,))
            self.db.commit()
            if deleted_task:
                return True
            else:
                return False
        except Exception:
            raise sqlite3.OperationalError

    def update_task(self, task_id, task):
        """
        tasks can be updated with respect to id.
        """

        try:

            self.task_id = task_id
            self.task = task
            self.cursor.execute(""" SELECT task FROM product WHERE id=?""", (self.task_id))
            self.cursor.execute(
                """ UPDATE product SET task=? WHERE id=?""", (self.task, self.task_id)
            )
            self.db.commit()
            return True
        except Exception:
            raise sqlite3.OperationalError

    def show_task(self):
        """
        All tasks from database displayed to user on screen.
        """
        try:
            self.cursor.execute(""" SELECT id, task, date, time, status FROM product """)
            all_product = self.cursor.fetchall()
            self.db.commit()
            if all_product == []:
                return None
            else:
                return all_product
        except Exception:
            raise sqlite3.OperationalError

    def search_task(self, search_value):
        """
        Group of Tasks displayed with respect to search_value.

        """
        try:
            self.search = search_value
            all_product = []
            if self.check_tag(search_value):
                self.cursor.execute(
                    """ SELECT id, task, date, time, status
                                    FROM product WHERE tags=?""",
                    (self.search),
                )
                all_product = self.cursor.fetchall()
            else:
                self.cursor.execute(""" SELECT * FROM product""")
                product = self.cursor.fetchall()
                for task in product:
                    if search_value.lower() in task[1]:
                        all_product.append(task)
            self.db.commit
            if all_product == []:
                return None
            else:
                return all_product
        except Exception:
            raise sqlite3.OperationalError

    def delete_all_task(self):
        """
        All Tasks from database will be deleted.
        """
        try:
            self.cursor.execute(""" DELETE FROM product """)
            self.db.commit()
            return True
        except Exception:
            raise sqlite3.OperationalError

    def check_id(self, task_id):
        """
        Check this is available in database.
        """
        try:
            self.cursor.execute(""" SELECT task FROM bookmarks WHERE id=?""", (task_id))
            all_row = self.cursor.fetchall()
            if all_row == []:
                return None
            return all_row
        except Exception:
            raise sqlite3.OperationalError
        