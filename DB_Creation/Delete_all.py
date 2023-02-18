"""
first run the create_DB file 
This module need to run one time using terminal "python DB_Creation/tables_creation.py"
it will create the tables in flight_DB  
"""

from flask import Flask
import mysql.connector

app = Flask(__name__)

mydb = mysql.connector.connect(
  host="localhost",
  user="root",
  password="admin",
  database="flight_db"
)

my_cursor = mydb.cursor()

# get all table names in the database
my_cursor.execute("SHOW TABLES")
tables = my_cursor.fetchall()

#TODO need to sort the tables per FK relations

# # loop through all tables and drop them
for table in tables:
    table_name = table[0]
    print(table_name)
    try:
        my_cursor.execute("DROP TABLE {}".format(table_name))
        mydb.commit()
    except Exception as e:
        print("Error:", e)
    
my_cursor.close()
mydb.close()
print("All tables deleted.")