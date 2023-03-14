# Register route
import sys
import os
 
# import a module in the parent
current = os.path.dirname(os.path.realpath(__file__))
# Getting the parent directory name
parent = os.path.dirname(current)
# adding the parent directory to the sys.path.
sys.path.append(parent)
from Forms_templates.customer_forms import update_customer_form,remove_ticket_form
# from Facades.AnonymousFacade import AnonymousFacade
# from Facades.CustomerFacade import CustomerFacade
from flask import Flask, redirect, url_for,request, render_template, session, flash
from flask_login import UserMixin, login_user, LoginManager,login_required, logout_user,current_user
from per_req_Wrappers import require_customer_role
from Facades.CustomerFacade import CustomerFacade
from Facades.AnonymousFacade import AnonymousFacade
from Facades.AdministratorFacade import AdministratorFacade
from Facades.AirlineFacade import AirlineFacade
from Forms_templates.general_forms import search_flights_form
from flask import jsonify

# @login_required
# @require_customer_role
# def customer_home(customer_details):
#     fac_obj = CustomerFacade(user_id=customer_details)
#     user = fac_obj.get_customer_by_user_id()
#     full_name = f'{user.last_name}, {user.first_name}' 
#     return render_template("customer/customer_home.html",
#         customer_details = customer_details,
#         text=full_name,
#         title=customer_details,
#         )
# from app import create_app
# app = create_app()
# from models import UserRoles,Users,Administrators,Customers, Countries,AirlineCompanies,Flights,Tickets

def api_get_all_countries():
    dal_obj = AnonymousFacade(api=True)
    return dal_obj.get_all_countries()

def api_get_all_flights():
    dal_obj = AnonymousFacade(api=True)
    return dal_obj.get_all_flights()

def api_get_my_flights(email=None,password=None):
    pass
    # print(email)
    # print(password)
    # dal_obj = AnonymousFacade(email=email,password=password,api=True)
    # return dal_obj.get_all_flights()


