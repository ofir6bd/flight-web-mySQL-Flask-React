"""
That data can be used to GET, PUT, POST and DELETE data types,
 which refers to the reading, updating, creating and deleting
 of operations concerning resources.
"""
import sys
import os
from datetime import datetime
# import a module in the parent
current = os.path.dirname(os.path.realpath(__file__))
# Getting the parent directory name
parent = os.path.dirname(current)
# adding the parent directory to the sys.path.
sys.path.append(parent)

from flask import request, session
from flask_login import current_user
from Facades.AirlineFacade import AirlineFacade
from flask import jsonify
from per_req_Wrappers import require_api_auth
from API_routes.api_validation import *


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
            print(type(flight))
            if flight:
                print(flight)
                print(session['airline_id'])
                if flight.airline_company_id == session['airline_id']:
                    res = fac_obj.remove_flight()
                    if res:
                        return jsonify({ 'success': 'Flight removed'}) 
                    else:
                        return jsonify({ 'error': 'Cannot delete flight, ticket is associated with'})
                else:
                    return jsonify({ 'error': 'Cannot delete flight that is not yours'}) 
            else:
                return jsonify({ 'error': 'flight not found'}) 
        else:
            return jsonify({ 'error': 'you do not have airline permissions'})

@require_api_auth
def api_add_flight():
    if not current_user.is_authenticated:
        return jsonify({ 'error': 'Email or password are incorrect'})
    else:
        if session['user_role'] == 'airline':
            dep_time = request.args.get('departure_time')
            lan_time = request.args.get('landing_time')
            res = validate_dates(dep_time,lan_time)
            if res:
                return jsonify(res)
            airline_company_id = session['airline_id']
            origin_country_id = int(request.args.get('origin_country_id'))
            destination_country_id = int(request.args.get('destination_country_id'))
            departure_time = datetime.strptime(request.args.get('departure_time'), '%Y-%m-%dT%H:%M')
            landing_time = datetime.strptime(request.args.get('landing_time'), '%Y-%m-%dT%H:%M')
            remaining_tickets = int(request.args.get('remaining_tickets'))

            if airline_company_id and origin_country_id and destination_country_id and departure_time and landing_time and remaining_tickets:
                res = validate_flight(action="",origin_country_id=origin_country_id,destination_country_id=destination_country_id,\
                                        departure_time=departure_time,landing_time=landing_time,remaining_tickets=remaining_tickets)
                if res:
                    return jsonify(res)
                
                fac_obj = AirlineFacade(api=True,airline_company_id=airline_company_id,origin_country_id=origin_country_id,destination_country_id=destination_country_id,\
                                        departure_time=departure_time,landing_time=landing_time,remaining_tickets=remaining_tickets)
                res = fac_obj.add_flight()
                if res: 
                    return jsonify({ 'success': 'Flight added'}) 
                else:
                    return jsonify({ 'error': 'Duplication error in DB'})
            else:
                return jsonify({ 'error': 'one or more parameters are missing'})
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
            user_id = session['user_id']
            fac_obj = AirlineFacade(api=True,id=id)
            airline = fac_obj.get_airline_by_id()
            country_id = airline.country_id
            res = validate_airline(action="update", name=name,country_id=country_id,user_id=user_id)
            if res:
                return jsonify(res)
            
            fac_obj = AirlineFacade(api=True,id=id,name=name)
            res = fac_obj.update_airline()
            if res: 
                return jsonify({ 'success': 'Airline updated'}) 
            else:
                return jsonify({ 'error': 'Duplication error in DB'})
        else:
            return jsonify({ 'error': 'you do not have airline permissions'})  
        
@require_api_auth
def api_update_flight(flight_id):
    if not current_user.is_authenticated:
        return jsonify({ 'error': 'Email or password are incorrect'})
    else:
        if session['user_role'] == 'airline':
            fac_obj = AirlineFacade(id=flight_id)
            flight = fac_obj.get_flight_by_id()
            if flight:
                if flight.airline_company_id == session['airline_id']:
                    id = flight_id
                    airline_company_id = session['airline_id']
                    origin_country_id = request.args.get('origin_country_id')
                    destination_country_id = request.args.get('destination_country_id')
                    if request.args.get('departure_time'):
                        departure_time = datetime.strptime(request.args.get('departure_time'), '%Y-%m-%dT%H:%M')
                    else:
                        departure_time = ""
                    if request.args.get('landing_time'):
                        landing_time = datetime.strptime(request.args.get('landing_time'), '%Y-%m-%dT%H:%M')
                    else:
                        landing_time = ""
                    remaining_tickets = request.args.get('remaining_tickets')

                    res = validate_flight(action="update",id=id,origin_country_id=origin_country_id,destination_country_id=destination_country_id,\
                                        departure_time=departure_time,landing_time=landing_time,remaining_tickets=remaining_tickets)
                    if res:
                        return jsonify(res)
            
                    fac_obj = AirlineFacade(api=True,id=id,airline_company_id=airline_company_id,origin_country_id=origin_country_id,destination_country_id=destination_country_id,\
                                                departure_time=departure_time,landing_time=landing_time,remaining_tickets=remaining_tickets)
                    res = fac_obj.update_flight()
                    if res: 
                        return jsonify({ 'success': 'Flight updated'}) 
                    else:
                        return jsonify({ 'error': 'Duplication error in DB'})
                else:
                    return jsonify({ 'error': 'you cannot update flight that is not yours'})
            else:
                    return jsonify({ 'error': 'flight_not_found'})
        else:
            return jsonify({ 'error': 'you do not have airline permissions'})  
        
        
@require_api_auth
def api_get_airline_details():
    if not current_user.is_authenticated:
        return jsonify({ 'error': 'Email or password are incorrect'})
    else:
        if session['user_role'] == 'airline':
            id = session['airline_id']
            fac_obj = AirlineFacade(api=True,id=id)
            
            res = fac_obj.get_airline_by_id()
            if res: 
                return jsonify(res.toJson()) 
            else:
                return jsonify({ 'error': 'error'})
        else:
            return jsonify({ 'error': 'you do not have airline permissions'})  
        
