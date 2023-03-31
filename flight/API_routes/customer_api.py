"""
That data can be used to GET, PUT, POST and DELETE data types,
 which refers to the reading, updating, creating and deleting
 of operations concerning resources.
"""
import sys
import os
 
# import a module in the parent
current = os.path.dirname(os.path.realpath(__file__))
# Getting the parent directory name
parent = os.path.dirname(current)
# adding the parent directory to the sys.path.
sys.path.append(parent)

from flask import request, session
from flask_login import current_user
from Facades.CustomerFacade import CustomerFacade
from flask import jsonify
from per_req_Wrappers import require_api_auth
from API_routes.api_validation import *

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
                        return jsonify({ 'error': 'a customer already exists with that user id/phone no or creadit card number'})
                else:
                    return jsonify({ 'error': 'Cannot delete ticket that is not yours'}) 
            else:
                return jsonify({ 'Error': 'Ticket not found'}) 
        else:
            return jsonify({ 'error': 'you do not have customer role'})
    
@require_api_auth
def api_add_ticket():
    if not current_user.is_authenticated:
        return jsonify({ 'error': 'Email or password are incorrect'})
    else:
        if session['user_role'] == 'customer':
            flight_id = request.args.get('flight_id')
            customer_id = session['customer_id']

            if flight_id and customer_id:
                res = validate_ticket(flight_id=flight_id,customer_id=customer_id)
                if res:
                    return jsonify(res)
                fac_obj = CustomerFacade(api=True,flight_id=flight_id,customer_id=customer_id)
                res = fac_obj.add_ticket()
                if res: 
                    return jsonify({ 'result': 'Ticket added'}) 
                else:
                    return jsonify({ 'error': 'Duplication error in DB'})
            else:
                return jsonify({ 'error': 'one of more parameters are missing'})
        else:
            return jsonify({ 'error': 'you do not have cutomer permissions'})  
        

@require_api_auth
def api_update_customer():
    if not current_user.is_authenticated:
        return jsonify({ 'error': 'Email or password are incorrect'})
    else:
        if session['user_role'] == 'customer':
            id = session['customer_id']
            first_name = request.args.get('first_name')
            last_name = request.args.get('last_name')
            address = request.args.get('address')
            phone_no = request.args.get('phone_no')
            credit_card_no = request.args.get('credit_card_no')
            user_id = session['user_id'] 

            res = validate_customer(action="update",first_name=first_name,last_name=last_name,address=address,\
                                              phone_no=phone_no,credit_card_no=credit_card_no)
            if res:
                return jsonify(res)


            fac_obj = CustomerFacade(api=True,id=id,first_name=first_name,last_name=last_name,address=address,\
                                                phone_no=phone_no,credit_card_no=credit_card_no,user_id=user_id)
            
            res = fac_obj.update_customer()
            if res: 
                return jsonify({ 'result': 'Customer updated'}) 
            else:
                return jsonify({ 'error': 'Duplication error in DB'})
        else:
            return jsonify({ 'error': 'you do not have cutomer permissions'})  