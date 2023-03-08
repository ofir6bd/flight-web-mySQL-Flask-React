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
from Forms_templates.general_forms import search_flights_form
from per_req_Wrappers import *
from Routes_files.customer_routes import update_customer,customer_home
from Routes_files.airline_routes import add_flight,company_home,remove_flight
from Routes_files.admin_routes import add_airline,add_customer,add_admin,remove_airline,remove_customer,remove_admin

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
    form = search_flights_form()
    if request.method == "GET":
        return render_template("index.html",
            form=form,
            text="Book your next flight today with us!",
            title="Home",
            btn_action="Search"
            )
    if request.method == "POST":
        origin_country = form.origin_country.data
        destination_country = form.destination_country.data
        departure_time = form.departure_time.data
        landing_time = form.landing_time.data

        fac_obj = AnonymousFacade(origin_country=origin_country,destination_country=destination_country)
        flights = fac_obj.get_flights_by_parameters()
        return render_template("flights.html",
            form=form,
            text="Book your next flight today with us!",
            title="Home",
            btn_action="Search",
            flights=flights,
            )

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
                session['user_id'] = user.id

                fac_obj = AnonymousFacade(user_id=int(user.id))
                admin = fac_obj.get_admin_by_user_id()
                airline = fac_obj.get_airline_by_user_id()
                customer = fac_obj.get_customer_by_user_id()
                if admin:
                    session['user_role'] = 'admin'
                elif airline:
                    session['user_role'] = 'airline'
                    return redirect(url_for('company_home',company_name=airline.name))
                elif customer:
                    session['user_role'] = 'customer'
                    return redirect(url_for('customer_home',customer=customer.user_id))
                else:
                    session['user_role'] = 'general_user'
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
        role = form.role.data
               
        fac_obj = AnonymousFacade(username=username,password=password,email=email,user_role=role)
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
    session.pop('user_id', None)
    session.pop('user_role', None)
    return redirect(url_for('login'))    

# Customer routes
app.add_url_rule('/<string:customer>/', view_func=customer_home,  methods=("GET", "POST"), strict_slashes=False)
app.add_url_rule('/<string:customer>/update_customer', view_func=update_customer, methods=("GET", "POST"), strict_slashes=False)

# admin routes
app.add_url_rule('/add_airline', view_func=add_airline,  methods=("GET", "POST"), strict_slashes=False)
app.add_url_rule('/add_customer', view_func=add_customer,  methods=("GET", "POST"), strict_slashes=False)
app.add_url_rule('/add_admin', view_func=add_admin,  methods=("GET", "POST"), strict_slashes=False)
app.add_url_rule('/remove_airline', view_func=remove_airline,  methods=("GET", "POST"), strict_slashes=False)
app.add_url_rule('/remove_customer', view_func=remove_customer,  methods=("GET", "POST"), strict_slashes=False)
app.add_url_rule('/remove_admin', view_func=remove_admin,  methods=("GET", "POST"), strict_slashes=False)

# Airline company routes
app.add_url_rule('/<string:company_name>/', view_func=company_home,  methods=("GET", "POST"), strict_slashes=False)
app.add_url_rule('/<string:company_name>/add_flight', view_func=add_flight,  methods=("GET", "POST"), strict_slashes=False)
app.add_url_rule('/<string:company_name>/remove_flight', view_func=remove_flight,  methods=("GET", "POST"), strict_slashes=False)


if __name__ == "__main__":
    app.run(debug=True)