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
