# sqlPython
The below commands are used to install mysql-connector-python in command prompt
PYTHON SQL CONNECTOR COMMANDS:
python -m pip install mysqlclient
python -m pip install mysql-connector-python
python -m pip install pymysql


The below code is used to check whether mysql.connector module  is installed or not.... 

--> Refer demo_my_sql_test
import mysql.connector
"""If the above code is executed with no errors, then you have "mysql.connector" module insatlled"""

--> Refer demo_mysql_connect.py

After importing the module 
"""we can start creating connection to the database by using user name and password"""
"""
mydb = mysql.connector.connect(
    host="localhost", 
    user="your_user_name", 
    password="your_MySQL_Password"
)

--> Refer creating_db_by_sqlpy.py
Creating a DataBase
"""we can create database by CREATE DATABASE statement"""
"""Cusror() function is used Allows Python code to execute PostgreSQL command in a database session. """
"""cursor() method: they are bound to the connection for the entire lifetime and all the commands are executed in the context of the database session wrapped by the connection."""
cur = mydb.cursor()
cur is the reference..
by using execute() method we can create database

--> Refer returning_db_list.py and db_exist or not.py

*** To check if the database is created or not we use the command "SHOW DATABASES;" 


                -->     CREATING A TABLE    <--
--> Refer creating_table.py
""we can create TABLE by CREATE TABLE table_Name statement"""
mydb = mysql.connector.connect(
    host="localhost", 
    user="your_user_name", 
    password="your_MySQL_Password"
    database="Database name"
)
we have to provide database name to store the tables

-- Checking if table is exists or not by using "SHOW TABLES;" statement
--> Refer check_if_table_exists.py

            --> Altering the table <--
--> Refer aletering_the_table.py
--> Refer multiple_statements_execute.py

