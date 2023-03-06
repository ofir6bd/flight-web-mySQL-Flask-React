
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
    DateTimeLocalField,
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

class add_airline_form(FlaskForm):
    username = StringField(
        validators=[
            InputRequired(),
            Length(3, 20, message="Please provide a valid name"),
            Regexp(
                "^[A-Za-z][A-Za-z0-9_.]*$",
                0,
                "Usernames must have only letters, " "numbers, dots or underscores",
            ),
        ]
    )
    email = StringField(validators=[InputRequired(), Email(), Length(1, 64)])
    password = PasswordField(validators=[InputRequired(), Length(8, 72)])
    cpassword = PasswordField(
        validators=[
            InputRequired(),
            Length(8, 72),
            EqualTo("password", message="Passwords must match !"),
        ]
    )

    def validate_email(self, email):
        fac_obj = AnonymousFacade(email=email.data)
        if fac_obj.get_user_by_email():
            raise ValidationError("Email already registered!")

    def validate_username(self, username):
        fac_obj = AnonymousFacade(username=username.data)
        if fac_obj.get_user_by_username():
            raise ValidationError("Username already taken!")
        
def get_all_airlines():
    final_list = []
    final_list.append((0, 'Airline company'))
    fac_obj = AnonymousFacade()
    airlines = fac_obj.get_all_airlines() 
    for i in airlines:
        final_list.append((i.id, i.name))
    return final_list

def get_all_countries():
    final_list = []
    final_list.append((0, 'Choose which Country'))
    fac_obj = AnonymousFacade()
    items = fac_obj.get_all_countries()
    for i in items:
        final_list.append((i.id, i.name))
    return final_list

class add_flight_form(FlaskForm):
    airline_company_id = SelectField('Country', coerce=int, validators=[DataRequired()])
    origin_country_id = SelectField('Country', coerce=int, validators=[DataRequired()])
    destination_country_id = SelectField('Country', coerce=int, validators=[DataRequired()])
    departure_time = DateTimeLocalField('Which date is your favorite?', format='%m/%d/%y')
    landing_time = DateTimeLocalField('Which date is your favorite?', format='%m/%d/%y')
    
    def __init__(self, *args, **kwargs):
        super(add_flight_form, self).__init__(*args, **kwargs)
        self.airline_company_id.choices = get_all_airlines()
        self.origin_country_id.choices = get_all_countries()
        self.destination_country_id.choices = get_all_countries()

    def validate_email(self, email):
        fac_obj = AnonymousFacade(email=email.data)
        if fac_obj.get_user_by_email():
            raise ValidationError("Email already registered!")

    def validate_username(self, username):
        fac_obj = AnonymousFacade(username=username.data)
        if fac_obj.get_user_by_username():
            raise ValidationError("Username already taken!")