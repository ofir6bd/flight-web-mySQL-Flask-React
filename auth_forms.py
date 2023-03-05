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

class login_form(FlaskForm):
    email = StringField(validators=[InputRequired(), Email(), Length(1, 64)])
    password = PasswordField(validators=[InputRequired(), Length(min=8, max=72)])
    # Placeholder labels to enable form rendering
    username = StringField(
        validators=[Optional()]
    )

def get_user_role_list():
    final_list = []
    final_list.append((0, 'User role'))
    fac_obj = AnonymousFacade()
    items = fac_obj.get_all_user_roles()
    for i in items:
        if i.role_name != "Anonymous":
            final_list.append((i.id, i.role_name))
    return final_list

class register_form(FlaskForm):
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

    role = SelectField('UserRoles', coerce=int, validators=[DataRequired()])

    def __init__(self, *args, **kwargs):
        super(register_form, self).__init__(*args, **kwargs)
        self.role.choices =  get_user_role_list()

    def validate_email(self, email):
        fac_obj = AnonymousFacade(email=email.data)
        if fac_obj.get_user_by_email():
            raise ValidationError("Email already registered!")

    def validate_username(self, username):
        fac_obj = AnonymousFacade(username=username.data)
        if fac_obj.get_user_by_username():
            raise ValidationError("Username already taken!")

    # def validate_email(self, email):
    #     if Users.query.filter_by(email=email.data).first():
    #         raise ValidationError("Email already registered!")

    # def validate_username(self, username):
    #     if Users.query.filter_by(username=username.data).first():
    #         raise ValidationError("Username already taken!")