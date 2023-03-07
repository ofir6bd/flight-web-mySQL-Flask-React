from Facades.FacadeBase import *

class AirlineFacade(FacadeBase):

    def __init__(self, id=0,username="",airline_company_id="",origin_country_id="",destination_country_id="",departure_time="",landing_time="",remaining_tickets=""):
        super().__init__(id=id,username=username,\
                         origin_country_id=origin_country_id,destination_country_id=destination_country_id,departure_time=departure_time,landing_time=landing_time,remaining_tickets=remaining_tickets)
        self.airline_company_id = airline_company_id

    def update_airline(airline):
        pass

    def add_flight(self):

        flight = Flights(airline_company_id=self.airline_company_id,
                                origin_country_id=self.origin_country_id,
                                destination_country_id=self.destination_country_id,
                                departure_time=self.departure_time,
                                landing_time=self.landing_time,
                                remaining_tickets=2)
        dal_obj = DataLayer()
        return dal_obj.insert_obj(flight)

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



# # ######################### testing functions
# with app.app_context():

#     obj6 = AirlineFacade(username="Ofir7bd") 
#     ans = obj6.get_airline_by_username()
    
#     print(ans)
#     print("Done")