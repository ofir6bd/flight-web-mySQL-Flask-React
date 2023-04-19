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

def api_get_flights_by_param():
    if request.args.get('origin_country_id'):
        origin_country_id = int(request.args.get('origin_country_id'))
    else: 
        origin_country_id = "0"
    if request.args.get('destination_country_id'):
        destination_country_id = int(request.args.get('destination_country_id'))
    else: 
        destination_country_id = "0"
    if request.args.get('departure_time'):
        departure_time = datetime.strptime(request.args.get('departure_time'), '%Y-%m-%dT%H:%M')
    else: 
        departure_time = None
    if request.args.get('landing_time'):
        landing_time = datetime.strptime(request.args.get('landing_time'), '%Y-%m-%dT%H:%M')
    else: 
        landing_time = None
    fac_obj = AnonymousFacade(api=True,origin_country=origin_country_id,destination_country=destination_country_id,\
                                departure_time=departure_time,landing_time=landing_time)
    return fac_obj.get_flights_by_parameters()

def api_get_all_countries():
    fac_obj = AnonymousFacade(api=True)
    return fac_obj.get_all_countries()

def api_get_all_user_roles():
    fac_obj = AnonymousFacade(api=True)
    return fac_obj.get_all_user_roles()

def api_get_all_airlines():
    fac_obj = AnonymousFacade(api=True)
    return fac_obj.get_all_airlines()

def api_get_all_flights():
    fac_obj = AnonymousFacade(api=True)
    return fac_obj.get_all_flights()

def api_get_flight_by_id(flight_id):
    fac_obj = AnonymousFacade(api=True,id=flight_id)
    res = fac_obj.get_flight_by_id()
    if res:
        return res
    else:
        return jsonify({ 'error': 'flight not found'})

def api_get_country_by_id(country_id):
    fac_obj = AnonymousFacade(api=True,id=country_id)
    res = fac_obj.get_country_by_id()
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
        return jsonify({ 'success': 'email and password are correct', 'user_id': user.id})
    else:
        return jsonify({ 'error': 'one of the parameters are wrong'})
    
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
            return jsonify({ 'success': 'user added'}) 
        else:
            return jsonify({ 'error': 'error occured'})
    else:
        return jsonify({ 'error': 'one of more parameters are'})

@require_api_auth
def api_get_admin_by_user_id():
    user_id = request.args.get('user_id')
    if not current_user.is_authenticated:
        return jsonify({ 'error': 'Email or password are incorrect'})
    else:    
        fac_obj = AdministratorFacade(user_id=user_id)
        admin = fac_obj.get_admin_by_user_id()
        if admin:
            return jsonify({'success': "user is admin",  'admin_id': admin.id})
        else:
            return jsonify({'error': "no user found"})

@require_api_auth
def api_get_customer_by_user_id():
    user_id = request.args.get('user_id')
    if not current_user.is_authenticated:
        return jsonify({ 'error': 'Email or password are incorrect'})
    else:    
        fac_obj = CustomerFacade(user_id=user_id)
        customer = fac_obj.get_customer_by_user_id()
        if customer:
            return jsonify({'success': "user is customer",  'customer_id': customer.id})
        else:
            return jsonify({'error': "no user found"})

@require_api_auth
def api_get_airline_by_user_id():
    user_id = request.args.get('user_id')
    if not current_user.is_authenticated:
        return jsonify({ 'error': 'Email or password are incorrect'})
    else:    
        fac_obj = AirlineFacade(user_id=user_id)
        airline = fac_obj.get_airline_by_user_id()
        if airline:
            return jsonify({'success': "user is airline",  'airline_id': airline.id})
        else:
            return jsonify({'error': "no user found"})

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
                return jsonify({ 'success': 'Customer added'}) 
            else:
                return jsonify({ 'error': 'error_occured'})
        else:
            return jsonify({ 'error': 'one of more parameters are missing'})
        

