# import sys
# import os
 
# # import a module in the parent
# current = os.path.dirname(os.path.realpath(__file__))
# # Getting the parent directory name
# parent = os.path.dirname(current)
# # adding the parent directory to the sys.path.
# sys.path.append(parent)

# from flask import Flask
# import os
# import tempfile
# import pytest
# from flask_sqlalchemy import SQLAlchemy
# from models import UserRoles,Users,Administrators,Customers, Countries,AirlineCompanies,Flights,Tickets
# from secrets_keys import *
# from app import create_app

# app = create_app()
# app.secret_key = SECRET_KEY
# app.config['SQLALCHEMY_DATABASE_URI'] = f'mysql://root:{PASSWORD}@localhost/test_db'

# db = SQLAlchemy()

# @pytest.fixture()
# def client():
#     app = Flask(__name__, static_folder='static')

#     app.config["TESTING"] = True
#     client = app.test_client()
#     yield client