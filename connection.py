import mysql.connector
mydb = mysql.connector.connect(host="localhost", user="root",password="Sharu@7981350465")
print(mydb.connection_id)
