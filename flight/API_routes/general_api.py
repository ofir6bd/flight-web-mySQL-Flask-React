"""
That data can be used to GET, PUT (updade), POST (Add) and DELETE data types,
 which refers to the reading, updating, creating and deleting
 of operations concerning resources.
"""
import sys
import os
from app import bcrypt
# import a module in the parent
current = os.path.dirname(os.path.realpath(__file__))
# Getting the parent directory name
parent = os.path.dirname(current)
# adding the parent directory to the sys.path.
sys.path.append(parent)

from flask import request, session
from flask_login import current_user
from Facades.AnonymousFacade import AnonymousFacade
from flask import jsonify
from per_req_Wrappers import require_api_auth
from API_routes.api_validation import *
from flask_bcrypt import check_password_hash

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
    
def api_check_login():
    email = request.args.get('email')
    password = request.args.get('password')
    fac_obj = AnonymousFacade(email=email)
    user = fac_obj.get_user_by_email()
    if check_password_hash(user.password, password):
        return jsonify({ 'success': 'email and password are correct'})
    else:
        return jsonify({ 'error': 'one of the parameters failed'})
    
def api_create_new_user():
    username = request.args.get('username')
    password = request.args.get('password')
    email = request.args.get('email')
    user_role = request.args.get('user_role')

    res = validate_user(username=username,password=password,email=email,user_role=user_role)
    if res:
        return jsonify(res)
    
    password = bcrypt.generate_password_hash(password) # encrypt password
    
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
            res = validate_customer(first_name=first_name,last_name=last_name,address=address,\
                                              phone_no=phone_no,credit_card_no=credit_card_no,user_id=user_id)
            if res:
                return jsonify(res)
            
            fac_obj = AnonymousFacade(api=True,first_name=first_name,last_name=last_name,address=address,\
                                            phone_no=phone_no,credit_card_no=credit_card_no,user_id=user_id)
            res = fac_obj.add_customer()
            if res: 
                return jsonify({ 'result': 'Customer added'}) 
            else:
                return jsonify({ 'error': 'error_occured'})
        else:
            return jsonify({ 'error': 'one of more parameters are missing'})
        

