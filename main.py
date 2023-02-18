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

@app.route('/insert-user',methods=['POST'])                   # 1st option to create view - the home route http://127.0.0.1:5000
def insertUser():  
    if request.method == 'POST':
        Role_Name = request.args['Role_Name']
        Username = request.args['Username']
        Password = request.args['Password']
        Email = request.args['Email']
        First_Name = request.args['First_Name']
        Last_Name = request.args['Last_Name']
        Address = request.args['Address']
        Phone_No = request.args['Phone_No']
        Credit_Card_No = request.args['Credit_Card_No']
        try:
            my_cursor.execute("INSERT INTO User_Roles (Role_Name) VALUES (%s)", (Role_Name,))
            my_cursor.execute("INSERT INTO Users (Username, Password, Email) VALUES (%s, %s, %s)", (Username, Password, Email))
            #TODO need to add if statement, administartor only if admin
            my_cursor.execute("INSERT INTO Administrators (First_Name, Last_Name) VALUES (%s, %s)", (First_Name, Last_Name))
            my_cursor.execute("INSERT INTO Customers (First_Name, Last_Name, Address, Phone_No, Credit_Card_No) VALUES (%s, %s, %s, %s, %s)", (First_Name, Last_Name, Address, Phone_No, Credit_Card_No))
            mydb.commit()
        except mysql.connector.errors.ProgrammingError as e:
            print(f"Error: {e}")
        return 'user inserted'

@app.route('/',methods=['GET','POST'])                   # 1st option to create view - the home route http://127.0.0.1:5000
def hello():   
    print('**********Starting main route')               				             # this function is the name of the route
    if request.method == 'GET':
        print('**********Starting GET main route')
        return render_template('home.html')        # render a template
     
    if request.method == 'POST':
        print('**********Starting POST at main route')
        print(request)
        
        return render_template('flight.html')
        
@app.route('/Countries',methods=['GET','POST'])                   # 1st option to create view - the home route http://127.0.0.1:5000
def countriesFunc():       
    if request.method == 'GET':
        print('**********Starting GET Countries route')
        return render_template('home.html')      
     
    if request.method == 'POST':
        print('**********Starting POST at main route')
        print(request.args)
        return render_template('flight.html')      

@app.route('/flight',methods=['GET','POST'])
def hello2():
      print(request)
      return render_template('home.html')


# info functions
@app.route("/country/<string:name>")
def getAirlinesByCountry(name):
    print('start')
    try:
        my_cursor.execute("""SELECT * FROM Countries WHERE Name = %s""", (name,))
        country = my_cursor.fetchone()
        # return render_template('user.html', user = user)  
        print(country)
    except mysql.connector.errors.ProgrammingError as e:
        print(f"Error: {e}")  
    return render_template('home.html') 



if __name__ == "__main__":
    app.debug = True
    app.run();
