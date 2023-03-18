"""
That data can be used to GET, PUT (updade), POST (Add) and DELETE data types,
 which refers to the reading, updating, creating and deleting
 of operations concerning resources.
"""# Register route
import sys
import os
from app import create_app,db,login_manager,bcrypt
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
from flask_bcrypt import Bcrypt,generate_password_hash, check_password_hash
from per_req_Wrappers import require_api_auth


def api_get_all_countries():
    dal_obj = AnonymousFacade(api=True)
    return dal_obj.get_all_countries()

def api_get_all_flights():
    dal_obj = AnonymousFacade(api=True)
    return dal_obj.get_all_flights()

def api_get_flight_by_id(flight_id):
    dal_obj = AnonymousFacade(api=True,id=flight_id)
    res = dal_obj.get_flight_by_id()
    if res:
        return res
    else:
        return jsonify({ 'error': 'flight not found'})

def api_get_country_by_id(country_id):
    dal_obj = AnonymousFacade(api=True,id=country_id)
    res = dal_obj.get_country_by_id()
    if res:
        return res
    else:
        return jsonify({ 'error': 'country not found'})
    

def api_create_new_user():
    username = request.args.get('username')
    password = request.args.get('username')
    password = bcrypt.generate_password_hash(password) # encrypt password
    email = request.args.get('email')
    user_role = request.args.get('user_role')

    if username and password and email and user_role:
        fac_obj = AnonymousFacade(api=True,username=username,password=password,email=email,user_role=user_role)
        res = fac_obj.create_new_user()
        if res: 
            return jsonify({ 'result': 'user added'}) 
        else:
            return jsonify({ 'error': 'error occured'})
    else:
        return jsonify({ 'error': 'one of more parameters are'})

@require_api_auth
def api_register_as_customer():
    if not current_user.is_authenticated:
        return jsonify({ 'error': 'Email or password are incorrect'})
    else:    
        first_name = request.args.get('first_name')
        last_name = request.args.get('last_name')
        address = request.args.get('address')
        phone_no = request.args.get('phone_no')
        credit_card_no = request.args.get('credit_card_no')
        user_id = session['user_id'] 

        if first_name and last_name and user_id and address and phone_no and credit_card_no and user_id:
            fac_obj = AnonymousFacade(api=True,first_name=first_name,last_name=last_name,address=address,\
                                            phone_no=phone_no,credit_card_no=credit_card_no,user_id=user_id)
            res = fac_obj.add_customer()
            if res: 
                return jsonify({ 'result': 'Customer added'}) 
            else:
                return jsonify({ 'error': 'error_occured'})
        else:
            return jsonify({ 'error': 'one of more parameters are missing'})
        

