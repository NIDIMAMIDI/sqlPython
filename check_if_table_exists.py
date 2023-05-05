import mysql.connector
mydb = mysql.connector.connect(
    host = "localhost",
    user = "root",
    password = "Sharu@7981350465",
    database = "hostel_students"
)
cur = mydb.cursor()
cur.execute("show tables")
for i in cur:
    print(i)