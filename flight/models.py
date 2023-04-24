"""
This file configure the data base and the relationship between the tables.
"""
from app import db
from flask_login import UserMixin


class UserRoles(db.Model):
    __tablename__ = 'user_roles'
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    role_name = db.Column(db.String(50), nullable=False, unique=True)
    
    def __repr__(self): # for print option
        return f'<Table: "UserRoles", role_name:"{self.role_name}">'
    
    def toJson(self):
        return {'Table':'UserRoles','id': self.id, 'role_name': self.role_name}

class Users(db.Model,UserMixin):
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    username = db.Column(db.String(50), nullable=False, unique=True)
    password = db.Column(db.String(1000), nullable=False)
    email = db.Column(db.String(50), nullable=False, unique=True)
    user_role = db.Column(db.Integer, db.ForeignKey('user_roles.id'))
    user_role_ = db.relationship('UserRoles')
    

    def __repr__(self):
        return f'<Table: "Users", id:"{self.id}", username:"{self.username}", password:"{self.password}", email:"{self.email}", user_role:"{self.user_role}">'
    
    def toJson(self):
        return {'Table':'Users','id': self.id, 'username': self.username,'password': self.password, 'email': self.email,'user_role': self.user_role}

class Administrators(db.Model):
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    first_name = db.Column(db.String(50), nullable=False)
    last_name = db.Column(db.String(50), nullable=False)
    user_id = db.Column(db.Integer, db.ForeignKey('users.id'),unique=True)
    user = db.relationship('Users')

    def __repr__(self):
        return f'<Table: "Administrators",id:"{self.id}", first_name:"{self.first_name}, last_name:"{self.last_name}, user_id:"{self.user_id}">'

    def toJson(self):
        return {'Table':'Administrators','id': self.id, 'first_name': self.first_name,'last_name': self.last_name, 'user_id': self.user_id}


class Customers(db.Model):
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    first_name = db.Column(db.String(50), nullable=False)
    last_name = db.Column(db.String(50), nullable=False)
    address = db.Column(db.String(50), nullable=False)
    phone_no = db.Column(db.String(50), nullable=False, unique=True)
    credit_card_no = db.Column(db.String(50), nullable=False, unique=True)
    user_id = db.Column(db.Integer, db.ForeignKey('users.id'),unique=True)
    user = db.relationship('Users')

    def __repr__(self):
        return f'<Table: "Customers",id:"{self.id}", first_name:"{self.first_name}", last_name:"{self.last_name}, address:"{self.address},phone_no:"{self.phone_no}, credit_card_no:"{self.credit_card_no}, user_id:"{self.user_id} ">'

    def toJson(self):
        return {'Table':'Customers','id': self.id, 'first_name': self.first_name,'last_name': self.last_name, 'address': self.address,\
                'phone_no': self.phone_no,'credit_card_no': self.credit_card_no, 'user_id': self.user_id}


class Countries(db.Model):
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    name = db.Column(db.String(50), nullable=False, unique=True)
    
    def __repr__(self):
        return f'<Table: "Countries",id:"{self.id}", name:"{self.name}">'
    
    def toJson(self):
        return {'Table':'Countries','id': self.id, 'name': self.name}

class AirlineCompanies(db.Model):
    __tablename__ = 'airline_companies'
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    name = db.Column(db.String(50), nullable=False, unique=True)
    country_id = db.Column(db.Integer, db.ForeignKey('countries.id'))
    user_id = db.Column(db.Integer, db.ForeignKey('users.id'),unique=True)
    user = db.relationship('Users')
    
    def __repr__(self):
        return f'<Table: "AirlineCompanies",id:"{self.id}", name:"{self.name}", country_id:"{self.country_id}", user_id:"{self.user_id}">'

    def toJson(self):
        return {'Table':'AirlineCompanies','id': self.id, 'name': self.name,'country_id': self.country_id, 'user_id': self.user_id}


class Flights(db.Model):
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    airline_company_id = db.Column(db.Integer, db.ForeignKey('airline_companies.id'))
    airline_company = db.relationship('AirlineCompanies')
    origin_country_id = db.Column(db.Integer, db.ForeignKey('countries.id'))
    origin_country = db.relationship('Countries', foreign_keys=[origin_country_id])
    destination_country_id = db.Column(db.Integer, db.ForeignKey('countries.id'))
    destination_country = db.relationship('Countries', foreign_keys=[destination_country_id])
    departure_time = db.Column(db.DateTime, nullable=False)
    landing_time = db.Column(db.DateTime, nullable=False)
    remaining_tickets = db.Column(db.Integer, default=0)
    
    def __repr__(self):
        return f'<Table: "Flights",id:"{self.id}", airline_company_id:"{self.airline_company_id}", origin_country_id:"{self.origin_country_id}",destination_country_id:"{self.destination_country_id}",departure_time:"{self.departure_time}",landing_time:"{self.landing_time}",remaining_tickets:"{self.remaining_tickets}">'

    def toJson(self):
        return {'Table':'Flights','id': self.id, 'airline_company_id': self.airline_company_id,'origin_country_id': self.origin_country_id,\
                 'destination_country_id': self.destination_country_id,'departure_time': self.departure_time,\
                    'landing_time': self.landing_time,'remaining_tickets': self.remaining_tickets}


class Tickets(db.Model):
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    flight_id = db.Column(db.Integer, db.ForeignKey('flights.id'))
    flight = db.relationship('Flights')
    customer_id = db.Column(db.Integer, db.ForeignKey('customers.id'))
    customer = db.relationship('Customers')
    
    def __repr__(self):
        return f'<Table: "Tickets",id:"{self.id}", flight_id:"{self.flight_id}",customer_id:"{self.customer_id}">'

    def toJson(self):
        return {'Table':'Tickets','id': self.id, 'flight_id': self.flight_id,'customer_id': self.customer_id}



