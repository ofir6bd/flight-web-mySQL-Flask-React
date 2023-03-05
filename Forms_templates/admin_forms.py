
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

class add_airline_form(FlaskForm):
    name = StringField('Name', validators=[DataRequired()])
    country = SelectField('Country', coerce=int, validators=[DataRequired()])
    user = SelectField('Users', coerce=int, validators=[DataRequired()])
    # submit = SubmitField('Add')

    def __init__(self, *args, **kwargs):
        super(add_airline_form, self).__init__(*args, **kwargs)
        self.country.choices = [(c.id, c.name) for c in Countries.query.all()]
        self.user.choices = [(u.id, u.username) for u in Users.query.all()]

    def validate_name(self, name):
        airline_company = AirlineCompanies.query.filter_by(name=name.data).first()
        if airline_company is not None:
            raise ValidationError('Please use a different name.')
      