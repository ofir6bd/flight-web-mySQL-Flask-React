
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
from wtforms import ValidationError,validators
from models import *
from Facades.AnonymousFacade import AnonymousFacade
from DAL import DataLayer

class search_flights_form(FlaskForm):
    origin_country = StringField(validators=[
            InputRequired(),
            Length(3, 20, message="Please provide a valid name"),
            Regexp(
                "^[A-Za-z][A-Za-z0-9_.]*$",
                0,
                "Usernames must have only letters, " "numbers, dots or underscores",
            ),
        ]
    )
    destination_country = StringField(validators=[
            InputRequired(),
            Length(3, 20, message="Please provide a valid name"),
            Regexp(
                "^[A-Za-z][A-Za-z0-9_.]*$",
                0,
                "Usernames must have only letters, " "numbers, dots or underscores",
            ),
        ]
    )
    
    departure_time = DateTimeLocalField('Which date is your favorite?', format='%m/%d/%y')
    landing_time = DateTimeLocalField('Which date is your favorite?', format='%m/%d/%y')
    

    # def validate_email(self, email):
    #     fac_obj = AnonymousFacade(email=email.data)
    #     if fac_obj.get_user_by_email():
    #         raise ValidationError("Email already registered!")

    # def validate_username(self, username):
    #     fac_obj = AnonymousFacade(username=username.data)
    #     if fac_obj.get_user_by_username():
    #         raise ValidationError("Username already taken!")