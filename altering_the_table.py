import mysql.connector
mydb = mysql.connector.connect(
    host = "localhost",
    user = "root",
    password = "Sharu@7981350465",
    database = "hostel_students"
)
cur = mydb.cursor()
alter_add = "alter table student_data add column guardian varchar(30)"
cur.execute(alter_add)
cur.execute("alter table student_data rename column guardian to guardian_id")
cur.execute("alter table student_data rename to hostel_student_details")
cur.execute("alter table hostel_student_details modify column guardian_id int")
cur.execute("alter table hostel_student_details drop guardian_id")