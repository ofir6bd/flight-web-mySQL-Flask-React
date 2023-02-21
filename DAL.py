"""
This data layer will be the only file that communicate with the DB, universal for all tables
"""
from tables_schema import *

class DataLayer(object):

    def __init__(self, id=0, table=""):
        self.id = id
        self.table = table

        
    def get_by_id(self):
        item = self.table.query.filter_by(id=self.id).first()
        return item
    
    def get_all(self):
        item = self.table.query.all()
        return item
    
    def insert_obj(self, obj):
        try:
            db.session.add(obj)
            db.session.commit()
        except Exception as e:
            print(f"Error: {e}")
    
    


######################### testing functions
# with app.app_context():
#     # obj1 = FacadeBase() 
#     # ans = obj1.get_flight_by_id(1)
#     obj1 = DataLayer() 
#     ans = obj1.get_all(Flights)
#     print(ans)
#     print("Done")