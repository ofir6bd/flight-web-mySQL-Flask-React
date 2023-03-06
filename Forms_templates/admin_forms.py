
import sys
import os
 
# import a module in the parent
current = os.path.dirname(os.path.realpath(__file__))
# Getting the parent directory name
parent = os.path.dirname(current)
# adding the parent directory to the sys.path.
sys.path.append(parent)

from wtforms import (
    StringField,
    PasswordField,
    BooleanField,
    IntegerField,
    DateField,
    TextAreaField,
)


from flask_wtf import FlaskForm
from wtforms.validators import InputRequired, Length, EqualTo, Email, Regexp ,Optional
import email_validator
from flask_login import current_user
from wtforms import ValidationError,validators,SelectField
from models import *
from Facades.AnonymousFacade import AnonymousFacade
from DAL import DataLayer
from wtforms.validators import DataRequired

def get_countries_list():
    final_list = []
    final_list.append((0, 'Choose which Country'))
    fac_obj = AnonymousFacade()
    items = fac_obj.get_all_countries()
    for i in items:
        final_list.append((i.id, i.name))
    return final_list

def get_airline_user_list():
    final_list = []
    final_list.append((0, 'Choose which user'))
    fac_obj = AnonymousFacade()
    users = fac_obj.get_all_users()
    #TODO create join table and not use 2 as filter to if 
    for i in users:
        if i.user_role == 2:
            final_list.append((i.id, i.username))
    return final_list

def get_customer_user_list():
    final_list = []
    final_list.append((0, 'Choose which user'))
    fac_obj = AnonymousFacade()
    users = fac_obj.get_all_users()
    #TODO create join table and not use 2 as filter to if 
    for i in users:
        if i.user_role == 3:
            final_list.append((i.id, i.username))
    return final_list

def get_admin_user_list():
    final_list = []
    final_list.append((0, 'Choose which user'))
    fac_obj = AnonymousFacade()
    users = fac_obj.get_all_users()
    #TODO create join table and not use 2 as filter to if 
    for i in users:
        if i.user_role == 1:
            final_list.append((i.id, i.username))
    return final_list

def get_all_airlines():
    final_list = []
    final_list.append((0, 'Airline company'))
    fac_obj = AnonymousFacade()
    airlines = fac_obj.get_all_airlines() 
    for i in airlines:
        full_details = f'{i.name},{i.country_id}'
        final_list.append((i.id, full_details))
    return final_list

def get_all_customers():
    final_list = []
    final_list.append((0, 'Customers'))
    fac_obj = AnonymousFacade()
    customers = fac_obj.get_all_customers() 
        # TODO add filter to show only if not FK to other table
    for i in customers:
        full_details = f'{i.first_name},{i.last_name},{i.address},{i.phone_no}'
        final_list.append((i.id,full_details))
    return final_list

def get_all_admins():
    final_list = []
    final_list.append((0, 'Administrators'))
    fac_obj = AnonymousFacade()
    admins = fac_obj.get_all_administrators() 
        # TODO add filter to show only if not FK to other table
    for i in admins:
        full_details = f'{i.first_name},{i.last_name}'
        final_list.append((i.id, full_details))
    return final_list

class add_airline_form(FlaskForm):
    name = StringField('Name', validators=[DataRequired()])
    country = SelectField('Country', coerce=int, validators=[DataRequired()])
    user = SelectField('Users', coerce=int, validators=[DataRequired()])
    # submit = SubmitField('Add')

    def __init__(self, *args, **kwargs):
        super(add_airline_form, self).__init__(*args, **kwargs)
        self.country.choices = get_countries_list()
        self.user.choices = get_airline_user_list()

    def validate_name(self, name):
        airline_company = AirlineCompanies.query.filter_by(name=name.data).first()
        if airline_company is not None:
            raise ValidationError('Please use a different name.')

class add_customer_form(FlaskForm):
    first_name = StringField(validators=[DataRequired()])
    last_name = StringField(validators=[DataRequired()])
    address = StringField(validators=[DataRequired()])
    phone_no = StringField(validators=[DataRequired()])
    credit_card_no = StringField(validators=[DataRequired()])
    user = SelectField('Users', coerce=int, validators=[DataRequired()])

    # submit = SubmitField('Add')

    def __init__(self, *args, **kwargs):
        super(add_customer_form, self).__init__(*args, **kwargs)
        self.user.choices = get_customer_user_list()
        
    def validate_phone_no(self, phone_no):
        item = Customers.query.filter_by(phone_no=phone_no.data).first()
        if item is not None:
            raise ValidationError('Please use a different phone_no.')
        
    def validate_credit_card_no(self, credit_card_no):
        item = Customers.query.filter_by(credit_card_no=credit_card_no.data).first()
        if item is not None:
            raise ValidationError('Please use a different credit_card_no.')

class add_admin_form(FlaskForm):
    first_name = StringField(validators=[DataRequired()])
    last_name = StringField(validators=[DataRequired()])
    user = SelectField('Users', coerce=int, validators=[DataRequired()])

    def __init__(self, *args, **kwargs):
        super(add_admin_form, self).__init__(*args, **kwargs)
        self.user.choices = get_admin_user_list()


class remove_airline_form(FlaskForm):
    airline_company_id = SelectField('Airline Company', validators=[DataRequired()], coerce=int)
    def __init__(self, *args, **kwargs):
        super(remove_airline_form, self).__init__(*args, **kwargs)
        self.airline_company_id.choices = get_all_airlines()
    
    def validate_airline_company_id(self, airline_company_id):
        obj = AnonymousFacade(id=airline_company_id.data)
        item = obj.get_flight_by_id()
        if item is not None:
            raise ValidationError('Tickets exists for this airline, cannot be deleted.')

class remove_customer_form(FlaskForm):
    customer_id = SelectField('Customers', validators=[DataRequired()], coerce=int)
    def __init__(self, *args, **kwargs):
        super(remove_customer_form, self).__init__(*args, **kwargs)
        self.customer_id.choices = get_all_customers()
    
    def validate_customer_id(self, customer_id):
        obj = AnonymousFacade(id=customer_id.data)
        item = obj.get_ticket_by_id()
        if item is not None:
            raise ValidationError('This customer have ticket, cannot be deleted.')


class remove_admin_form(FlaskForm):
    admin_id = SelectField('Administrators', validators=[DataRequired()], coerce=int)
    def __init__(self, *args, **kwargs):
        super(remove_admin_form, self).__init__(*args, **kwargs)
        self.admin_id.choices = get_all_admins()
                