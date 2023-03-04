# Register route
import sys
import os
 
# import a module in the parent
current = os.path.dirname(os.path.realpath(__file__))
# Getting the parent directory name
parent = os.path.dirname(current)
# adding the parent directory to the sys.path.
sys.path.append(parent)
from Forms_templates.customer_form import update_customer_form
# from Facades.AnonymousFacade import AnonymousFacade
# from Facades.CustomerFacade import CustomerFacade
from flask import Flask, redirect, url_for,request, render_template, session, flash
from flask_login import UserMixin, login_user, LoginManager,login_required, logout_user,current_user
from per_req_Wrappers import require_admin_role
from Forms_templates.admin_forms import add_airline_form

@login_required
@require_admin_role
def add_airline():
    form = add_airline_form() 
    
    return render_template("admin/airline.html",
        form=form,
        text="add airline",
        title="add airline",
        btn_action="add airline",
        )
