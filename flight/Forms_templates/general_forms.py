
import sys
import os
 
# import a module in the parent
current = os.path.dirname(os.path.realpath(__file__))
# Getting the parent directory name
parent = os.path.dirname(current)
# adding the parent directory to the sys.path.
sys.path.append(parent)

from wtforms import ValidationError,validators,SelectField
from wtforms.validators import DataRequired
from wtforms import StringField, DateTimeLocalField
from flask_wtf import FlaskForm
from wtforms import ValidationError
from models import *
from Facades.AnonymousFacade import AnonymousFacade


def get_all_countries():
    final_list = [(0, 'Choose which Country')]
    fac_obj = AnonymousFacade()
    items = fac_obj.get_all_countries()
    for i in items:
        final_list.append((i.id, i.name))
    return final_list


class search_flights_form(FlaskForm):
    origin_country = SelectField(validators=[DataRequired()])
    destination_country =SelectField(validators=[DataRequired()])
    departure_time = DateTimeLocalField('Which date is your favorite?',format='%Y-%m-%dT%H:%M')
    landing_time = DateTimeLocalField('Which date is your favorite?',format='%Y-%m-%dT%H:%M') 
    
    def __init__(self, *args, **kwargs):
        super(search_flights_form, self).__init__(*args, **kwargs)
        self.origin_country.choices = get_all_countries()
        self.destination_country.choices = get_all_countries()


def get_customer_user_list():
    final_list = [(0, 'Choose which user')]
    fac_obj = AnonymousFacade()
    users = fac_obj.get_all_users()
    #TODO create join table and not use 2 as filter to if 
    for i in users:
        if i.user_role == 3:
            final_list.append((i.id, i.username))
    return final_list

class register_customer_form(FlaskForm):
    first_name = StringField(validators=[DataRequired()])
    last_name = StringField(validators=[DataRequired()])
    address = StringField(validators=[DataRequired()])
    phone_no = StringField(validators=[DataRequired()])
    credit_card_no = StringField(validators=[DataRequired()])
        
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