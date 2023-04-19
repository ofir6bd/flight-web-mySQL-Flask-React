
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
from flask import jsonify

class FacadeBase(object):

    def __init__(self,api=False, id=0,name="", username="", password="", email="", role_name="",\
                 user_id="",user_role="", first_name="", last_name="", address="", phone_no="",\
                      credit_card_no="",origin_country="",origin_country_id="",\
                        destination_country="", destination_country_id="",\
                      departure_time=None,flight_id="",landing_time="",travelers="",remaining_tickets="",airline_company_id="",customer_id=""):
        self.api = api
        self.id = id
        self.name = name
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
        self.flight_id = flight_id
        self.landing_time = landing_time
        self.travelers = travelers
        self.remaining_tickets = remaining_tickets
        self.airline_company_id = airline_company_id
        self.customer_id = customer_id

    def get_all_flights(self):
        dal_obj = DataLayer(table1=Flights, api=self.api)      
        return dal_obj.get_all()
    
    def get_all_user_roles(self):
        dal_obj = DataLayer(table1=UserRoles, api=self.api)      
        return dal_obj.get_all()
    
    def get_all_users(self):
        dal_obj = DataLayer(table1=Users)      
        return dal_obj.get_all()
    
    def get_all_countries(self):
        dal_obj = DataLayer(table1=Countries, api=self.api)  
        return dal_obj.get_all()   
    
    def get_all_customers(self):
        dal_obj = DataLayer(table1=Customers, api=self.api)      
        return dal_obj.get_all()

    def get_all_administrators(self):
        dal_obj = DataLayer(table1=Administrators, api=self.api)     
        return dal_obj.get_all()

    def get_flight_by_id(self):
        dal_obj = DataLayer(api=self.api,table1=Flights,id=self.id)      
        return dal_obj.get_by_id()
    
    def get_customer_by_id(self):
        dal_obj = DataLayer(table1=Customers,id=self.id)      
        return dal_obj.get_by_id()
    
    def get_ticket_by_id(self):
        dal_obj = DataLayer(table1=Tickets,id=self.id)      
        return dal_obj.get_by_id()
    
    def get_customer_by_phone_no(self):
        dal_obj = DataLayer(table1=Customers,input_attribute='phone_no', input_value=self.phone_no)  
        return dal_obj.get_one_by_param()

    def get_customer_by_credit_card_no(self):
        dal_obj = DataLayer(table1=Customers,input_attribute='credit_card_no', input_value=self.credit_card_no)  
        return dal_obj.get_one_by_param()
    
    def get_flights_by_parameters(self):
        dal_obj = DataLayer() 
        all_flight_and_countries = dal_obj.join_flights_countries()

        # drop flights that not match to the origin country
        for i in reversed(range(len(all_flight_and_countries))):
            if self.origin_country != "0":
                if int(self.origin_country) != int(all_flight_and_countries[i][1].id):
                    all_flight_and_countries.pop(i)
        # drop flights that not match to the destination country
        for i in reversed(range(len(all_flight_and_countries))):
            if self.destination_country != "0":
                if int(self.destination_country) != int(all_flight_and_countries[i][2].id):
                    all_flight_and_countries.pop(i)

        # drop flights that not match to the departure_time
        for i in reversed(range(len(all_flight_and_countries))):
            if self.departure_time != None:
                flight_date = all_flight_and_countries[i][0].departure_time
                request_date = self.departure_time 
                if not -1<=((request_date - flight_date).days)<=3:
                    all_flight_and_countries.pop(i)

        # drop flights that not match to the landing_time
        for i in reversed(range(len(all_flight_and_countries))):
            if self.landing_time != None:
                flight_date = all_flight_and_countries[i][0].landing_time
                request_date = self.landing_time 
                if not -1<=((request_date - flight_date).days)<=3:
                    all_flight_and_countries.pop(i)

        # drop flights that no tickets available
        for i in reversed(range(len(all_flight_and_countries))):
            tickets = all_flight_and_countries[i][0].remaining_tickets
            if tickets == 0:
                all_flight_and_countries.pop(i)

        if self.api:
            lst = []
            for item in all_flight_and_countries:
                temp = [item[0].toJson(),\
                        item[1].toJson(),\
                        item[2].toJson()]
                lst.append(temp)
            return jsonify(lst)     
            
        return all_flight_and_countries

    def get_all_airlines(self):
        dal_obj = DataLayer(table1=AirlineCompanies, api=self.api)       
        return dal_obj.get_all()

    def get_airline_by_id(self):
        dal_obj = DataLayer(table1=AirlineCompanies,id=self.id)      
        return dal_obj.get_by_id()

    # def get_airline_by_parameteres(self,origin_country_id,destination_country_id, date):
    #     pass

    def get_airline_by_name(self):
        dal_obj = DataLayer(table1=AirlineCompanies,input_attribute='name', input_value=self.name)
        return dal_obj.get_one_by_param()


    def get_country_by_id(self):
        dal_obj = DataLayer(api=self.api,table1=Countries,id=self.id)      
        return dal_obj.get_by_id()
    
    def get_admin_by_id(self):
        dal_obj = DataLayer(table1=Administrators,id=self.id)      
        return dal_obj.get_by_id()

    def create_new_user(self):
        user = Users(username=self.username,password=self.password,email=self.email,user_role=int(self.user_role))
        dal_obj = DataLayer()      
        return dal_obj.insert_obj(user)
    
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
    
    def get_flights_by_airline_id(self):
        dal_obj = DataLayer(table1=Flights,input_attribute='airline_company_id', input_value=int(self.airline_company_id))
        return dal_obj.get_all_by_filter()
    
    def get_ticket_by_flight_id(self):
        dal_obj = DataLayer(table1=Tickets,input_attribute='flight_id', input_value=self.flight_id)
        return dal_obj.get_one_by_param()
        
