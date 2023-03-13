# Register route
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
from Forms_templates.general_forms import search_flights_form

@login_required
@require_customer_role
def customer_home(customer_details):
    fac_obj = CustomerFacade(user_id=customer_details)
    user = fac_obj.get_customer_by_user_id()
    full_name = f'{user.last_name}, {user.first_name}' 
    return render_template("customer/customer_home.html",
        customer_details = customer_details,
        text=full_name,
        title=customer_details,
        )


@login_required
@require_customer_role
def update_customer(customer_details):
    form = update_customer_form() 
    fac_obj = CustomerFacade(user_id=customer_details)
    customer = fac_obj.get_customer_by_user_id()
    first_name = customer.first_name
    last_name = customer.last_name
    address = customer.address
    phone_no = customer.phone_no
    credit_card_no = customer.credit_card_no

    if form.validate_on_submit():
        fac_obj = CustomerFacade(id=customer.id, first_name=form.first_name.data,last_name=form.last_name.data,address=form.address.data,phone_no=form.phone_no.data,credit_card_no=form.credit_card_no.data)
        res = fac_obj.update_customer()
        if res:
            flash(f"Customer detailes updated", "success")
        else:
            flash("error occurred", "danger")
        form = search_flights_form()
        return redirect(url_for('index',customer_details=customer_details))
    
    return render_template("customer/update_customer.html",
        first_name = first_name,
        last_name = last_name,
        address=address,
        phone_no=phone_no,
        credit_card_no=credit_card_no,
        customer_details = customer_details,
        form=form,
        text="Update customer",
        title="Update customer",
        btn_action="Update customer",
        )


@login_required
@require_customer_role
def book_verification(flight_id,customer_details):
    if request.method == "GET":
        return render_template("verification.html",
            text="are you sure you want to book this flight?",
            title="flight",
            btn_action="Book now",
            customer_details=customer_details
            )
    if request.method == "POST":
        fac_obj = CustomerFacade(flight_id=flight_id)
        res = fac_obj.add_ticket()
        if res:
            flash(f"Book suscesfully generated", "success")
            
        else:
            flash("error occurred", "danger")
        # form = search_flights_form()
        return redirect(url_for('index',customer_details=customer_details))
    

@login_required
@require_customer_role
def remove_ticket(customer_details):
    form = remove_ticket_form() 
    fac_obj = CustomerFacade(user_id=session['user_id'])
    customer = fac_obj.get_customer_by_user_id()
    fac_obj = CustomerFacade(customer_id=customer.id)
    all_customer_tickets = fac_obj.get_my_ticket()
    # print(all_customer_tickets)

    final_list = [(0, 'Choose which ticket')]
    print(len(all_customer_tickets))
    for ticket in all_customer_tickets:   
        full_tickets_details = f'ID:{ticket[0].id}, From:{ticket[1].name}, To:{ticket[2].name}, Departure Date:{ticket[0].departure_time}, Landing Date:{ticket[0].landing_time}'
        final_list.append((ticket[0].id, full_tickets_details ))
    
    form.tickets_detailes.choices = final_list

    if form.validate_on_submit():
        fac_obj = CustomerFacade(flight_id=form.tickets_detailes.data)
        ticket = fac_obj.get_ticket_by_flight_id()
        fac_obj = CustomerFacade(id=ticket.id)
        res = fac_obj.remove_ticket()
        if res:
            flash(f"Ticket removed", "success")
        return redirect(url_for('customer_home',customer_details=customer_details))

    return render_template("customer/remove_ticket.html",
        customer_details = customer_details,
        form=form,
        text="Remove ticket",
        title="Remove ticket",
        btn_action="Remove ticket",
        )