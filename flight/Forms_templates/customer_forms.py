import sys
import os
import re
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


class update_customer_form(FlaskForm):
    first_name = StringField()
    last_name = StringField()
    address = StringField()
    phone_no = StringField()
    credit_card_no = StringField()


    def validate_first_name(self, first_name):
        first_name_regex_pattern = re.compile(r"^[a-zA-Z\s]{2,50}$")
        first_name = first_name.data
        if not first_name_regex_pattern.search(first_name) and first_name:
            raise ValidationError('first name must contain characteres only 2 to 50') 
    
    
    def validate_last_name(self, last_name):
        last_name_regex_pattern = re.compile(r"^[a-zA-Z\s]{2,50}$")
        last_name = last_name.data
        if not last_name_regex_pattern.search(last_name) and last_name:
            raise ValidationError('last name must contain characteres only 2 to 50')    
    
    
    def validate_address(self, address):
        address_regex_pattern = re.compile(r"^[a-zA-Z0-9\s]{2,50}$")
        address = address.data
        if not address_regex_pattern.search(address) and address:
            raise ValidationError('address must contain characteres and digits only 2 to 50') 
        
        
    def validate_phone_no(self, phone_no):
        phone_no_regex_pattern = re.compile(r"^[0-9]{10}$")
        phone_no = phone_no.data
        if phone_no:
            if not phone_no_regex_pattern.search(phone_no):
                raise ValidationError('phone no must contain 10 digits only') 
            obj = AnonymousFacade(phone_no=phone_no)
            item = obj.get_customer_by_phone_no()
            if item is not None:
                raise ValidationError('Please use a different phone_no.')


    def validate_credit_card_no(self, credit_card_no):
        credit_card_no_regex_pattern = re.compile(r"^[0-9]{16}$")
        credit_card_no = credit_card_no.data
        if credit_card_no:
            if not credit_card_no_regex_pattern.search(credit_card_no):
                raise ValidationError('credit_card_no must contain 16 digits only') 
            obj = AnonymousFacade(credit_card_no=credit_card_no)
            item = obj.get_customer_by_credit_card_no()
            if item is not None:
                raise ValidationError('Please use a different credit_card_no.')


class remove_ticket_form(FlaskForm):
    tickets_detailes = SelectField(validators=[DataRequired()], coerce=int)
