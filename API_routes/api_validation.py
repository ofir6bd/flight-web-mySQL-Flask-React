
import re
from Facades.CustomerFacade import CustomerFacade
from Facades.AnonymousFacade import AnonymousFacade
from Facades.AdministratorFacade import AdministratorFacade
from Facades.AirlineFacade import AirlineFacade

first_name_regex_pattern = re.compile(r"^[a-zA-Z\s]{1,50}$")
last_name_regex_pattern = re.compile(r"^[A-Za-z\s]{1,50}$")
address_regex_pattern = re.compile(r"^[A-Za-z0-9]{1,50}$")
phone_no_regex_pattern = re.compile(r"^[0-9]{10}$")
credit_card_no_regex_pattern = re.compile(r"^[0-9]{16}$")
user_id_regex_pattern = re.compile(r"^[0-9]{0,50}$")



def validate_customer(action="",first_name="",last_name="",address="",phone_no="",credit_card_no="",user_id=""):
    final_error_lst = []  
    if not first_name_regex_pattern.search(first_name) and first_name:
       final_error_lst.append({'first_name error': 'first name must contain characteres only 2 to 50'}) 
    if not last_name_regex_pattern.search(last_name) and last_name:
       final_error_lst.append({'last_name error': 'last name must contain characteres only 2 to 50'}) 
    if not address_regex_pattern.search(address) and address:
       final_error_lst.append({'address error': 'address name must contain characteres and digits only 2 to 50'}) 
    if not phone_no_regex_pattern.search(phone_no) and phone_no:
       final_error_lst.append({'phone_no error': 'phone_no must contain 10 digits only'}) 
    if not credit_card_no_regex_pattern.search(credit_card_no) and credit_card_no:
       final_error_lst.append({'credit_card_no error': 'credit_card_no must contain 16 digits only'}) 
    if not user_id_regex_pattern.search(str(user_id)) and user_id:
       final_error_lst.append({'user_id error': 'user_id must contain digits only'}) 
    
    if action != "update":
        fac_obj = CustomerFacade(id=user_id,user_id=user_id)
        customer = fac_obj.get_customer_by_user_id()
        if customer:
            final_error_lst.append({'error': 'Customer already exists for that user_id'}) 
        user = fac_obj.get_user_by_id()
        if user.user_role != 3:
            final_error_lst.append({'error': 'user role is not customer'}) 

    if len(final_error_lst) > 0:
       return final_error_lst
    else:
       return
    
name_regex_pattern = re.compile(r"^[a-zA-Z\s]{1,50}$")
country_id_regex_pattern = re.compile(r"^[0-9]{0,50}$")

def validate_airline(action="",name="",country_id="",user_id=""):
    final_error_lst = []  
    if not name_regex_pattern.search(name) and name:
       final_error_lst.append({'name error': 'name must contain characteres only 2 to 50'}) 
    if not country_id_regex_pattern.search(str(country_id)) and country_id:
       final_error_lst.append({'country_id error': 'country_id must contain digits only'}) 
    if not user_id_regex_pattern.search(str(user_id)) and user_id:
       final_error_lst.append({'user_id error': 'user_id must contain digits only'}) 
    
    if action != "update":
        fac_obj = AdministratorFacade(id=user_id,user_id=user_id)
        airline = fac_obj.get_airline_by_user_id()
        if airline:
            final_error_lst.append({'error': 'Airline already exists for that user_id'}) 
        user = fac_obj.get_user_by_id()
        if user.user_role != 2:
            final_error_lst.append({'error': 'user role is not airline'}) 

    if len(final_error_lst) > 0:
       return final_error_lst
    else:
       return

# print( validate_customer(first_name='fdfdd fdfd',last_name="rr",address="Atlit",phone_no="0548105702",credit_card_no="1234567891234567",user_id=2))
