import mysql.connector
mydb = mysql.connector.connect(host="localhost", user = "root", password = "Sharu@7981350465", database = "hostel_students")
cur = mydb.cursor()
alt_add = "alter table hostel_student_details add column warden_name varchar(30)"
alt_rename_col = "alter table hostel_student_details rename column warden_name to warden_id"
alt_modidy = "alter table hostel_student_details modify column warden_id int"
alt_rename_table = "alter table hostel_student_details rename to student_details"
alt_drop = "alter table student_details drop column room_no"
cur.execute(alt_add)
cur.execute(alt_rename_col)
cur.execute(alt_modidy)
cur.execute(alt_rename_table)
cur.execute(alt_drop)