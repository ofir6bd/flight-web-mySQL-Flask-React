from Facades.FacadeBase import *

class AdministratorFacade(FacadeBase):

    def __init__(self, id=0,name="",country_id="",user_id="",origin_country="",first_name="",last_name="",address="",phone_no="",credit_card_no=""):
        super().__init__(id=id,user_id=user_id,origin_country=origin_country,first_name=first_name,last_name=last_name,address=address,phone_no=phone_no,credit_card_no=credit_card_no)
        self.country_id = country_id
        self.name = name

    def get_all_customers():
        pass

    def add_airline(self):
        new_airline = AirlineCompanies(name=self.name, country_id=self.country_id,user_id=int(self.user_id))
        dal_obj = DataLayer()
        return dal_obj.insert_obj(new_airline)


    def add_customer(self):
        new_customer = Customers(first_name=self.first_name,last_name=self.last_name,address=self.address,phone_no=self.phone_no,credit_card_no=self.credit_card_no,user_id=int(self.user_id))
        dal_obj = DataLayer()
        return dal_obj.insert_obj(new_customer)

    def add_administrator(self):
        new_admin = Administrators(first_name=self.first_name,last_name=self.last_name,user_id=int(self.user_id))
        dal_obj = DataLayer()
        return dal_obj.insert_obj(new_admin)

    def remove_airline(airline):
        pass

    def remove_customer(customer):
        pass

    def remove_administrator(administrator):
        pass
