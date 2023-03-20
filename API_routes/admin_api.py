"""
That data can be used to GET, PUT (updade), POST (Add) and DELETE data types,
 which refers to the reading, updating, creating and deleting
 of operations concerning resources.
"""# Register route
import sys
import os
 
# import a module in the parent
current = os.path.dirname(os.path.realpath(__file__))
# Getting the parent directory name
parent = os.path.dirname(current)
# adding the parent directory to the sys.path.
sys.path.append(parent)
from Forms_templates.customer_forms import update_customer_form,remove_ticket_form
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
from API_routes.api_validation import *

@require_api_auth
def api_get_all_customers():
    if not current_user.is_authenticated:
        return jsonify({ 'error': 'Email or password are incorrect'})
    else:
        if session['user_role'] == 'admin':
            dal_obj = AnonymousFacade(api=True)
            return dal_obj.get_all_customers()
        else:
            return jsonify({ 'error': 'you do not have admin permissions'}) 

@require_api_auth
def api_delete_customer(customer_id):
    if not current_user.is_authenticated:
        return jsonify({ 'error': 'Email or password are incorrect'})
    else:
        if session['user_role'] == 'admin':
            fac_obj = AdministratorFacade(api=True,id=customer_id)
            customer = fac_obj.get_customer_by_id()
            if customer: 
                res = fac_obj.remove_customer()
                if res:
                    return jsonify({ 'result': 'Customer removed'}) 
                else:
                    return jsonify({ 'error': 'Cannot delete Customer, ticket is associated with'})  
            else:
                return jsonify({ 'Error': 'Customer not found'}) 
        else:
            return jsonify({ 'error': 'you do not have admin permissions'})            

@require_api_auth
def api_delete_airline(airline_id):
    if not current_user.is_authenticated:
        return jsonify({ 'error': 'Email or password are incorrect'})
    else:
        if session['user_role'] == 'admin':
            fac_obj = AdministratorFacade(api=True,id=airline_id)
            airline = fac_obj.get_airline_by_id()
            if airline: 
                res = fac_obj.remove_airline()
                if res:
                    return jsonify({ 'result': 'Airline removed'}) 
                else:
                    return jsonify({ 'error': 'Cannot delete Airline, flight is associated with'})  
            else:
                return jsonify({ 'Error': 'Airline not found'}) 
        else:
            return jsonify({ 'error': 'you do not have admin permissions'})  

@require_api_auth
def api_delete_admin(admin_id):
    if not current_user.is_authenticated:
        return jsonify({ 'error': 'Email or password are incorrect'})
    else:
        if session['user_role'] == 'admin':
            fac_obj = AdministratorFacade(api=True,id=admin_id)
            admin = fac_obj.get_admin_by_id()
            if admin: 
                if admin.id != session['admin_id']:
                    res = fac_obj.remove_administrator()
                    if res:
                        return jsonify({ 'result': 'Admin removed'}) 
                    else:
                        return jsonify({ 'error': 'error_occured'})
                else:
                    return jsonify({ 'error': 'You cannot remove yourself'})  
            else:
                return jsonify({ 'Error': 'Admin not found'}) 
        else:
            return jsonify({ 'error': 'you do not have admin permissions'})  
        
@require_api_auth
def api_add_admin():
    if not current_user.is_authenticated:
        return jsonify({ 'error': 'Email or password are incorrect'})
    else:
        if session['user_role'] == 'admin':
            first_name = request.args.get('first_name')
            last_name = request.args.get('last_name')
            user_id = request.args.get('user_id')
            if first_name and last_name and user_id:
                fac_obj = AdministratorFacade(api=True,first_name=first_name,last_name=last_name,user_id=user_id)
                res = fac_obj.add_administrator()
                if res: 
                    return jsonify({ 'result': 'Admin added'}) 
                else:
                    return jsonify({ 'error': 'an admin already exists with that user id'})
            else:
                return jsonify({ 'error': 'one of more parameters are missing'})
        else:
            return jsonify({ 'error': 'you do not have admin permissions'})  
        
@require_api_auth
def api_add_customer():
    if not current_user.is_authenticated:
        return jsonify({ 'error': 'Email or password are incorrect'})
    else:
        if session['user_role'] == 'admin':
            first_name = request.args.get('first_name')
            last_name = request.args.get('last_name')
            address = request.args.get('address')
            phone_no = request.args.get('phone_no')
            credit_card_no = request.args.get('credit_card_no')
            user_id = request.args.get('user_id')

            if first_name and last_name and user_id and address and phone_no and credit_card_no and user_id:
                res = validate_customer(first_name=first_name,last_name=last_name,address=address,\
                                              phone_no=phone_no,credit_card_no=credit_card_no,user_id=user_id)
                if res:
                    return jsonify(res)
                fac_obj = AdministratorFacade(api=True,first_name=first_name,last_name=last_name,address=address,\
                                              phone_no=phone_no,credit_card_no=credit_card_no,user_id=user_id)
                res = fac_obj.add_customer()
                if res: 
                    return jsonify({ 'result': 'Customer added'}) 
                else:
                    return jsonify({ 'error': 'duplication error in DB'})
            else:
                return jsonify({ 'error': 'one of more parameters are missing'})
        else:
            return jsonify({ 'error': 'you do not have admin permissions'})  
        
@require_api_auth
def api_add_airline():
    if not current_user.is_authenticated:
        return jsonify({ 'error': 'Email or password are incorrect'})
    else:
        if session['user_role'] == 'admin':
            name = request.args.get('name')
            country_id = request.args.get('country_id')
            user_id = request.args.get('user_id')

            if name and country_id and user_id:
                res = validate_airline(name=name,country_id=country_id,user_id=user_id)
                if res:
                    return jsonify(res)
                fac_obj = AdministratorFacade(api=True,name=name,country_id=country_id,user_id=user_id)
                res = fac_obj.add_airline()
                if res: 
                    return jsonify({ 'result': 'Airline added'}) 
                else:
                    return jsonify({ 'error': 'a airline already exists with that user id'})
            else:
                return jsonify({ 'error': 'one of more parameters are missing'})
        else:
            return jsonify({ 'error': 'you do not have admin permissions'})  