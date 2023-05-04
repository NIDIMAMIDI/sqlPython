import mysql.connector
mydb = mysql.connector.connect(host="localhost", user="root",password="Sharu@7981350465", database="shannu")
cur = mydb.cursor()
t = "create table swap(emp_id integer(10), emp_name varchar(30), salary integer(10))"
cur.execute(t) 
