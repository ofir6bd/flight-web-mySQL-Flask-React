
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
from Facades.CustomerFacade import CustomerFacade

# class add_ticket_form(FlaskForm):
#     flight_id    

class update_customer_form(FlaskForm):
    first_name = StringField(validators=[Length(3, 20, message="Please provide a valid name"),
            Regexp(
                "^[A-Za-z][A-Za-z_.]*$",
                0,
                "first name must have only letters, " "dots or underscores",
            ),
        ])
    last_name = StringField(validators=[Length(3, 20, message="Please provide a valid name"),
            Regexp(
                "^[A-Za-z][A-Za-z_.]*$",
                0,
                "last name must have only letters, " "dots or underscores",
            ),
        ])
    address = StringField(validators=[Length(3, 20, message="Please provide a valid name"),
            Regexp(
                "^[A-Za-z][A-Za-z_.]*$",
                0,
                "address must have only letters, " "dots or underscores",
            ),
        ])
    phone_no = StringField(validators=[Length(10,10, message="Please provide a valid phone number"),
            Regexp(
                "^[0-9]{10}$",
                0,
                "phone no must have 10 digits only",
            ),
        ])
    credit_card_no = StringField(validators=[Length(16,16, message="Please provide a valid phone number"),
            Regexp(
                "^[0-9]{16}$",
                0,
                "credit card no must have 16 digits only",
            ),
        ])


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
   
    

    # email = StringField(validators=[InputRequired(), Email(), Length(1, 64)])
    # password = PasswordField(validators=[InputRequired(), Length(8, 72)])
    # cpassword = PasswordField(
    #     validators=[
    #         InputRequired(),
    #         Length(8, 72),
    #         EqualTo("password", message="Passwords must match !"),
    #     ]
    # )

    # def validate_email(self, email):
    #     fac_obj = AnonymousFacade(email=email.data)
    #     if fac_obj.get_user_by_email():
    #         raise ValidationError("Email already registered!")

    # def validate_username(self, username):
    #     fac_obj = AnonymousFacade(username=username.data)
    #     if fac_obj.get_user_by_username():
    #         raise ValidationError("Username already taken!")
        

class remove_ticket_form(FlaskForm):
    tickets_detailes = SelectField(validators=[DataRequired()], coerce=int)
