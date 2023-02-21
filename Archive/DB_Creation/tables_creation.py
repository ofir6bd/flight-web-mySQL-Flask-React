"""
first run the create_DB file 
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

my_cursor.execute("""CREATE TABLE User_Roles (Id INT AUTO_INCREMENT PRIMARY KEY, 
                                            Role_Name VARCHAR(255) UNIQUE                                            
                                            )""")

my_cursor.execute("""CREATE TABLE Users (Id INT AUTO_INCREMENT PRIMARY KEY, 
                                        Username VARCHAR(255), 
                                        Password VARCHAR(255), 
                                        Email VARCHAR(255),
                                        User_Role INT,
                                        FOREIGN KEY (User_Role) REFERENCES User_Roles(Id)
                                        )""")

my_cursor.execute("""CREATE TABLE Administrators (Id INT AUTO_INCREMENT PRIMARY KEY, 
                                                    First_Name VARCHAR(255), 
                                                    Last_Name VARCHAR(255),   
                                                    User_Id INT,
                                                    FOREIGN KEY (User_Id) REFERENCES Users(Id)
                                                    )""")                                        


my_cursor.execute("""CREATE TABLE Customers (Id INT AUTO_INCREMENT PRIMARY KEY, 
                                            First_Name VARCHAR(255), 
                                            Last_Name VARCHAR(255), 
                                            Address VARCHAR(255), 
                                            Phone_No VARCHAR(255) UNIQUE, 
                                            Credit_Card_No VARCHAR(255) UNIQUE,
                                            User_Id INT,
                                            FOREIGN KEY (User_Id) REFERENCES Users(Id)
                                            )""")

my_cursor.execute("""CREATE TABLE Countries (Id INT AUTO_INCREMENT PRIMARY KEY,                                            
                                            Name VARCHAR(255) UNIQUE
                                            )""")                                              
                                        
my_cursor.execute("""CREATE TABLE Airline_Companies (Id INT AUTO_INCREMENT PRIMARY KEY, 
                                            Name VARCHAR(255) UNIQUE,
                                            Country_Id INT,
                                            FOREIGN KEY (Country_Id) REFERENCES Countries(Id),
                                            User_Id INT,
                                            FOREIGN KEY (User_Id) REFERENCES Users(Id)
                                            )""")

my_cursor.execute("""CREATE TABLE Flights (Id INT AUTO_INCREMENT PRIMARY KEY,                                            
                                            Airline_Company_Id INT,
                                            FOREIGN KEY (Airline_Company_Id) REFERENCES Airline_Companies(Id),
                                            Origin_Country_Id INT,
                                            FOREIGN KEY (Origin_Country_Id) REFERENCES Countries(Id),
                                            Destination_Country_Id INT,
                                            FOREIGN KEY (Destination_Country_Id) REFERENCES Countries(Id),
                                            Departure_Time DATETIME, 
                                            Lending_Time DATETIME,
                                            Remaining_Tickets INT
                                            )""")    

my_cursor.execute("""CREATE TABLE Tickets (Id INT AUTO_INCREMENT PRIMARY KEY,                                            
                                            Flight_Id INT,
                                            FOREIGN KEY (Flight_Id) REFERENCES Flights(Id),
                                            Customer_Id INT,
                                            FOREIGN KEY (Customer_Id) REFERENCES Customers(Id)
                                            )""")
                                            #TODO flight_ID and Customer_ID combination should be Unique


# my_cursor.execute("INSERT INTO Users (Username, Password, Email) VALUES (%s, %s, %s)", ("Benda", "13579864", "Ofir6bd@gmail.com"))
# mydb.commit()

# my_cursor.execute("INSERT INTO Customers (First_Name, Last_Name, Address, Phone_No, Credit_Card_No, User_Id) VALUES (%s, %s, %s, %s, %s, %s)", ("Ofir", "Ben David", "Atlit Haharov 17", "0548105702", "65437634983498", 1))
# mydb.commit()

# my_cursor.execute("SELECT * FROM Customers")
# my_result = my_cursor.fetchall()

# for x in my_result:
#   print(x)

# my_cursor.execute("SELECT * FROM Users")
# my_result = my_cursor.fetchall()

# for x in my_result:
#   print(x)


my_cursor.close()
mydb.close()