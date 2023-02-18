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
countries_list = ['Israel', 'Marocco', 'USA']
Airlines_list = ['El-Al', 'Ryanair', 'Lufthansa']

for i in range(len(countries_list)):
    try:
        my_cursor.execute("INSERT INTO Countries (Name) VALUES (%s)", (countries_list[i],))
        my_cursor.execute("INSERT INTO Airline_Companies (Name) VALUES (%s)", (Airlines_list[i],))
        mydb.commit()
    except mysql.connector.errors.ProgrammingError as e:
        print(f"Error: {e}")

my_cursor.close()
mydb.close()