
from functools import wraps
from flask import Flask, redirect, url_for,request, render_template, session, flash

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
