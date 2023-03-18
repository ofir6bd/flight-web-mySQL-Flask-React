"""
That data can be used to GET, PUT, POST and DELETE data types,
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


# def delete_sessions():
#     session.pop('user_id', None)
#     session.pop('user_role', None)
#     session.pop('admin_id', None)
#     session.pop('airline_id', None)
#     session.pop('customer_id', None)

# def api_login(email,password):
#     fac_obj = CustomerFacade(email=email)
#     user = fac_obj.get_user_by_email()
#     if check_password_hash(user.password, password):
#         login_user(user)
#         session['user_id'] = user.id

#         fac_obj = AnonymousFacade(user_id=int(user.id))
#         admin = fac_obj.get_admin_by_user_id()
#         airline = fac_obj.get_airline_by_user_id()
#         customer = fac_obj.get_customer_by_user_id()

#         if admin:
#             session['user_role'] = 'admin'
#             session['admin_id'] = admin.id
#         elif airline:
#             session['user_role'] = 'airline'
#             session['airline_id'] = airline.id
#         elif customer:
#             session['user_role'] = 'customer'
#             session['customer_id'] = customer.id
#         else:
#             session['user_role'] = 'general_user'
#     return

def api_get_all_countries():
    dal_obj = AnonymousFacade(api=True)
    return dal_obj.get_all_countries()

def api_get_all_flights():
    dal_obj = AnonymousFacade(api=True)
    return dal_obj.get_all_flights()

@require_api_auth
def api_get_my_tickets():
    if not current_user.is_authenticated:
        return jsonify({ 'error': 'email or password are incorrect'})
    else:
        if session['user_role'] == 'customer':
            fac_obj = CustomerFacade(api=True,customer_id=session['customer_id'])
            return fac_obj.get_my_ticket()

@require_api_auth
def api_delete_my_ticket(ticket_id):
    if not current_user.is_authenticated:
        return jsonify({ 'error': 'Email or password are incorrect'})
    else:
        if session['user_role'] == 'customer':
            fac_obj = CustomerFacade(api=True,id=ticket_id)
            ticket = fac_obj.get_ticket_by_id()
            if ticket:
                if ticket.customer_id == session['customer_id']:
                    res = fac_obj.remove_ticket()
                    if res:
                        return jsonify({ 'result': 'Ticket removed'}) 
                    else:
                        return jsonify({ 'error': 'error occured'})
                else:
                    return jsonify({ 'error': 'Cannot delete ticket that is not yours'}) 
            else:
                return jsonify({ 'Error': 'Ticket not found'}) 
        else:
            return jsonify({ 'error': 'you do not have customer role'})
    
        
@require_api_auth
def api_delete_my_flight(flight_id):
    if not current_user.is_authenticated:
        return jsonify({ 'error': 'Email or password are incorrect'})
    else:
        if session['user_role'] == 'airline':
            fac_obj = AirlineFacade(api=True,id=flight_id)
            flight = fac_obj.get_flight_by_id()
            if flight:
                if flight.airline_company_id == session['airline_id']:
                    res = fac_obj.remove_flight()
                    if res:
                        return jsonify({ 'result': 'Flight removed'}) 
                    else:
                        return jsonify({ 'error': 'Cannot delete flight, ticket is associated with'})
                else:
                    return jsonify({ 'error': 'Cannot delete flight that is not yours'}) 
            else:
                return jsonify({ 'Error': 'flight not found'}) 
        else:
            return jsonify({ 'error': 'you do not have airline role'})

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
            return jsonify({ 'error': 'you do not have admin role'})            

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
            return jsonify({ 'error': 'you do not have admin role'})  