from flask import session
from Facades.FacadeBase import *

class CustomerFacade(FacadeBase):

    def __init__(self, id=0,email="",user_id="",flight_id="",customer_id="",first_name=None\
                 ,last_name="",address="",phone_no="",credit_card_no=""):
        super().__init__(id=id,email=email,user_id=user_id,flight_id=flight_id,customer_id=customer_id\
                         ,first_name=first_name,last_name=last_name,address=address,\
                            phone_no=phone_no,credit_card_no=credit_card_no)


    def update_customer(self):
        dal_obj = DataLayer(id = self.id,table1=Customers)
        customer = dal_obj.get_by_id()
        print(self.first_name)
        print(customer.first_name)
        if (self.first_name != customer.first_name) and self.first_name:
            customer.first_name = self.first_name
        if (self.last_name != customer.last_name) and self.last_name:
            customer.last_name = self.last_name
        if (self.address != customer.address) and self.address:
            customer.address = self.address
        if (self.phone_no != customer.phone_no) and self.phone_no:
            customer.phone_no = self.phone_no
        if (self.credit_card_no != customer.credit_card_no) and self.credit_card_no:
            customer.credit_card_no = self.credit_card_no
        dal_obj = DataLayer()
        return dal_obj.update_item(customer)

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

    def get_my_ticket(self):
        dal_obj = DataLayer(table1=Tickets,input_attribute='customer_id', input_value=self.customer_id)
        all_my_tickets =  dal_obj.get_all_by_filter()

        dal_obj = DataLayer() 
        all_flight_and_countries = dal_obj.join_flights_countries()
        final_list = [] 
        for ticket in all_my_tickets:
            # print(ticket.flight_id)
            for i in range(len(all_flight_and_countries)):
                if ticket.flight_id == all_flight_and_countries[i][0].id:
                    final_list.append(all_flight_and_countries[i])
        return final_list





