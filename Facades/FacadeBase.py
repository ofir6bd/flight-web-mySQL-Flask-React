
import sys
import os
 
# import a module in the parent
current = os.path.dirname(os.path.realpath(__file__))
# Getting the parent directory name
parent = os.path.dirname(current)
# adding the parent directory to the sys.path.
sys.path.append(parent)
from DAL import DataLayer
from models import UserRoles,Users,Administrators,Customers, Countries,AirlineCompanies,Flights,Tickets

class FacadeBase(object):

    def __init__(self, id=0, username="", password="", email="", role_name="",\
                 user_id="",user_role="", first_name="", last_name="", address="", phone_no="",\
                      credit_card_no="",origin_country="",origin_country_id="",\
                        destination_country="", destination_country_id="",\
                      departure_time="",landing_time="",travelers=""):
        self.id = id
        self.username = username
        self.password = password
        self.email = email
        self.role_name = role_name
        self.user_id = user_id
        self.user_role = user_role
        self.first_name =first_name
        self.last_name = last_name
        self.address = address
        self.phone_no = phone_no
        self.credit_card_no = credit_card_no
        self.origin_country = origin_country
        self.origin_country_id = origin_country_id
        self.destination_country = destination_country
        self.destination_country_id = destination_country_id
        self.departure_time = departure_time
        self.landing_time = landing_time
        self.travelers = travelers


    def get_all_flights(self):
        dal_obj = DataLayer(table1=Flights)      
        flights = dal_obj.get_all()
        return flights
    
    def get_all_user_roles(self):
        dal_obj = DataLayer(table1=UserRoles)      
        user_roles = dal_obj.get_all()
        return user_roles
    
    def get_all_users(self):
        dal_obj = DataLayer(table1=Users)      
        user_roles = dal_obj.get_all()
        return user_roles
    
    def get_all_countries(self):
        dal_obj = DataLayer(table1=Countries)      
        countries = dal_obj.get_all()
        return countries
    
    def get_all_customers(self):
        dal_obj = DataLayer(table1=Customers)      
        customers = dal_obj.get_all()
        return customers

    def get_all_administrators(self):
        dal_obj = DataLayer(table1=Administrators)      
        admins = dal_obj.get_all()
        return admins

    def get_flight_by_id(self):
        dal_obj = DataLayer(table1=Flights,id=self.id)      
        flight = dal_obj.get_by_id()
        return flight

    def get_flights_by_parameters(self):
        dal_obj = DataLayer() 
        all_flight_and_countries = dal_obj.join_flights_countries()

        for i in reversed(range(len(all_flight_and_countries))):
            if self.origin_country != all_flight_and_countries[i][1].name:
                all_flight_and_countries.pop(i)

        for i in reversed(range(len(all_flight_and_countries))):
            if self.destination_country != all_flight_and_countries[i][2].name:
                all_flight_and_countries.pop(i)
        return all_flight_and_countries


    def get_all_airlines(self):
        dal_obj = DataLayer(table1=AirlineCompanies)      
        airline_company = dal_obj.get_all()
        return airline_company

    def get_airline_by_id(self):
        dal_obj = DataLayer(table1=AirlineCompanies,id=self.id)      
        airline = dal_obj.get_by_id()
        return airline

    def get_airline_by_parameteres(self,origin_country_id,destination_country_id, date):
        pass

    def get_all_countries(self):
        dal_obj = DataLayer(table1=Countries)      
        countries = dal_obj.get_all()
        return countries

    def get_country_by_id(self):
        dal_obj = DataLayer(table1=Countries,id=self.id)      
        country = dal_obj.get_by_id()
        return country

    def create_new_user(self):
        user = Users(username=self.username,password=self.password,email=self.email,user_role=int(self.user_role))
        dal_obj = DataLayer()      
        res = dal_obj.insert_obj(user)
        return res
    
    def get_user_by_email(self):
        dal_obj = DataLayer(table1=Users,input_attribute='email', input_value=self.email)
        return dal_obj.get_one_by_param()
    
    def get_user_by_username(self):
        dal_obj = DataLayer(table1=Users,input_attribute='username', input_value=self.username)
        return dal_obj.get_one_by_param()
    
    def get_user_by_id(self):
        dal_obj = DataLayer(table1=Users,input_attribute='id', input_value=self.id)
        return dal_obj.get_one_by_param()
    
    def get_admin_by_user_id(self):
        dal_obj = DataLayer(table1=Administrators,input_attribute='user_id', input_value=self.user_id)
        return dal_obj.get_one_by_param()
    
    def get_airline_by_user_id(self):
        dal_obj = DataLayer(table1=AirlineCompanies,input_attribute='user_id', input_value=self.user_id)
        return dal_obj.get_one_by_param()
    
    def get_customer_by_user_id(self):
        dal_obj = DataLayer(table1=Customers,input_attribute='user_id', input_value=self.user_id)
        return dal_obj.get_one_by_param()
    
        




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
