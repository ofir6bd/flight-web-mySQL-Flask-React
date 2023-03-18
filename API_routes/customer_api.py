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
    
   