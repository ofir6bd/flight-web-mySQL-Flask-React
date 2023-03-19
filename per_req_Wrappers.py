
from functools import wraps
from flask import Flask, redirect, url_for,request, render_template, session, flash
from Facades.AnonymousFacade import AnonymousFacade
from flask_bcrypt import Bcrypt,generate_password_hash, check_password_hash
from flask_login import login_user,logout_user
# admin wrapper 
def require_admin_role(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        if session['user_role'] != 'admin':
            flash('You are not authorized to open the requested page, welcome back to home page!')
            return redirect(url_for('index'))  
        return func(*args, **kwargs)
    return wrapper


# airline wrapper 
def require_airline_role(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        if session['user_role'] != 'airline':
            flash('You are not authorized to open the requested page, welcome back to home page!')
            return redirect(url_for('index'))  
        return func(*args, **kwargs)
    return wrapper

# customer wrapper 
def require_customer_role(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        if session['user_role'] != 'customer':
            flash('You are not authorized to open the requested page, welcome back to home page!')
            return redirect(url_for('index'))  
        return func(*args, **kwargs)
    return wrapper


def api_login(email,password):
    fac_obj = AnonymousFacade(email=email)
    user = fac_obj.get_user_by_email()
    if check_password_hash(user.password, password):
        login_user(user)
        session['user_id'] = user.id

        fac_obj = AnonymousFacade(user_id=int(user.id))
        admin = fac_obj.get_admin_by_user_id()
        airline = fac_obj.get_airline_by_user_id()
        customer = fac_obj.get_customer_by_user_id()

        if admin:
            session['user_role'] = 'admin'
            session['admin_id'] = admin.id
        elif airline:
            session['user_role'] = 'airline'
            session['airline_id'] = airline.id
        elif customer:
            session['user_role'] = 'customer'
            session['customer_id'] = customer.id
        else:
            session['user_role'] = 'general_user'
            if user.user_role == 3:
                session['user_role_num'] = "pre_customer"
    return

# api wrapper 
def require_api_auth(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        email = request.args.get('email')
        password = request.args.get('password')
        api_login(email,password)
        res = func(*args, **kwargs) # calling the function
        logout_user()
        session.pop('user_id', None)
        session.pop('user_role', None)
        session.pop('admin_id', None)
        session.pop('airline_id', None)
        session.pop('customer_id', None)
        session.pop('user_role_num', None)
        return res
    return wrapper
