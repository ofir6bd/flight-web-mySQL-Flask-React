from Facades.FacadeBase import *

class AdministratorFacade(FacadeBase):

    def __init__(self, id=0,name="",country_id="",user_id="",origin_country=""):
        super().__init__(id=id,user_id=user_id,origin_country=origin_country)
        self.country_id = country_id
        self.name = name

    def get_all_customers():
        pass

    def add_airline(self):
        new_airline = AirlineCompanies(name=self.name, country_id=self.country_id,user_id=int(self.user_id))
        dal_obj = DataLayer()
        return dal_obj.insert_obj(new_airline)


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
