
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
    countries_list = []
    fac_obj = AnonymousFacade()
    countries = fac_obj.get_all_countries()
    for c in countries:
        countries_list.append((c.id, c.name))
    return countries_list

def get_airline_user_list():
    final_list = []
    fac_obj = AnonymousFacade()
    users = fac_obj.get_all_users()
    #TODO create join table and not use 2 as filter to if 
    for i in users:
        if i.user_role == 2:
            final_list.append((i.id, i.username))
    return final_list

def get_customer_user_list():
    final_list = []
    fac_obj = AnonymousFacade()
    users = fac_obj.get_all_users()
    #TODO create join table and not use 2 as filter to if 
    for i in users:
        if i.user_role == 3:
            final_list.append((i.id, i.username))
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
      