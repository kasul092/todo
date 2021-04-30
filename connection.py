import sqlite3

con=sqlite3.connect("test.db")
#print("database connected")

cur=con.cursor()

#cur.execute('''CREATE TABLE product(p_id INTEGER PRIMARY KEY AUTOINCREMENT,task text NOT NULL,date text,status text)''');
#print("table created")

cur.execute("INSERT INTO product(task,date,status) VALUES('go to meeting','24-12-2020','not complete')");
cur.execute("INSERT INTO product(task,date,status) VALUES('give presentation','24-12-2020','not complete')");
cur.execute("INSERT INTO product(task,date,status) VALUES('preparation of presentation','23-12-2020','complete')");
con.commit()
print("data inserted")
#con.close()
#print("connection closed")

cur.execute("SELECT * From product")
rows=cur.fetchall()
for row in rows:
    print(row)