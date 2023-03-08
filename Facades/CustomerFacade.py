from Facades.FacadeBase import *

class CustomerFacade(FacadeBase):

    def __init__(self, id=0,email="",user_id=""):
        super().__init__(id=id,email=email,user_id=user_id)


    def update_customer(self,customer):
        pass

    def add_ticket(self,ticket):
        pass

    def remove_ticket(self):
        dal_obj = DataLayer(id=self.id,table1=Tickets)
        ticket = dal_obj.get_by_id()
        return dal_obj.delete_obj(ticket)

    def get_my_ticket(self,ticket):
        pass

