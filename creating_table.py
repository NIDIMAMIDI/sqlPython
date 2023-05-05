import mysql.connector
mydb = mysql.connector.connect(host="localhost", user="root", password="Sharu@7981350465", database="hostel_students")
cur = mydb.cursor()
c = "create table student_data(id int primary key, name varchar(30) not null, contact_no int(10) unique not null, room_no int not null)"
cur.execute(c)
