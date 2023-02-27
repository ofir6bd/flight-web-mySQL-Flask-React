"""
This data layer will be the only file that communicate with the DB, universal for all tables
"""
from tables_schema import *

class DataLayer(object):

    def __init__(self, id=0, table1="",table_column1="",table2="",table_column2="",input_attribute="",input_value="",username="",password=""):
        self.id = id
        self.table1 = table1
        self.table_column1 = table_column1
        self.table2 = table2
        self.table_column2 = table_column2
        self.input_attribute = input_attribute
        self.input_value = input_value
        self.username = username
        self.password = password

    def get_by_id(self):
        try:
            with app.app_context():
                item = self.table1.query.filter_by(id=self.id).first()
        except Exception as e:
            print(f"Error: {e}")
        return item
    
    def get_all(self):
        try:
            with app.app_context():
                item = self.table1.query.all()
        except Exception as e:
            print(f"Error: {e}")
        return item
    
    def insert_obj(self, obj):
        try:
            with app.app_context():
                # print(obj)
                db.session.add(obj)
                db.session.commit()
            return True
        except Exception as e:
            print(f"Error: {e}")
            return False

    def delete_obj(self, obj):
        try:
            with app.app_context():
                db.session.delete(obj)
                db.session.commit()
        except Exception as e:
            print(f"Error: {e}")

    def check_user_and_pass(self):
        try:
            with app.app_context():
                user = Users.query.filter_by(username=self.username,password=self.password).first()
            if user:
                return True
            else:
                return False
        except Exception as e:
            print(f"Error: {e}")

    def join_tables(self):
        try:
            with app.app_context():
                final_table = db.session.query(self.table1,self.table2).\
                    filter(getattr(self.table2, self.input_attribute)==self.input_value)\
                    .join(self.table1,getattr(self.table1, self.table_column1)==getattr(self.table2, self.table_column2)).first()
            return final_table
        except Exception as e:
            print(f"Error: {e}")
        

    
    


# ######################### testing functions
# with app.app_context():
#     dal_obj = DataLayer(table=AirlineCompanies,table2=Users,username="Ofir9bd",table_column="user_id")
#     final_table = dal_obj.join_tables()    
#     print(final_table[0].name)
#     print("Done")
# # #     # obj1 = FacadeBase() 
# # #     # ans = obj1.get_flight_by_id(1)
# # #     obj1 = DataLayer() 
# # #     ans = obj1.get_all(Flights)
#     ans = db.session.query(AirlineCompanies,Users ).filter(Users.username=='Ofir7bd').join(AirlineCompanies,AirlineCompanies.user_id==Users.id).first()
#     print(ans)
#     print("Done")