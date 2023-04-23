"""
This data layer will be the only file that communicate with the DB, universal for all tables
"""
from app import create_app,db
from models import Users, Countries,Flights
from flask import flash
from sqlalchemy.orm import aliased
from flask import jsonify

app=create_app()


class DataLayer(object):

    def __init__(self,api=False, id=0, table1="",table_column1="",table2="",table_column2="",input_attribute="",input_value="",username="",password=""):
        self.api = api
        self.id = id
        self.table1 = table1
        self.table_column1 = table_column1
        self.table2 = table2
        self.table_column2 = table_column2
        self.input_attribute = input_attribute
        self.input_value = input_value
        self.username = username
        self.password = password


    def get_one_by_param(self):
        try:
            with app.app_context():
                item = self.table1.query.filter_by(**{self.input_attribute: self.input_value}).first()
        except Exception as e:
            print(f"Error: {e}")
        return item

    def get_by_id(self):
        try:
            with app.app_context():
                item = self.table1.query.filter_by(id=int(self.id)).first()
                if self.api:
                    return jsonify(item)
        except Exception as e:
            print(f"Error: {e}")
        return item
    
    def get_all(self):
        try:
            with app.app_context():
                items = self.table1.query.all()
                if self.api:
                    return jsonify([item.toJson() for item in items])    
        except Exception as e:
            print(f"Error: {e}")
        return items
    
    @staticmethod
    def insert_obj(obj):
        try:
            with app.app_context():
                db.session.add(obj)
                db.session.commit()
            return True
        except Exception as e:
            db.session.rollback()
            print(f"Error: {e}")
            flash(f"Duplcation error in Database!", "danger")
            return False
            
    def delete_obj(self, obj):
        try:
            with app.app_context():
                db.session.delete(obj)
                db.session.commit()
                return True
        except Exception as e:
            print(f"Error: {e}")
            flash(f"An error occured !", "danger")
            return False

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

    # join tables with one shared column
    def join_tables(self):
        try:
            with app.app_context():
                final_table = db.session.query(self.table1,self.table2).\
                    filter(getattr(self.table2, self.input_attribute)==self.input_value)\
                    .join(self.table1,getattr(self.table1, self.table_column1)==getattr(self.table2, self.table_column2)).first()
            return final_table
        except Exception as e:
            print(f"Error: {e}")

    
    def join_flights_countries(self):
        origin_country = aliased(Countries)
        dest_country = aliased(Countries)
        items = db.session.query(Flights, origin_country, dest_country)\
                        .join(origin_country, Flights.origin_country_id == origin_country.id)\
                        .join(dest_country, Flights.destination_country_id == dest_country.id)\
                        .all()
        return items
    
    def get_all_by_filter(self):
        try:
            with app.app_context():
                items = self.table1.query.filter_by(**{self.input_attribute: self.input_value}).all()
                return items
        except Exception as e:
            print(f"Error: {e}")


    def update_item(self,obj):
        try:
            with app.app_context():
                db.session.add(obj)
                db.session.commit()
        except Exception as e:
            print(f"Error: {e}")
            return False
        return True

