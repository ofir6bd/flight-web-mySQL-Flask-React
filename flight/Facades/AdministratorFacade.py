""" 
This file is connecting between the DAL (the connection to the DB) and the views, for the admin functions
"""

from Facades.FacadeBase import *

class AdministratorFacade(FacadeBase):

    def __init__(self,api=False, id=0,name="",country_id="",user_id="",origin_country="",first_name="",last_name="",address="",phone_no="",credit_card_no=""):
        super().__init__(api=api,id=id,user_id=user_id,origin_country=origin_country,first_name=first_name,last_name=last_name,address=address,phone_no=phone_no,credit_card_no=credit_card_no)
        self.country_id = country_id
        self.name = name


    def add_airline(self):
        new_airline = AirlineCompanies(name=self.name, country_id=self.country_id,user_id=int(self.user_id))
        dal_obj = DataLayer()
        return dal_obj.insert_obj(new_airline)


    def add_customer(self):
        new_customer = Customers(first_name=self.first_name,last_name=self.last_name,address=self.address,phone_no=self.phone_no,credit_card_no=self.credit_card_no,user_id=int(self.user_id))
        dal_obj = DataLayer()
        return dal_obj.insert_obj(new_customer)


    def add_administrator(self):
        new_admin = Administrators(first_name=self.first_name,last_name=self.last_name,user_id=int(self.user_id))
        dal_obj = DataLayer()
        return dal_obj.insert_obj(new_admin)


    def remove_airline(self):
        dal_obj = DataLayer(id=self.id,table1=AirlineCompanies)
        airline = dal_obj.get_by_id()
        return dal_obj.delete_obj(airline)


    def remove_customer(self):
        dal_obj = DataLayer(id=self.id,table1=Customers)
        customer = dal_obj.get_by_id()
        return dal_obj.delete_obj(customer)


    def remove_administrator(self):
        dal_obj = DataLayer(id=self.id,table1=Administrators)
        admin = dal_obj.get_by_id()
        return dal_obj.delete_obj(admin)
    
    
    def get_all_users_pre_customer(self):
        dal_obj = DataLayer(id=self.id,table1=Customers)
        customers = dal_obj.get_all()
        dal_obj = DataLayer(id=self.id,table1=Users,input_attribute='user_role', input_value=int(3))
        users = dal_obj.get_all_by_filter()
        if self.api:
            for i in reversed(range(len(users))):
                for customer in customers:
                    if customer.user_id == users[i].id:
                        users.pop(i)
                        break
                          
            return jsonify([user.toJson() for user in users])


    def get_all_users_pre_admin(self):
        dal_obj = DataLayer(id=self.id,table1=Administrators)
        admins = dal_obj.get_all()
        dal_obj = DataLayer(id=self.id,table1=Users,input_attribute='user_role', input_value=int(1))
        users = dal_obj.get_all_by_filter()
        if self.api:
            for i in reversed(range(len(users))):
                for admin in admins:
                    if admin.user_id == users[i].id:
                        users.pop(i)
                        break
                          
            return jsonify([user.toJson() for user in users])


    def get_all_users_pre_airline(self):
        dal_obj = DataLayer(id=self.id,table1=AirlineCompanies)
        airlines = dal_obj.get_all()
        dal_obj = DataLayer(id=self.id,table1=Users,input_attribute='user_role', input_value=int(2))
        users = dal_obj.get_all_by_filter()
        
        if self.api:
            for i in reversed(range(len(users))):
                for airline in airlines:
                    if airline.user_id == users[i].id:
                        users.pop(i)
                        break
                          
            return jsonify([user.toJson() for user in users])
