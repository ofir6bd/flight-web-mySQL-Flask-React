
from functools import wraps
from flask import Flask, redirect, url_for,request, render_template, session, flash

# admin wrapper 
def require_admin_role(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        if session['user_role'] != 1:
            flash('You are not authorized to open the requested page, welcome back to home page!')
            return redirect(url_for('index'))  
        return func(*args, **kwargs)
    return wrapper


# airline wrapper 
def require_airline_role(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        if session['user_role'] != 2:
            flash('You are not authorized to open the requested page, welcome back to home page!')
            return redirect(url_for('index'))  
        return func(*args, **kwargs)
    return wrapper

# customer wrapper 
def require_customer_role(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        if session['user_role'] != 3:
            flash('You are not authorized to open the requested page, welcome back to home page!')
            return redirect(url_for('index'))  
        return func(*args, **kwargs)
    return wrapper
