
import sys
import os
 
# import a module in the parent
current = os.path.dirname(os.path.realpath(__file__))
# Getting the parent directory name
parent = os.path.dirname(current)
# adding the parent directory to the sys.path.
sys.path.append(parent)
from DAL import *

class FacadeBase(object):

    def __init__(self, id=0, username="", password="", email="", role_name="",user_role="", first_name="", last_name="", adress="", phone_no="", credit_card_no=""):
        self.id = id
        self.username = username
        self.password = password
        self.email = email
        self.role_name = role_name
        self.user_role = user_role
        self.first_name =first_name
        self.last_name = last_name
        self.adress = adress
        self.phone_no = phone_no
        self.credit_card_no = credit_card_no

    def get_all_flights(self):
        dal_obj = DataLayer(id=self.id, table=Flights)      
        flights = dal_obj.get_all()
        return flights

    def get_flight_by_id(self):
        dal_obj = DataLayer(table=Flights,id=self.id)      
        flight = dal_obj.get_by_id()
        return flight

    def get_flights_by_parameters(self,origin_country_id,destination_country_id, date):
        pass

    def get_all_airlines(self):
        dal_obj = DataLayer(table=AirlineCompanies)      
        airline_company = dal_obj.get_all()
        return airline_company

    def get_airline_by_id(self):
        dal_obj = DataLayer(table=AirlineCompanies,id=self.id)      
        airline = dal_obj.get_by_id()
        return airline

    def get_airline_by_parameteres(self,origin_country_id,destination_country_id, date):
        pass

    def get_all_countries(self):
        dal_obj = DataLayer(table=Countries)      
        countries = dal_obj.get_all()
        return countries

    def get_country_by_id(self):
        dal_obj = DataLayer(table=Countries,id=self.id)      
        country = dal_obj.get_by_id()
        return country

    def create_new_user(self):
        user = Users(username=self.username,password=self.password,email=self.email,user_role=self.user_role)
        dal_obj = DataLayer()      
        res = dal_obj.insert_obj(user)
        return res



######################### testing functions
# with app.app_context():
#     # obj1 = FacadeBase(id=1) 
#     # ans = obj1.get_flight_by_id()
#     # ans = obj1.get_all_flights()
#     # ans = obj1.get_all_airlines()
#     # ans = obj1.get_airline_by_id()
#     # ans = obj1.get_all_countries()
#     # ans = obj1.get_country_by_id()
#     # obj2 = FacadeBase(username='Ofir',password='123456',email='q@q.com', user_role= 2 )
#     # obj2.create_new_user()
    
#     # print(ans)
#     print("Done")
