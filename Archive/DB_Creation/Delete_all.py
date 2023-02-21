"""
first run the create_DB file 
This module need to run one time using terminal "python DB_Creation/delete_all.py"
it will create the tables in flight_DB  
"""

from flask import Flask
import mysql.connector
from sqlalchemy import create_engine

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

tables = ['Tickets', 'Flights', 'Airline_Companies', 'Countries', 'Customers', 'Administrators', 'Users', 'User_Roles']

# loop through all tables and drop them
for table in tables:

    try:
        my_cursor.execute("DROP TABLE {}".format(table))
        mydb.commit()
        # print(f'{table} have been deleted')
    except Exception as e:
        print("Error:", e)
    
my_cursor.close()
mydb.close()
print("All tables deleted.")