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
    print(current_user)
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
                    return jsonify({ 'error': 'Cannot delete flight that is not yours'}) 
            else:
                return jsonify({ 'Error': 'Ticket not found'}) 
    
        

            

