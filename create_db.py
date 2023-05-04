import mysql.connector
mydb = mysql.connector.connect(host="localhost", user="root",password="Sharu@7981350465")
cur = mydb.cursor()
cur.execute("create database Shannu")