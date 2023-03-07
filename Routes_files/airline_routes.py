# Register route
import sys
import os
 
# import a module in the parent
current = os.path.dirname(os.path.realpath(__file__))
# Getting the parent directory name
parent = os.path.dirname(current)
# adding the parent directory to the sys.path.
sys.path.append(parent)
from Forms_templates.airline_forms import add_flight_form
# from Facades.AnonymousFacade import AnonymousFacade
# from Facades.CustomerFacade import CustomerFacade
from flask import Flask, redirect, url_for,request, render_template, session, flash
from flask_login import UserMixin, login_user, LoginManager,login_required, logout_user,current_user
from per_req_Wrappers import require_airline_role
from Facades.AirlineFacade import AirlineFacade


@login_required
@require_airline_role
def company_home(company_name):
    return render_template("airline/company_home.html",
        airline_name = company_name,
        text=company_name,
        title=company_name,
        )

@login_required
@require_airline_role
def add_flight(company_name):
    form = add_flight_form() 
    if form.validate_on_submit():
        fac_obj = AirlineFacade(id=form.airline_company_id.data)
        airline = fac_obj.get_airline_by_id()
        fac_obj = AirlineFacade(id=form.origin_country_id.data)
        origin_country_id = fac_obj.get_country_by_id()
        fac_obj = AirlineFacade(id=form.destination_country_id.data)
        destination_country_id = fac_obj.get_country_by_id()
        
        fac_obj = AirlineFacade(airline_company_id=airline.id,
                                origin_country_id=origin_country_id.id,
                                destination_country_id=destination_country_id.id,
                                departure_time=form.departure_time.data,
                                landing_time=form.landing_time.data,
                                remaining_tickets=2)
        res = fac_obj.add_flight()
        if res:
            flash(f"Flight added", "success")
        return redirect(url_for('company_home',company_name=company_name))
    return render_template("airline/add_flight.html",
        airline_name = company_name,
        form=form,
        text="Add flight",
        title="Add flight",
        btn_action="Add flight",
        )