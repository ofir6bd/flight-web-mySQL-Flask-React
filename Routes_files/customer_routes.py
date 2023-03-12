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
def update_customer(customer):
    form = update_customer_form() 

    return render_template("customer/customer.html",
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
        form = search_flights_form()
        return render_template("index.html",
                form=form,
                text="Book your next flight today with us!",
                title="Home",
                btn_action="Search",
                customer_details=customer_details
                )
    

@login_required
@require_customer_role
def remove_ticket(customer_details):
    form = remove_ticket_form() 
    fac_obj = CustomerFacade(user_id=session['user_id'])
    customer = fac_obj.get_customer_by_user_id()
    fac_obj = CustomerFacade(customer_id=customer.id)
    all_customer_tickets = fac_obj.get_my_ticket()
    print(all_customer_tickets)
    # final_list = [(0, 'Choose which ticket')]
    # for i in all_company_flights:
    #     dal_obj1 = AirlineFacade(id=i.origin_country_id)
    #     origin = dal_obj1.get_country_by_id()
    #     dal_obj2 = AirlineFacade(id=i.destination_country_id)
    #     destination = dal_obj2.get_country_by_id()
    #     full_flight_details = f'{company_name}, From:{origin.name}, To:{destination.name}, Departure Date:{i.departure_time}, Landing Date:{i.landing_time}'
    #     final_list.append((i.id, full_flight_details ))

    # form.flights_detailes.choices = final_list

    # if form.validate_on_submit():
    #     fac_obj = AirlineFacade(id=form.flights_detailes.data)
    #     res = fac_obj.remove_flight()
        
    #     if res:
    #         flash(f"Flight removed", "success")
    #     return redirect(url_for('company_home',company_name=company_name))
    return render_template("airline/remove_flight.html",
        customer_details = customer_details,
        form=form,
        text="Remove flight",
        title="Remove flight",
        btn_action="Remove flight",
        )