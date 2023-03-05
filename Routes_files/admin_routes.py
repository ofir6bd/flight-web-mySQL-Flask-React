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
from Forms_templates.admin_forms import add_airline_form
from models import UserRoles,Users,Administrators,Customers, Countries,AirlineCompanies,Flights,Tickets
from app import db

@login_required
@require_admin_role
def add_airline():
    form = add_airline_form() 
    if form.validate_on_submit():
        country = Countries.query.get(form.country.data)

        airline_company = AirlineCompanies(name=form.name.data, country_id=country.id,user_id=1)
        print('here')
        db.session.add(airline_company)
        db.session.commit()
        return redirect(url_for('index'))
    return render_template("admin/airline.html",
        form=form,
        text="add airline",
        title="add airline",
        btn_action="add airline",
        )
