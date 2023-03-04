from flask import Flask, redirect, url_for,request, render_template, session, flash
# from flask_mysqldb import MySQL
# import mysql.connector
# from flask_sqlalchemy import SQLAlchemy
from flask_login import UserMixin, login_user, LoginManager,login_required, logout_user,current_user
from Facades.AnonymousFacade import AnonymousFacade
from Facades.CustomerFacade import CustomerFacade
# from flask_wtf import FlaskForm
# from wtforms import StringField, PasswordField,SubmitField
# from wtforms.validators import DataRequired
import hashlib
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime
from flask_login import UserMixin
from flask_bcrypt import Bcrypt,generate_password_hash, check_password_hash
from auth_forms import login_form,register_form
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
from Forms_templates.customer_form import update_customer_form
from Forms_templates.admin_forms import add_airline_form
from functools import wraps

# from Routes_files.customer_routes import *

@login_manager.user_loader
def load_user(user_id):
    fac_obj = AnonymousFacade(id=user_id)
    return fac_obj.get_user_by_id()
    # return Users.query.get(int(user_id))

app = create_app()

# Home route
@app.route("/", methods=("GET", "POST"), strict_slashes=False)
def index():
    return render_template("index.html",title="Home")

# Login route
@app.route("/login/", methods=("GET", "POST"), strict_slashes=False)
def login():
    form = login_form()

    if form.validate_on_submit():
        try:
            fac_obj = CustomerFacade(email=form.email.data)
            user = fac_obj.get_user_by_email()
            if check_password_hash(user.password, form.password.data):
                login_user(user)
                print(user.id)
                session['user_id'] = user.id
                session['user_role'] = user.user_role
                return redirect(url_for('index'))
            else:
                flash("Invalid Username or password!", "danger")
        except Exception as e:
            flash(e, "danger")

    return render_template("auth.html",
        form=form,
        text="Login",
        title="Login",
        btn_action="Login"
        )


# Register route
@app.route("/register/", methods=("GET", "POST"), strict_slashes=False)
def register():
    form = register_form() 

    if form.validate_on_submit():        
        username = form.username.data
        password = form.password.data
        password=bcrypt.generate_password_hash(password) # encrypt password
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



# update_customer route
@app.route("/update_customer/", methods=("GET", "POST"), strict_slashes=False)
@login_required
def update_customer():
    form = update_customer_form() 

    return render_template("customer/customer.html",
        form=form,
        text="Update customer",
        title="Update customer",
        btn_action="Update customer",
        )

# @login_manager.unauthorized_handler
# def unauthorized():
#     # do stuff
#     return a_response


# admin wrapper 
def require_admin_role(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        if session['user_role'] != 1:
            return redirect(url_for('login'))  
        return func(*args, **kwargs)
    return wrapper

# update_customer route
@app.route("/add_airline/", methods=("GET", "POST"), strict_slashes=False)
@login_required
@require_admin_role
def add_airline():
    form = add_airline_form() 
    
    return render_template("admin/airline.html",
        form=form,
        text="add airline",
        title="add airline",
        btn_action="add airline",
        )

# def update_customer():
#     form = update_customer_form()
#     return render_template("auth.html",
#         form=form,
#         text="Create account",
#         title="Register",
#         btn_action="Register account"
#         )


# app.add_url_rule('/update_customer', view_func=update_customer)




if __name__ == "__main__":
    app.run(debug=True)