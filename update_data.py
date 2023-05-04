import mysql.connector
mydb = mysql.connector.connect(host="localhost", user="root",password="Sharu@7981350465", database="shannu")
cur = mydb.cursor()
u = "update swap set salary = salary + 100 where emp_id = 100"
cur.execute(u)
mydb.commit()