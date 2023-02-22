"""
This data layer will be the only file that communicate with the DB, universal for all tables
"""
from tables_schema import *

class DataLayer(object):

    def __init__(self, id=0, table="",table_column="",table2="",username="",password=""):
        self.id = id
        self.table = table
        self.table_column = table_column
        self.table2 = table2
        self.username = username
        self.password = password

    def get_by_id(self):
        try:
            item = self.table.query.filter_by(id=self.id).first()
        except Exception as e:
            print(f"Error: {e}")
        return item
    
    def get_all(self):
        try:
            item = self.table.query.all()
        except Exception as e:
            print(f"Error: {e}")
        return item
    
    def insert_obj(self, obj):
        try:
            db.session.add(obj)
            db.session.commit()
        except Exception as e:
            print(f"Error: {e}")

    def delete_obj(self, obj):
        try:
            db.session.delete(obj)
            db.session.commit()
        except Exception as e:
            print(f"Error: {e}")

    def check_user_and_pass(self):
        try:
            user = Users.query.filter_by(username=self.username,password=self.password).first()
            if user:
                return True
            else:
                return False
        except Exception as e:
            print(f"Error: {e}")

    def join_tables(self):
        final_table = db.session.query(self.table,self.table2 ).filter(self.table2.username==self.username).join(self.table,self.table.user_id==self.table2.id).first()
        return final_table

    
    


# ######################### testing functions
# with app.app_context():
# # #     # obj1 = FacadeBase() 
# # #     # ans = obj1.get_flight_by_id(1)
# # #     obj1 = DataLayer() 
# # #     ans = obj1.get_all(Flights)
#     ans = db.session.query(AirlineCompanies,Users ).filter(Users.username=='Ofir7bd').join(AirlineCompanies,AirlineCompanies.user_id==Users.id).first()
#     print(ans)
#     print("Done")