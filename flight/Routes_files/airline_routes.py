# Register route
import sys
import os
 
# import a module in the parent
current = os.path.dirname(os.path.realpath(__file__))
# Getting the parent directory name
parent = os.path.dirname(current)
# adding the parent directory to the sys.path.
sys.path.append(parent)

from Forms_templates.airline_forms import add_flight_form,remove_flight_form,update_airline_form,company_flights_form,update_flight_form
from flask import Flask, redirect, url_for, render_template, flash
from flask_login import login_required
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
    form.airline_company_id.choices = [(0, 'Airline company'),(1, company_name)]

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
                                remaining_tickets=form.remaining_tickets.data)
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

@login_required
@require_airline_role
def remove_flight(company_name):
    form = remove_flight_form() 
    fac_obj = AirlineFacade(name=company_name)
    all_company_flights = fac_obj.get_my_flights()
    final_list = [(0, 'Choose which flight')]
    for i in all_company_flights:
        dal_obj1 = AirlineFacade(id=i.origin_country_id)
        origin = dal_obj1.get_country_by_id()
        dal_obj2 = AirlineFacade(id=i.destination_country_id)
        destination = dal_obj2.get_country_by_id()
        full_flight_details = f'{company_name}, From:{origin.name}, To:{destination.name}, Departure Date:{i.departure_time}, Landing Date:{i.landing_time}'
        final_list.append((i.id, full_flight_details ))
    form.flights_detailes.choices = final_list
    if form.validate_on_submit():
        fac_obj = AirlineFacade(id=form.flights_detailes.data)
        res = fac_obj.remove_flight()
    
        if res:
            flash(f"Flight removed", "success")
        return redirect(url_for('company_home',company_name=company_name))
    return render_template("airline/remove_flight.html",
        airline_name = company_name,
        form=form,
        text="Remove flight",
        title="Remove flight",
        btn_action="Remove flight",
        )


@login_required
@require_airline_role
def update_airline(company_name):
    form = update_airline_form() 
    fac_obj = AirlineFacade(name=company_name)
    airline = fac_obj.get_airline_by_name()
    if form.validate_on_submit():
        fac_obj = AirlineFacade(id=airline.id, name=form.name.data)
        res = fac_obj.update_airline()
        if res:
            flash(f"Airline detailes updated", "success")
        else:
            flash("error occurred", "danger")
        return redirect(url_for('company_home',company_name=form.name.data))
    
    return render_template("airline/update_airline.html",
        name = airline.name,
        airline_name = company_name,
        form=form,
        text="Update airline",
        title="Update airline",
        btn_action="Update airline",
        )


@login_required
@require_airline_role
def update_flight(company_name):
    
    form = company_flights_form() 
    fac_obj = AirlineFacade(name=company_name)
    all_company_flights = fac_obj.get_my_flights()

    final_list = [(0, 'Choose which flight')]
    for i in all_company_flights:
        dal_obj1 = AirlineFacade(id=i.origin_country_id)
        origin = dal_obj1.get_country_by_id()
        dal_obj2 = AirlineFacade(id=i.destination_country_id)
        destination = dal_obj2.get_country_by_id()
        full_flight_details = f'{company_name}, From:{origin.name}, To:{destination.name}, Departure Date:{i.departure_time}, Landing Date:{i.landing_time}'
        final_list.append((i.id, full_flight_details ))

    form.flights_detailes.choices = final_list
    selected_flight_id = form.flights_detailes.data
    if form.validate_on_submit():
        return redirect(url_for('update_flight_fields',company_name=company_name,flight_id=selected_flight_id))
        
    return render_template("airline/choose_flight.html",
        airline_name = company_name,
        form=form,
        text="Update flight",
        title="Update flight",
        btn_action="Update flight",
        )
    

@login_required
@require_airline_role
def update_flight_fields(company_name,flight_id):
    form = update_flight_form() 
    fac_obj = AirlineFacade(id=flight_id)
    flight = fac_obj.get_flight_by_id()
    origin_country_id = flight.origin_country_id
    dal_obj = AirlineFacade(id=origin_country_id)
    origin_country = dal_obj.get_country_by_id()

    destination_country_id = flight.destination_country_id
    dal_obj = AirlineFacade(id=destination_country_id)
    destination_country = dal_obj.get_country_by_id()
    departure_time = flight.departure_time
    landing_time = flight.landing_time
    remaining_tickets = flight.remaining_tickets

    if form.destination_country_id.data == origin_country_id or form.origin_country_id.data == destination_country_id:
        flash('Origin and destination cannot be the same.', "danger")
    else: 
        if form.validate_on_submit():

            fac_obj = AirlineFacade(name=company_name)
            airline = fac_obj.get_airline_by_name()
            fac_obj = AirlineFacade(id=flight_id,airline_company_id=airline.id,\
                                    origin_country_id=form.origin_country_id.data,\
                                    destination_country_id=form.destination_country_id.data,\
                                    departure_time=form.departure_time.data,\
                                    landing_time=form.landing_time.data,\
                                    remaining_tickets=form.remaining_tickets.data)
            
            res = fac_obj.update_flight()
            if res:
                flash(f"Airline detailes updated", "success")
            else:
                flash("error occurred", "danger")
            return redirect(url_for('company_home',company_name=company_name))
    return render_template("airline/update_flight.html",
        origin_country=origin_country.name,
        destination_country = destination_country.name,
        departure_time = departure_time,
        landing_time=landing_time,
        remaining_tickets=remaining_tickets,
        airline_name = company_name,
        form=form,
        text="Update flight",
        title="Update flight",
        btn_action="Update flight",
        )
