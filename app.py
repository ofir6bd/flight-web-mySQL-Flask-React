from flask import Flask, redirect, url_for,request, render_template, session, flash
# from flask_mysqldb import MySQL
# import mysql.connector
# from flask_sqlalchemy import SQLAlchemy
from flask_login import UserMixin, login_user, LoginManager,login_required, logout_user,current_user
from Facades.AnonymousFacade import AnonymousFacade
# from flask_wtf import FlaskForm
# from wtforms import StringField, PasswordField,SubmitField
# from wtforms.validators import DataRequired
import hashlib

app = Flask(__name__)          


@app.route('/add_user',methods=['GET','POST'])                   # 1st option to create view - the home route http://127.0.0.1:5000
def add_user(): 
    if request.method == 'GET':
        return render_template("customer/add_user.html")
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        hash_password= hashlib.md5(password.encode()) #encryption - hashing the passwored 
        print(hash_password)
        email = request.form['email']
        new_user = AnonymousFacade(username=username,password=hash_password,email=email,user_role=3)
        res = new_user.create_new_user()
        if res: 
            print("User added!")
        else: 
            print("error")
        return redirect(url_for("home"))


@app.route('/login',methods=['GET','POST'])
def login():
    if request.method=="GET":
        return render_template('login.html')
    elif request.method=="POST":
        username = request.form['username']
        password = request.form['password']
        user =AnonymousFacade(username=username,password=password)
        user_exists = user.login()
        if user_exists:
            # If user exists, set session variable and redirect to home page
            # session.permanent = True
            try:
                session["username"] = username 
            except Exception as e:
                print(f"Error: {e}")
            flash("Login Succesfuly!")
            return redirect(url_for("home"))
        else:
            error = 'Invalid username or password'
            return render_template('login.html', error=error)


@app.route('/',methods=['GET','POST'])                   # 1st option to create view - the home route http://127.0.0.1:5000
def home():   
    print('**********Starting main route')               				             # this function is the name of the route
    if request.method == 'GET':
        print('**********Starting GET main route')
        return render_template('home.html')        # render a template
     
    if request.method == 'POST':
        print('**********Starting POST at main route')
        print(request)
        
        return render_template('flight.html')
        
# @app.route('/Countries',methods=['GET','POST'])                   # 1st option to create view - the home route http://127.0.0.1:5000
# def countriesFunc():       
#     if request.method == 'GET':
#         print('**********Starting GET Countries route')
#         return render_template('home.html')      
     
#     if request.method == 'POST':
#         print('**********Starting POST at main route')
#         print(request.args)
#         return render_template('flight.html')      

@app.route('/flights',methods=['GET','POST'])
def flights_func():
    print('start flights_func')
    if request.method=='POST':
        print(request.form.get('destination'))
        destination = request.form.get('destination')
        print(destination)
    return render_template('flights.html', destination=destination)



if __name__ == "__main__":
    app.debug = True
    app.run()
