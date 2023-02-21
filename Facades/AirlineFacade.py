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