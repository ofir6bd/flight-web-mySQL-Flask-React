import sys
import os
 
# import a module in the parent
current = os.path.dirname(os.path.realpath(__file__))
# Getting the parent directory name
parent = os.path.dirname(current)
# adding the parent directory to the sys.path.
sys.path.append(parent)

from flask import Flask, redirect, url_for, render_template,  flash
from flask_login import login_required
from per_req_Wrappers import require_admin_role
from Forms_templates.admin_forms import add_airline_form,add_customer_form,add_admin_form,remove_airline_form,remove_customer_form,remove_admin_form
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


@login_required
@require_admin_role
def remove_airline():
    form = remove_airline_form() 
    if form.validate_on_submit():
        fac_obj = AdministratorFacade(id=form.airline_company_id.data)
        res = fac_obj.remove_airline()
        if res:
            flash(f"Airline company removed", "success")
        return redirect(url_for('index'))
    return render_template("admin/Remove_airline.html",
        form=form,
        text="Remove airline",
        title="Remove airline",
        btn_action="Remove airline",
        )


@login_required
@require_admin_role
def remove_customer():
    form = remove_customer_form() 
    if form.validate_on_submit():
        fac_obj = AdministratorFacade(id=form.customer_id.data)
        res = fac_obj.remove_customer()
        if res:
            flash(f"Customer removed", "success")
        return redirect(url_for('index'))
    return render_template("admin/remove_customer.html",
        form=form,
        text="Remove customer",
        title="Remove customer",
        btn_action="Remove customer",
        )


@login_required
@require_admin_role
def remove_admin():
    form = remove_admin_form() 
    if form.validate_on_submit():
        fac_obj = AdministratorFacade(id=form.admin_id.data)
        res = fac_obj.remove_administrator()
        if res:
            flash(f"Administrator removed", "success")
        return redirect(url_for('index'))
    return render_template("admin/remove_admin.html",
        form=form,
        text="Remove admin",
        title="Remove admin",
        btn_action="Remove admin",
        )