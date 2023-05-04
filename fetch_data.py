import mysql.connector
mydb = mysql.connector.connect(host="localhost", user="root",password="Sharu@7981350465", database="shannu")
cur = mydb.cursor() 
f = "select * from swap"
cur.execute(f)
display = cur.fetchall()
for x in display:
    print(x)