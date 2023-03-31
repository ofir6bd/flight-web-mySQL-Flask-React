import sys
import os
 
# import a module in the parent
current = os.path.dirname(os.path.realpath(__file__))
# Getting the parent directory name
parent = os.path.dirname(current)
# adding the parent directory to the sys.path.
sys.path.append(parent)


from flight.secrets_keys import *
from flight.app import create_app

app = create_app()
app.secret_key = SECRET_KEY
app.config['TESTING'] = True
app.config['SQLALCHEMY_DATABASE_URI'] = f'mysql://root:{PASSWORD}@localhost/test_db'

import pytest

from flight.routes import * 

def test_home_route():
  res = app.test_client().get("/")
  print()

test_home_route()
# def test_assert():
#     assert True

# def test_home_page(client):
#   response = client.get('/')
#   assert response.status_code == 200

# @pytest.fixture
# def client():
#     client = app.test_client()
#     return client
