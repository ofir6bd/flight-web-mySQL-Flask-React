# Register route
import sys
import os
 
# import a module in the parent
current = os.path.dirname(os.path.realpath(__file__))
# Getting the parent directory name
parent = os.path.dirname(current)
# adding the parent directory to the sys.path.
sys.path.append(parent)
from Forms_templates.customer_forms import update_customer_form
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
        customer_id = customer_details,
        text=full_name,
        title=customer_details,
        )

# @login_required
# @require_customer_role
# def add_ticket(customer):
#     form = add_ticket_form()
#     # fac_obj = CustomerFacade(user_id=customer)
#     # user = fac_obj.get_customer_by_user_id()
#     # full_name = f'{user.last_name}, {user.first_name}'
    
#     return render_template("customer/add_ticket.html",
#         customer = customer,
#         form=form,
#         text="Add ticket",
#         title="Add ticket",
#         btn_action="Add ticket",
#         )

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
def book_verification(flight_id):
    if request.method == "GET":
        return render_template("verification.html",
            text="are you sure you want to book this flight?",
            title="flight",
            btn_action="Book now"
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
                btn_action="Search"
                )