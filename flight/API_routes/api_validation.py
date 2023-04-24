"""
      this page validating the inputs values of the api
"""

import re
from Facades.CustomerFacade import CustomerFacade
from Facades.AnonymousFacade import AnonymousFacade
from Facades.AdministratorFacade import AdministratorFacade
from Facades.AirlineFacade import AirlineFacade
from datetime import datetime
 
# regex patterns in order to check the inputs
first_name_regex_pattern = re.compile(r"^[a-zA-Z\s]{1,50}$")
last_name_regex_pattern = re.compile(r"^[A-Za-z\s]{1,50}$")
address_regex_pattern = re.compile(r"^[A-Za-z0-9]{1,50}$")
phone_no_regex_pattern = re.compile(r"^[0-9]{10}$")
credit_card_no_regex_pattern = re.compile(r"^[0-9]{16}$")
user_id_regex_pattern = re.compile(r"^[0-9]{0,50}$")

def validate_customer(action="",first_name="",last_name="",address="",phone_no="",credit_card_no="",user_id=""):
   final_error_lst = []  
   if not first_name_regex_pattern.search(first_name) and first_name:
      final_error_lst.append({'error': 'first name must contain characteres only 2 to 50'}) 
   if not last_name_regex_pattern.search(last_name) and last_name:
      final_error_lst.append({'error': 'last name must contain characteres only 2 to 50'}) 
   if not address_regex_pattern.search(address) and address:
      final_error_lst.append({'error': 'address name must contain characteres and digits only 2 to 50'}) 
   if not phone_no_regex_pattern.search(phone_no) and phone_no:
      final_error_lst.append({'error': 'phone_no must contain 10 digits only'}) 
   if not credit_card_no_regex_pattern.search(credit_card_no) and credit_card_no:
      final_error_lst.append({'error': 'credit_card_no must contain 16 digits only'}) 
   if not user_id_regex_pattern.search(str(user_id)) and user_id:
      final_error_lst.append({'error': 'user_id must contain digits only'}) 
   
   fac_obj = AirlineFacade(id=user_id)
   if not fac_obj.get_user_by_id():
      final_error_lst.append({'error': 'user_id not found'}) 
   
   if action != "update":
      fac_obj = CustomerFacade(id=user_id,user_id=user_id)
      customer = fac_obj.get_customer_by_user_id()
      if customer:
         final_error_lst.append({'error': 'Customer already exists for that user_id'}) 
      user = fac_obj.get_user_by_id()
      if user:
         if user.user_role != 3:
            final_error_lst.append({'error': 'user role for this user is not customer'}) 

   if len(final_error_lst) > 0:
      return final_error_lst
   else:
      return
   
   
name_regex_pattern = re.compile(r"^[a-zA-Z\s]{1,50}$")
country_id_regex_pattern = re.compile(r"^[0-9]{0,50}$")

def validate_airline(action="",name="",country_id="",user_id=""):
   final_error_lst = []  
   if not name_regex_pattern.search(name) and name:
      final_error_lst.append({'error': 'name must contain characters only 2 - 50'}) 
   if not country_id_regex_pattern.search(str(country_id)) and country_id:
      final_error_lst.append({'error': 'country_id must contain digits only'}) 
   if not user_id_regex_pattern.search(str(user_id)) and user_id:
      final_error_lst.append({'error': 'user_id must contain digits only'}) 
   
   fac_obj = AirlineFacade(id=country_id)
   if not fac_obj.get_country_by_id():
      final_error_lst.append({'error': 'country_id not found'}) 
   fac_obj = AirlineFacade(id=user_id)
   if not fac_obj.get_user_by_id():
      final_error_lst.append({'error': 'user_id not found'}) 
      
   if action != "update":
      fac_obj = AdministratorFacade(id=user_id,user_id=user_id)
      airline = fac_obj.get_airline_by_user_id()
      if airline:
         final_error_lst.append({'error': 'Airline already exists for that user_id'}) 
      user = fac_obj.get_user_by_id()
      if user:
         if user.user_role != 2:
            final_error_lst.append({'error': 'user role for this user is not airline'}) 

   if len(final_error_lst) > 0:
      return final_error_lst
   else:
      return


def validate_admin(action="",first_name="",last_name="",user_id=""):
   final_error_lst = []  
   if not first_name_regex_pattern.search(first_name) and first_name:
      final_error_lst.append({'error': 'first name must contain characteres only 2 - 50'}) 
   if not last_name_regex_pattern.search(last_name) and last_name:
      final_error_lst.append({'error': 'last name must contain characteres only 2 - 50'}) 
   if not user_id_regex_pattern.search(str(user_id)) and user_id:
      final_error_lst.append({'error': 'user_id must contain digits only'}) 
   
   fac_obj = AirlineFacade(id=user_id)
   if not fac_obj.get_user_by_id():
      final_error_lst.append({'error': 'user_id not found'}) 
      
   if action != "update":
      fac_obj = AdministratorFacade(id=user_id,user_id=user_id)
      admin = fac_obj.get_admin_by_user_id()
      if admin:
         final_error_lst.append({'error': 'Admin already exists for that user_id'}) 
      user = fac_obj.get_user_by_id()
      if user:
         if user.user_role != 1:
            final_error_lst.append({'error': 'user role for this user is not admin'}) 
   if len(final_error_lst) > 0:
      return final_error_lst
   else:
      return
   
flight_id_regex_pattern = re.compile(r"^[0-9]{0,50}$")


