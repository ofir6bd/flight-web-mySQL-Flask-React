"""
This module need to run one time using terminal "python DB_Creation/create_DB.py"
it will create flight_DB in mysql 
"""

import mysql.connector

mydb = mysql.connector.connect(
    host="localhost",
    user="root",
    password="admin"
)

my_cursor = mydb.cursor()

my_cursor.execute("CREATE DATABASE flight_db")

try:
    my_cursor.execute("SHOW DATABASES")
    for db in my_cursor:
        print(db)
except mysql.connector.errors.ProgrammingError as e:
    print(f"Error: {e}")
finally:
    my_cursor.close()
    mydb.close()