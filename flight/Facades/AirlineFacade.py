from Facades.FacadeBase import *
from flask import jsonify

class AirlineFacade(FacadeBase):

    def __init__(self,api=False, user_id="",id=0,name="",flight_id="",username="",airline_company_id="",origin_country_id="",destination_country_id="",departure_time="",landing_time="",remaining_tickets=""):
        super().__init__(api=api,user_id=user_id,id=id,flight_id=flight_id,username=username,airline_company_id=airline_company_id,name=name,\
                        origin_country_id=origin_country_id,destination_country_id=destination_country_id,departure_time=departure_time,landing_time=landing_time,remaining_tickets=remaining_tickets)
        

    def update_airline(self):
        dal_obj = DataLayer(id = self.id,table1=AirlineCompanies)
        airline = dal_obj.get_by_id()
        if (self.name != airline.name) and self.name:
            airline.name = self.name
        dal_obj = DataLayer()
        return dal_obj.update_item(airline)


    def add_flight(self):
        flight = Flights(airline_company_id=self.airline_company_id,
                                origin_country_id=self.origin_country_id,
                                destination_country_id=self.destination_country_id,
                                departure_time=self.departure_time,
                                landing_time=self.landing_time,
                                remaining_tickets=self.remaining_tickets)
        dal_obj = DataLayer()
        return dal_obj.insert_obj(flight)

    def update_flight(self):
        dal_obj = DataLayer(id = self.id,table1=Flights)
        flight = dal_obj.get_by_id()
        if (self.origin_country_id != flight.origin_country_id) and self.origin_country_id:
            flight.origin_country_id = self.origin_country_id
        if (self.destination_country_id != flight.destination_country_id) and self.destination_country_id:
            flight.destination_country_id = self.destination_country_id
        if (self.departure_time != flight.departure_time) and self.departure_time:
            flight.departure_time = self.departure_time
        if (self.landing_time != flight.landing_time) and self.landing_time:
            flight.landing_time = self.landing_time
        if (self.remaining_tickets != flight.remaining_tickets) and self.remaining_tickets:
            flight.remaining_tickets = self.remaining_tickets
        
        dal_obj = DataLayer()
        return dal_obj.update_item(flight)

    def remove_flight(self):
        dal_obj = DataLayer(id=self.id,table1=Flights)
        flight = dal_obj.get_by_id()
        return dal_obj.delete_obj(flight)

    def get_my_flights(self):
        dal_obj = DataLayer(table1=AirlineCompanies,input_attribute='name', input_value=self.name)
        airline = dal_obj.get_one_by_param()
        dal_obj = DataLayer(table1=Flights,input_attribute='airline_company_id', input_value=int(airline.id))
        flights = dal_obj.get_all_by_filter()
        
        if self.api:
            dal_obj = DataLayer()
            all_flights_countries = dal_obj.join_flights_countries() 
            lst = []
            for flight in flights:
                for i in range(len(all_flights_countries)):
                    if flight.id == all_flights_countries[i][0].id:
                        flight_id = all_flights_countries[i][0].id
                        departure_time = all_flights_countries[i][0].departure_time
                        landing_time = all_flights_countries[i][0].landing_time
                        origin_country = all_flights_countries[i][1].name
                        destination_country = all_flights_countries[i][2].name
                        temp = {"flight_id": flight_id,"departure_time": departure_time,"landing_time": landing_time, "origin_country":origin_country,"destination_country":destination_country }
                        lst.append(temp)
            return jsonify(lst)    
        return flights

    def get_airline_by_username(self):
        dal_obj = DataLayer(table1=AirlineCompanies,table_column1="user_id",\
                    table2=Users,table_column2="id",\
                    input_attribute="username",input_value=self.username)
        final_table = dal_obj.join_tables()
        # print(final_table)
        return final_table[0].name
