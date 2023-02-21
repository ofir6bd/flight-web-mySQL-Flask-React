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

class AdministratorFacade(FacadeBase):

    def get_all_customers():
        pass

    def add_airline():
        #TODO need to send all parameteres for this function
        pass

    def add_customer():
        #TODO need to send all parameteres for this function
        pass

    def add_administrator():
        #TODO need to send all parameteres for this function
        pass

    def remove_airline(airline):
        pass

    def remove_customer(customer):
        pass

    def remove_administrator(administrator):
        pass
