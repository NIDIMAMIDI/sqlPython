import mysql.connector
mydb = mysql.connector.connect(host="localhost", user="root",password="Sharu@7981350465", database="shannu")
cur = mydb.cursor()
d = "delete from swap where emp_id = 210"
cur.execute(d)
mydb.commit()