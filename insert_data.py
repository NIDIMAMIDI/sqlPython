import mysql.connector
mydb = mysql.connector.connect(host="localhost", user="root",password="Sharu@7981350465", database="shannu")
cur = mydb.cursor() 
z = "insert into swap(emp_id, emp_name, salary) values(%s,%s,%s)"
a = (100, "Sharu", 798165)
cur.execute(z,a)
mydb.commit()
print("Data Inserted Successfully")