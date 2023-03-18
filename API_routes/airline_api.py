"""
That data can be used to GET, PUT, POST and DELETE data types,
 which refers to the reading, updating, creating and deleting
 of operations concerning resources.
"""# Register route
import sys
import os
from datetime import datetime
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
def api_get_my_flights():
    if not current_user.is_authenticated:
        return jsonify({ 'error': 'email or password are incorrect'})
    else:
        if session['user_role'] == 'airline':
            fac_obj = AirlineFacade(api=True,id=session['airline_id'])
            airline = fac_obj.get_airline_by_id()
            fac_obj.name = airline.name
            return fac_obj.get_my_flights()

        
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
            return jsonify({ 'error': 'you do not have airline permissions'})

@require_api_auth
def api_add_flight():
    if not current_user.is_authenticated:
        return jsonify({ 'error': 'Email or password are incorrect'})
    else:
        if session['user_role'] == 'airline':
            airline_company_id = session['airline_id']
            origin_country_id = int(request.args.get('origin_country_id'))
            destination_country_id = int(request.args.get('destination_country_id'))
            departure_time = datetime.strptime(request.args.get('departure_time'), '%Y-%m-%dT%H:%M')
            landing_time = datetime.strptime(request.args.get('landing_time'), '%Y-%m-%dT%H:%M')
            remaining_tickets = int(request.args.get('remaining_tickets'))

            if airline_company_id and origin_country_id and destination_country_id and departure_time and landing_time and remaining_tickets:
                fac_obj = AirlineFacade(api=True,airline_company_id=airline_company_id,origin_country_id=origin_country_id,destination_country_id=destination_country_id,\
                                        departure_time=departure_time,landing_time=landing_time,remaining_tickets=remaining_tickets)
                res = fac_obj.add_flight()
                if res: 
                    return jsonify({ 'result': 'Flight added'}) 
                else:
                    return jsonify({ 'error': 'error occured'})
            else:
                return jsonify({ 'error': 'one of more parameters are missing'})
        else:
            return jsonify({ 'error': 'you do not have airline permissions'})  
        

@require_api_auth
def api_update_airline():
    if not current_user.is_authenticated:
        return jsonify({ 'error': 'Email or password are incorrect'})
    else:
        if session['user_role'] == 'airline':
            id = session['airline_id']
            name = request.args.get('name')
            
            fac_obj = AirlineFacade(api=True,id=id,name=name)
            res = fac_obj.update_airline()
            if res: 
                return jsonify({ 'result': 'Airline updated'}) 
            else:
                return jsonify({ 'error': 'error_occured'})
        else:
            return jsonify({ 'error': 'you do not have airline permissions'})  