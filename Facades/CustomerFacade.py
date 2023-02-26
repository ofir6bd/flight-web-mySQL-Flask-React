import sys
import os
 
# import a module in the parent
current = os.path.dirname(os.path.realpath(__file__))
# Getting the parent directory name
parent = os.path.dirname(current)
# adding the parent directory to the sys.path.
sys.path.append(parent)
from DAL import *
from FacadeBase import FacadeBase

class CustomerFacade(FacadeBase):

    def __init__(self, id=0):
        super().__init__(id=id)

    def update_customer(self,customer):
        pass

    def add_ticket(self,ticket):
        pass

    def remove_ticket(self):
        dal_obj = DataLayer(id=self.id,table=Tickets)
        ticket = dal_obj.get_by_id()
        dal_obj.delete_obj(ticket)
        print('record deleted')

    def get_my_ticket(self,ticket):
        pass

# with app.app_context():
#     # obj4 = CustomerFacade(id=1) 
#     # ans = obj4.login()

#     obj5 = CustomerFacade(id=2) 
#     obj5.remove_ticket()
    
#     # print(ans)
#     print("Done")