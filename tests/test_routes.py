import sys
import os
 
# import a module in the parent
current = os.path.dirname(os.path.realpath(__file__))
# Getting the parent directory name
parent = os.path.dirname(current)
# adding the parent directory to the sys.path.
sys.path.append(parent)

# from flask import Flask
# import os
# from models import UserRoles,Users,Administrators,Customers, Countries,AirlineCompanies,Flights,Tickets
from secrets_keys import *
from app import create_app
# import unittest

app = create_app()
app.secret_key = SECRET_KEY
app.config['TESTING'] = True
app.config['SQLALCHEMY_DATABASE_URI'] = f'mysql://root:{PASSWORD}@localhost/test_db'

import pytest
from flask import Flask
import json

# from routes import index

from routes import index 

def test_assert():
    assert True

def test_home_page(client):
  response = client.get('/')
  assert response.status_code == 200

@pytest.fixture
def client():
    client = app.test_client()
    return client

# if __name__ == "__main__":
#     client()
# def test_post_route__success():
#     app = Flask(__name__)
#     configure_routes(app)
#     client = app.test_client()
#     url = '/post/test'

#     mock_request_headers = {
#         'authorization-sha256': '123'
#     }

#     mock_request_data = {
#         'request_id': '123',
#         'payload': {
#             'py': 'pi',
#             'java': 'script'
#         }
#     }

#     response = client.post(url, data=json.dumps(mock_request_data), headers=mock_request_headers)
#     assert response.status_code == 200


# def test_post_route__failure__unauthorized():
#     app = Flask(__name__)
#     configure_routes(app)
#     client = app.test_client()
#     url = '/post/test'

#     mock_request_headers = {}

#     mock_request_data = {
#         'request_id': '123',
#         'payload': {
#             'py': 'pi',
#             'java': 'script'
#         }
#     }

#     response = client.post(url, data=json.dumps(mock_request_data), headers=mock_request_headers)
#     assert response.status_code == 401


# def test_post_route__failure__bad_request():
#     app = Flask(__name__)
#     configure_routes(app)
#     client = app.test_client()
#     url = '/post/test'

#     mock_request_headers = {
#         'authorization-sha256': '123'
#     }

#     mock_request_data = {}

#     response = client.post(url, data=json.dumps(mock_request_data), headers=mock_request_headers)
#     assert response.status_code == 400