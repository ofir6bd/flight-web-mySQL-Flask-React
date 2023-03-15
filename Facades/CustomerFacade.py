from flask import session
from Facades.FacadeBase import *
from flask import jsonify



class CustomerFacade(FacadeBase):

    def __init__(self,api=False, id=0,email="",user_id="",flight_id="",customer_id="",first_name=None\
                 ,last_name="",address="",phone_no="",credit_card_no=""):
        super().__init__(api=api,id=id,email=email,user_id=user_id,flight_id=flight_id,customer_id=customer_id\
                         ,first_name=first_name,last_name=last_name,address=address,\
                            phone_no=phone_no,credit_card_no=credit_card_no)


    def update_customer(self):
        dal_obj = DataLayer(id = self.id,table1=Customers)
        customer = dal_obj.get_by_id()
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

        # reduce ticket number from remainig tickets
        dal_obj = DataLayer(table1=Flights,id=self.flight_id)
        flight = dal_obj.get_by_id()
        flight.remaining_tickets = flight.remaining_tickets - 1
        res = dal_obj.update_item(flight)
        if res:
            dal_obj = DataLayer()
            return dal_obj.insert_obj(ticket)
        else:
            return res
    def remove_ticket(self):
        dal_obj = DataLayer(id=self.id,table1=Tickets)
        ticket = dal_obj.get_by_id()
        # adding ticket number to remainig tickets
        dal_obj = DataLayer(table1=Flights,id=ticket.flight_id)
        flight = dal_obj.get_by_id()
        flight.remaining_tickets = flight.remaining_tickets + 1
        res = dal_obj.update_item(flight)
        if res:
            dal_obj = DataLayer()
            return dal_obj.delete_obj(ticket)
        else:
            return res
        
        
    def get_my_ticket(self):
        dal_obj = DataLayer(api=self.api,table1=Tickets,input_attribute='customer_id', input_value=self.customer_id)
        all_my_tickets =  dal_obj.get_all_by_filter()
        
        dal_obj = DataLayer() 
        all_flight_and_countries = dal_obj.join_flights_countries()
        final_list = [] 
        for ticket in all_my_tickets:
            for i in range(len(all_flight_and_countries)):
                if ticket.flight_id == all_flight_and_countries[i][0].id:
                    final_list.append(all_flight_and_countries[i])

        if self.api:
            lst = []

            for i in range(len(final_list)):
                temp = [all_flight_and_countries[i][0].toJson(),\
                        all_flight_and_countries[i][1].toJson(),\
                            all_flight_and_countries[i][2].toJson()]
                lst.append(temp)
                # print(lst)
            return jsonify(lst)    

        return final_list





