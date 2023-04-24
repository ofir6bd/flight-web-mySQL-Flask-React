import sys
import os
 
# import a module in the parent
current = os.path.dirname(os.path.realpath(__file__))
# Getting the parent directory name
parent = os.path.dirname(current)
# adding the parent directory to the sys.path.
sys.path.append(parent)

from wtforms import StringField
from flask_wtf import FlaskForm
from wtforms.validators import Length, Regexp
from wtforms import ValidationError,SelectField
from models import *
from Facades.AnonymousFacade import AnonymousFacade
from wtforms.validators import DataRequired


def get_all_countries():
    final_list = [(0, 'Choose which Country')]
    fac_obj = AnonymousFacade()
    items = fac_obj.get_all_countries()
    for i in items:
        final_list.append((i.id, i.name))
    return final_list


def get_airline_user_list():
    final_list = [(0, 'Choose which user')]
    fac_obj = AnonymousFacade()
    users = fac_obj.get_all_users()
    for i in users:
        if i.user_role == 2:
            final_list.append((i.id, i.username))
    return final_list


def get_customer_user_list():
    final_list = [(0, 'Choose which user')]
    fac_obj = AnonymousFacade()
    users = fac_obj.get_all_users() 
    for i in users:
        if i.user_role == 3:
            final_list.append((i.id, i.username))
    return final_list


def get_admin_user_list():
    final_list = [(0, 'Choose which user')]
    fac_obj = AnonymousFacade()
    users = fac_obj.get_all_users()
    for i in users:
        if i.user_role == 1:
            final_list.append((i.id, i.username))
    return final_list


def get_all_airlines():
    final_list = [(0, 'Airline company')]
    fac_obj = AnonymousFacade()
    airlines = fac_obj.get_all_airlines() 
    for i in airlines:
        full_details = f'{i.name},{i.country_id}'
        final_list.append((i.id, full_details))
    return final_list


def get_all_customers():
    final_list = [(0, 'Customers')]
    fac_obj = AnonymousFacade()
    customers = fac_obj.get_all_customers() 
    for i in customers:
        full_details = f'{i.first_name},{i.last_name},{i.address},{i.phone_no}'
        final_list.append((i.id,full_details))
    return final_list


def get_all_admins():
    final_list = [(0, 'Administrators')]
    fac_obj = AnonymousFacade()
    admins = fac_obj.get_all_administrators() 
    for i in admins:
        full_details = f'{i.first_name},{i.last_name}'
        final_list.append((i.id, full_details))
    return final_list


class add_airline_form(FlaskForm):
    name = StringField('Name', validators=[DataRequired()])
    country = SelectField('Country', coerce=int, validators=[DataRequired()])
    user = SelectField('Users', coerce=int, validators=[DataRequired()])
    
    def __init__(self, *args, **kwargs):
        super(add_airline_form, self).__init__(*args, **kwargs)
        self.country.choices = get_all_countries()
        self.user.choices = get_airline_user_list()

    def validate_name(self, name):
        obj = AnonymousFacade(name=name.data)
        item = obj.get_airline_by_name()
        if item is not None:
            raise ValidationError('Please use a different name.')

class add_customer_form(FlaskForm):
    first_name = StringField(validators=[DataRequired(),Length(3, 20, message="Please provide a valid name"),
            Regexp(
                "^[A-Za-z][A-Za-z_.]*$",
                0,
                "first name must have only letters, " "dots or underscores",
            ),
        ])
    last_name = StringField(validators=[DataRequired(),Length(3, 20, message="Please provide a valid name"),
            Regexp(
                "^[A-Za-z][A-Za-z_.]*$",
                0,
                "last name must have only letters, " "dots or underscores",
            ),
        ])
    address = StringField(validators=[DataRequired(),Length(3, 20, message="Please provide a valid name"),
            Regexp(
                "^[A-Za-z][A-Za-z_.]*$",
                0,
                "address must have only letters, " "dots or underscores",
            ),
        ])
    phone_no = StringField(validators=[DataRequired(),Length(10, 10, message="Please provide a valid phone number"),
            Regexp(
                "^[0-9]{10}$",
                0,
                "phone no must have 10 digits only",
            ),
        ])
    credit_card_no = StringField(validators=[DataRequired(),Length(16,16, message="Please provide a valid phone number"),
            Regexp(
                "^[0-9]{16}$",
                0,
                "credit card no must have 16 digits only",
            ),
        ])
    user = SelectField('Users', coerce=int, validators=[DataRequired()])

    def __init__(self, *args, **kwargs):
        super(add_customer_form, self).__init__(*args, **kwargs)
        self.user.choices = get_customer_user_list()
        
    def validate_phone_no(self, phone_no):
        obj = AnonymousFacade(phone_no=phone_no.data)
        item = obj.get_customer_by_phone_no()
        if item is not None:
            raise ValidationError('Please use a different phone_no.')
        
    def validate_credit_card_no(self, credit_card_no):
        obj = AnonymousFacade(credit_card_no=credit_card_no.data)
        item = obj.get_customer_by_credit_card_no()
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
                