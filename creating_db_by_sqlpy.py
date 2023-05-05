"""we can create database by CREATE DATABASE statement"""
"""Cusror() function is used Allows Python code to execute PostgreSQL command in a database session. """
"""cursor() method: they are bound to the connection for the entire lifetime and all the commands are executed in the context of the database session wrapped by the connection."""

import mysql.connector
mydb = mysql.connector.connect(host="localhost", user="root", password="Sharu@7981350465")
cur = mydb.cursor()
cur.execute("create database hostel_students")
