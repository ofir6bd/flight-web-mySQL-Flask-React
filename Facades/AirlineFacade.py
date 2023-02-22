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
class AirlineFacade(FacadeBase):

    def __init__(self, id=0,username=""):
        super().__init__(id=id,username=username)
        

    def update_airline(airline):
        pass

    def add_flight(flight):
        pass

    def update_flight(flight):
        pass

    def remove_flight(flight):
        pass

    def get_my_flight():
        pass

    def get_airline_by_username(self):
        dal_obj = DataLayer(table1=AirlineCompanies,table_column1="user_id",\
                    table2=Users,table_column2="id",\
                    input_attribute="username",input_value=self.username)
        final_table = dal_obj.join_tables()
        # print(final_table)
        return final_table[0].name

with app.app_context():

    obj6 = AirlineFacade(username="Ofir8bd") 
    ans = obj6.get_airline_by_username()
    
    print(ans)
    print("Done")