import sys
import os
 
# import a module in the parent
current = os.path.dirname(os.path.realpath(__file__))
# Getting the parent directory name
parent = os.path.dirname(current)
# adding the parent directory to the sys.path.
sys.path.append(parent)
from DAL import *
from Facades.FacadeBase import FacadeBase

class AnonymousFacade(FacadeBase):

    def __init__(self, username="", password="", email="",user_role="",origin_country="",destination_country="",departure_time="",landing_time="",travelers=""):
        super().__init__(username=username,password=password,email=email,user_role=user_role,origin_country=origin_country,destination_country=destination_country,departure_time=departure_time,landing_time=landing_time,travelers=travelers)

    def login(self):
        dal_obj = DataLayer(username=self.username,password=self.password)      
        result = dal_obj.check_user_and_pass()
        return result

    def add_customer():
        #TODO need to send all parameteres for this function
        pass


# with app.app_context():
#     obj3 = AnonymousFacade(username="Ofir6bd",password="123456789") 
#     ans = obj3.login()
    
#     print(ans)
#     print("Done")