def validate_ticket(flight_id="",customer_id=""):
   final_error_lst = []  
   if not flight_id_regex_pattern.search(flight_id) and flight_id:
      final_error_lst.append({'error': 'flight_id must contain digits only'}) 
   
   fac_obj = CustomerFacade(id=flight_id,flight_id=flight_id,customer_id=customer_id)
   res = fac_obj.check_one_flight_customer_combination_on_ticket()
   if res:
      final_error_lst.append({'error': 'The same customer cannot buy the same ticket'}) 
   flight = fac_obj.get_flight_by_id()
   if not flight:
      final_error_lst.append({'error': 'Flight_id did not found'}) 

   if len(final_error_lst) > 0:
      return final_error_lst
   else:
      return
   

origin_country_id_regex_pattern = re.compile(r"^[0-9]{0,50}$")
destination_country_id_regex_pattern = re.compile(r"^[0-9]{0,50}$")
departure_time_regex_pattern = re.compile(r"\d{4}-\d{2}-\d{2}\s\d{2}:\d{2}")
landing_time_regex_pattern = re.compile(r"\d{4}-\d{2}-\d{2}\s\d{2}:\d{2}")
remaining_tickets_regex_pattern = re.compile(r"[0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0]")

def validate_flight(action="",id="",origin_country_id="",destination_country_id="",departure_time="",landing_time="",remaining_tickets=""):
   final_error_lst = []  
   if not flight_id_regex_pattern.search(str(origin_country_id)) and origin_country_id:
      final_error_lst.append({'error': 'origin_country_id must contain digits only'}) 
   if not destination_country_id_regex_pattern.search(str(destination_country_id)) and destination_country_id:
      final_error_lst.append({'error': 'destination_country_id must contain digits only'}) 
   if not departure_time_regex_pattern.search(str(departure_time)) and departure_time:
      final_error_lst.append({'error': 'departure_time must be in format: "%Y-%m-%dT%H:%M"'}) 
   if not landing_time_regex_pattern.search(str(landing_time)) and landing_time:
      final_error_lst.append({'error': 'landing_time must be in format: "%Y-%m-%dT%H:%M"'}) 
   if not remaining_tickets_regex_pattern.search(str(remaining_tickets)) and remaining_tickets:
      final_error_lst.append({'error': 'remaining_tickets must be between 0-250'}) 
   
   
   # validate FK
   if origin_country_id:
      fac_obj = AirlineFacade(id=origin_country_id)
      if not fac_obj.get_country_by_id():
         final_error_lst.append({'error': 'origin country id not found'}) 
   if destination_country_id:
      fac_obj = AirlineFacade(id=destination_country_id)
      if not fac_obj.get_country_by_id():
         final_error_lst.append({'error': 'destination country id not found'}) 
   
   if action == 'update':
      fac_obj = AirlineFacade(id=id)
      flight = fac_obj.get_flight_by_id()
      origin_c_id = flight.origin_country_id
      destination_c_id = flight.destination_country_id
      if origin_country_id:
         origin_c_id = origin_country_id
      if destination_country_id:
         destination_c_id = destination_country_id
      if str(origin_c_id) == str(destination_c_id):
         final_error_lst.append({'error': 'origin and destination countries cannot be the same'}) 
   else:     
      if origin_country_id == destination_country_id:
         final_error_lst.append({'error': 'origin and destination countries cannot be the same'}) 
      
   if len(final_error_lst) > 0:
      return final_error_lst
   else:
      return
      
      
def validate_dates(departure_time,landing_time):
   final_error_lst = [] 
   try:
      departure_time = datetime.strptime(departure_time, '%Y-%m-%dT%H:%M')
   except Exception as e:
         print(f"Error: {e}")
         final_error_lst.append({'error': 'departure_time must be in format: "%Y-%m-%dT%H:%M"'}) 
   try:
      landing_time = datetime.strptime(landing_time, '%Y-%m-%dT%H:%M')
   except Exception as e:
         print(f"Error: {e}")
         final_error_lst.append({'error': 'landing_time must be in format: "%Y-%m-%dT%H:%M"'}) 
         
   if len(final_error_lst) > 0:
      return final_error_lst
   else:
      return
   
   
username_regex_pattern = re.compile(r"^[a-zA-Z\s]{1,50}$")
password_regex_pattern = re.compile(r"^(?=.*[A-Za-z])(?=.*\d)[A-Za-z\d]{8,}$")
email_regex_pattern = re.compile(r"([A-Za-z0-9]+[.-_])*[A-Za-z0-9]+@[A-Za-z0-9-]+(\.[A-Z|a-z]{2,})+")
user_role_regex_pattern = re.compile(r"^[1-3]$")

def validate_user(action="",username="",password="",email="",user_role=""):
   final_error_lst = []  
   if not username_regex_pattern.search(username) and username:
      final_error_lst.append({'error': 'username must contain characteres only 2 to 50'}) 
   if not password_regex_pattern.search(password) and password:
      final_error_lst.append({'error': 'password rules-Minimum eight characters, at least one letter and one number'}) 
   if not email_regex_pattern.search(email) and email:
      final_error_lst.append({'error': 'email not legal'}) 
   if not user_role_regex_pattern.search(user_role) and user_role:
      final_error_lst.append({'error': 'user_role can be 1, 2 or 3'}) 
   
   fac_obj = AnonymousFacade(username=username,email=email)
   if fac_obj.get_user_by_username():
      final_error_lst.append({'error': 'username already taken'}) 
   if fac_obj.get_user_by_email():
      final_error_lst.append({'error': 'email already taken'}) 
   
   if len(final_error_lst) > 0:
      return final_error_lst
   else:
      return