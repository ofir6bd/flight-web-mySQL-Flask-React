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
def add_flight():
    form = add_flight_form() 
    if form.validate_on_submit():
        fac_obj = AirlineFacade(id=form.user.data)
        user = fac_obj.get_user_by_id()
        fac_obj = AirlineFacade(first_name=form.first_name.data,\
                                      last_name=form.last_name.data,\
                                     address=form.address.data,\
                                      phone_no=form.phone_no.data,\
                                     credit_card_no=form.credit_card_no.data,user_id=user.id)
        res = fac_obj.add_customer()
        if res:
            flash(f"Flight added", "success")
        return redirect(url_for('index'))
    return render_template("customer/add_flight.html",
        form=form,
        text="Add flight",
        title="Add flight",
        btn_action="Add flight",
        )