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
from Forms_templates.admin_forms import add_airline_form,add_customer_form,add_admin_form
from models import UserRoles,Users,Administrators,Customers, Countries,AirlineCompanies,Flights,Tickets
from app import db
from Facades.AdministratorFacade import AdministratorFacade

@login_required
@require_admin_role
def add_airline():
    form = add_airline_form() 
    if form.validate_on_submit():
        fac_obj = AdministratorFacade(id=form.country.data)
        country = fac_obj.get_country_by_id()
        fac_obj = AdministratorFacade(id=form.user.data)
        user = fac_obj.get_user_by_id()
        fac_obj = AdministratorFacade(name=form.name.data, country_id=country.id,user_id=user.id)
        res = fac_obj.add_airline()
        if res:
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
        fac_obj = AdministratorFacade(id=form.user.data)
        user = fac_obj.get_user_by_id()
        fac_obj = AdministratorFacade(first_name=form.first_name.data,\
                                      last_name=form.last_name.data,\
                                         address=form.address.data,\
                                             phone_no=form.phone_no.data,\
                                                 credit_card_no=form.credit_card_no.data,user_id=user.id)
        res = fac_obj.add_customer()
        if res:
            flash(f"Customer added", "success")
        return redirect(url_for('index'))
    return render_template("admin/add_customer.html",
        form=form,
        text="Add customer",
        title="Add customer",
        btn_action="Add customer",
        )

@login_required
@require_admin_role
def add_admin():
    form = add_admin_form() 
    if form.validate_on_submit():
        fac_obj = AdministratorFacade(id=form.user.data)
        user = fac_obj.get_user_by_id()
        fac_obj = AdministratorFacade(first_name=form.first_name.data,\
                                      last_name=form.last_name.data,\
                                       user_id=user.id)
        res = fac_obj.add_administrator()
        if res:
            flash(f"Admin added", "success")
        return redirect(url_for('index'))
    return render_template("admin/add_admin.html",
        form=form,
        text="Add admin",
        title="Add admin",
        btn_action="Add admin",
        )