"""we can start creating connection to the database by using user name and password"""
"""
mydb = mysql.connector.connect(
    host="localhost", 
    user="your_user_name", 
    password="your_MySQL_Password"
)
"""

import mysql.connector
mydb = mysql.connector.connect(host="localhost", user="root", password="Sharu@7981350465")
print(mydb)
print(mydb.connection_id)



