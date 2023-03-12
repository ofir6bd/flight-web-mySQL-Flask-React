from flask import session
from Facades.FacadeBase import *

class CustomerFacade(FacadeBase):

    def __init__(self, id=0,email="",user_id="",flight_id=""):
        super().__init__(id=id,email=email,user_id=user_id,flight_id=flight_id)


    def update_customer(self,customer):
        pass

    def add_ticket(self):
        dal_obj = DataLayer(table1=Customers,input_attribute='user_id', input_value=int(session['user_id']))
        user = dal_obj.get_one_by_param()
        ticket = Tickets(flight_id=self.flight_id,customer_id=user.id)
        dal_obj = DataLayer()
        return dal_obj.insert_obj(ticket)

    def remove_ticket(self):
        dal_obj = DataLayer(id=self.id,table1=Tickets)
        ticket = dal_obj.get_by_id()
        return dal_obj.delete_obj(ticket)

    def get_my_ticket(self,ticket):
        pass

