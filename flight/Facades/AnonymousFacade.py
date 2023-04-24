""" 
This file is connecting between the DAL (the connection to the DB) and the views, for the general functions
"""
from Facades.FacadeBase import *

class AnonymousFacade(FacadeBase):

    def __init__(self,api=False,id="",name="",username="", password="", email="",user_role="",user_id="",\
                origin_country="",destination_country="",departure_time=None,\
                landing_time="",travelers="",first_name="",last_name="",address="",phone_no="",credit_card_no=""):
        super().__init__(api=api,id=id,name=name,username=username,password=password,email=email,\
                        user_role=user_role,user_id=user_id,origin_country=origin_country,\
                        destination_country=destination_country,departure_time=departure_time,\
                        landing_time=landing_time,travelers=travelers,first_name=first_name,last_name=last_name,address=address\
                            ,phone_no=phone_no,credit_card_no=credit_card_no)


    def login(self):
        dal_obj = DataLayer(username=self.username,password=self.password)      
        result = dal_obj.check_user_and_pass()
        return result


    def add_customer(self):
        new_customer = Customers(first_name=self.first_name,last_name=self.last_name,address=self.address,phone_no=self.phone_no,credit_card_no=self.credit_card_no,user_id=int(self.user_id))
        dal_obj = DataLayer()
        return dal_obj.insert_obj(new_customer)

