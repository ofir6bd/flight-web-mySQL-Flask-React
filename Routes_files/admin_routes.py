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
from per_req_Wrappers import require_admin_role
from Forms_templates.admin_forms import add_airline_form,add_customer_form
from models import UserRoles,Users,Administrators,Customers, Countries,AirlineCompanies,Flights,Tickets
from app import db
from Facades.AdministratorFacade import AdministratorFacade

@login_required
@require_admin_role
def add_airline():
    form = add_airline_form() 
    if form.validate_on_submit():
        country = Countries.query.get(form.country.data)
        user = Users.query.get(form.user.data)
        fac_obj = AdministratorFacade(name=form.name.data, country_id=country.id,user_id=user.id)
        res = fac_obj.add_airline()
        if res:
        # airline_company = AirlineCompanies(name=form.name.data, country_id=country.id,user_id=user.id)
        # db.session.add(airline_company)
        # db.session.commit()
            flash(f"Airline company added", "success")
        return redirect(url_for('index'))
    return render_template("admin/add_airline.html",
        form=form,
        text="Add airline",
        title="Add airline",
        btn_action="Add airline",
        )

@login_required
@require_admin_role
def add_customer():
    form = add_customer_form() 
    if form.validate_on_submit():
        country = Countries.query.get(form.country.data)
        user = Users.query.get(form.user.data)
        airline_company = AirlineCompanies(name=form.name.data, country_id=country.id,user_id=user.id)
        print('here')
        db.session.add(airline_company)
        db.session.commit()
        return redirect(url_for('index'))
    return render_template("admin/add_customer.html",
        form=form,
        text="Add customer",
        title="Add customer",
        btn_action="Add customer",
        )