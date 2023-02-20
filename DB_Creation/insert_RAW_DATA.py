"""
first run the create_DB file 
This module need to run one time using terminal "python DB_Creation/insert_RAW_DATA.py"
it will create the tables in flight_DB  
"""

from flask import Flask, redirect, url_for,request, render_template
from flask_mysqldb import MySQL
import mysql.connector

app = Flask(__name__)          

mydb = mysql.connector.connect(
  host="localhost",
  user="root",
  password="admin",
  database="flight_db"
)

my_cursor = mydb.cursor()
user_roles_list = ['Administrator', 'Airline_Company', 'Customer', 'Anonymous']
users_list = [['Ofir6bd','123456789','Ofir6bd@gmail.com'],['Ofir7bd','123456789','Ofir7bd@gmail.com']]
countries_list = ['Israel', 'Marocco', 'USA', 'Lebanon']
Airlines_list = ['El-Al', 'Ryanair', 'Lufthansa', 'united airlines']

######### insert data to DB
for i in range(len(user_roles_list)):
  try:
      my_cursor.execute("INSERT INTO User_Roles (Role_Name) VALUES (%s)", (user_roles_list[i],))
      mydb.commit()
  except mysql.connector.errors.ProgrammingError as e:
      print(f"Error: {e}")

for i in range(len(users_list)):
  try:
      my_cursor.execute("INSERT INTO Users (Username, Password, Email, User_Role) VALUES (%s, %s, %s)", (users_list[i][0], users_list[i][1], users_list[i][2]), )
      mydb.commit()
  except mysql.connector.errors.ProgrammingError as e:
      print(f"Error: {e}")

# for i in range(len(Airlines_list)):
#   try:
#       my_cursor.execute("INSERT INTO User_Roles (Role_Name) VALUES (%s)", (user_roles_list[i],))
#       my_cursor.execute("INSERT INTO Countries (Name) VALUES (%s)", (countries_list[i],))
#       my_cursor.execute("INSERT INTO Airline_Companies (Name) VALUES (%s)", (Airlines_list[i],))
#       mydb.commit()
#   except mysql.connector.errors.ProgrammingError as e:
#       print(f"Error: {e}")

# for i in range(len(Airlines_list)):
#   try:
#       my_cursor.execute("INSERT INTO User_Roles (Role_Name) VALUES (%s)", (user_roles_list[i],))
#       my_cursor.execute("INSERT INTO Countries (Name) VALUES (%s)", (countries_list[i],))
#       my_cursor.execute("INSERT INTO Airline_Companies (Name) VALUES (%s)", (Airlines_list[i],))
#       mydb.commit()
#   except mysql.connector.errors.ProgrammingError as e:
#       print(f"Error: {e}")

my_cursor.close()
mydb.close()