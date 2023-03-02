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
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime
from flask_login import UserMixin
from forms import login_form,register_form
from app import create_app,db,login_manager,bcrypt
from models import UserRoles,Users,Administrators,Customers, Countries,AirlineCompanies,Flights,Tickets
from sqlalchemy.exc import (
    IntegrityError,
    DataError,
    DatabaseError,
    InterfaceError,
    InvalidRequestError,
)
from werkzeug.routing import BuildError


@login_manager.user_loader
def load_user(user_id):
    return Users.query.get(int(user_id))

app = create_app()

# Home route
@app.route("/", methods=("GET", "POST"), strict_slashes=False)
def index():
    return render_template("index.html",title="Home")

# Login route
@app.route("/login/", methods=("GET", "POST"), strict_slashes=False)
def login():
    form = login_form()

    return render_template("auth.html",form=form)


# Register route
@app.route("/register/", methods=("GET", "POST"), strict_slashes=False)
def register():
    form = register_form() 

    if form.validate_on_submit():        
        username = form.username.data
        password = form.pwd.data
        password = hashlib.md5(password.encode())
        # password=bcrypt.generate_password_hash(password) # encrypt password
        email = form.email.data
               
        fac_obj = AnonymousFacade(username=username,password=password,email=email,user_role=3)
        res = fac_obj.create_new_user()
        if res:
            flash(f"Account Succesfully created", "success")
            return redirect(url_for("login"))
        
    return render_template("auth.html",
        form=form,
        text="Create account",
        title="Register",
        btn_action="Register account"
        )

@app.route("/logout")
@login_required
def logout():
    logout_user()
    return redirect(url_for('login'))    

  
if __name__ == "__main__":
    app.run(debug=True)