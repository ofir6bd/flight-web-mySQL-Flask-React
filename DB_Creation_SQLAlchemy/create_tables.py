from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime


app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql://root:admin@localhost/flight_db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)

class UserRoles(db.Model):
    __tablename__ = 'user_roles'
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    role_name = db.Column(db.String(50), nullable=False, unique=True)
    
    def __repr__(self): # for print option
        return f'<Table: "UserRoles", role_name:"{self.role_name}">'

class Users(db.Model):
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    username = db.Column(db.String(50), nullable=False, unique=True)
    password = db.Column(db.String(50), nullable=False)
    email = db.Column(db.String(50), nullable=False, unique=True)
    user_role = db.Column(db.Integer, db.ForeignKey('user_roles.id'))
    user_role_ = db.relationship('UserRoles')

    def __repr__(self):
        return f'<Table: "Users", id:"{self.id}", username:"{self.username}, password:"{self.password}, email:"{self.email}, user_role:"{self.user_role}">'

class Administrators(db.Model):
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    first_name = db.Column(db.String(50), nullable=False)
    last_name = db.Column(db.String(50), nullable=False)
    user_id = db.Column(db.Integer, db.ForeignKey('users.id'))
    user = db.relationship('Users')

    def __repr__(self):
        return f'<Table: "Administrators",id:"{self.id}", first_name:"{self.first_name}, last_name:"{self.last_name}, user_id:"{self.user_id}">'

class Customers(db.Model):
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    first_name = db.Column(db.String(50), nullable=False)
    last_name = db.Column(db.String(50), nullable=False)
    address = db.Column(db.String(50), nullable=False)
    phone_no = db.Column(db.String(50), nullable=False, unique=True)
    credit_card_no = db.Column(db.String(50), nullable=False, unique=True)
    user_id = db.Column(db.Integer, db.ForeignKey('users.id'))
    user = db.relationship('Users')

    def __repr__(self):
        return f'<Table: "Customers",id:"{self.id}", first_name:"{self.first_name}, last_name:"{self.last_name}, address:"{self.address},phone_no:"{self.phone_no}, credit_card_no:"{self.credit_card_no}, user_id:"{self.user_id} ">'

class Countries(db.Model):
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    name = db.Column(db.String(50), nullable=False, unique=True)
    
    def __repr__(self):
        return f'<Table: "Countries",id:"{self.id}", name:"{self.name}">'

class AirlineCompanies(db.Model):
    __tablename__ = 'airline_companies'
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    name = db.Column(db.String(50), nullable=False, unique=True)
    country_id = db.Column(db.Integer, db.ForeignKey('countries.id'))
    user_id = db.Column(db.Integer, db.ForeignKey('users.id'))
    user = db.relationship('Users')
    
    def __repr__(self):
        return f'<Table: "AirlineCompanies",id:"{self.id}", name:"{self.name}, country_id:"{self.country_id}, user_id:"{self.user_id}">'

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
        return f'<Table: "Flights",id:"{self.id}", airline_company_id:"{self.airline_company_id}, origin_country_id:"{self.origin_country_id}",destination_country_id:"{self.destination_country_id}",departure_time:"{self.departure_time}",landing_time:"{self.landing_time}",remaining_tickets:"{self.remaining_tickets}">'

class Tickets(db.Model):
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    flight_id = db.Column(db.Integer, db.ForeignKey('flights.id'))
    flight = db.relationship('Flights')
    customer_id = db.Column(db.Integer, db.ForeignKey('customers.id'))
    customer = db.relationship('Customers')
    
    def __repr__(self):
        return f'<Table: "Tickets",id:"{self.id}", flight_id:"{self.flight_id}",customer_id:"{self.customer_id}">'

user_roles_list = ['Administrator', 'Airline_Company', 'Customer', 'Anonymous']
users_list = [['Ofir8bd','123456789','Ofir8bd@gmail.com',1],\
                ['Ofir7bd','123456789','Ofir7bd@gmail.com',2],\
                ['Ofir6bd','123456789','Ofir6bd@gmail.com',3],\
                ['Ofir66bd','123456789','Ofir66bd@gmail.com',3],\
                ['Ofir9bd','123456789','Ofir9bd@gmail.com',4],\
                    ['Kobe24','123456789','Kobe24@gmail.com',1],\
                       ['El_Al_company','123456789','El_Al_company@gmail.com',2],\
                        ['Ryanair_company','123456789','Ryanair_company@gmail.com',2],\
                            ['Lufthansa_company','123456789','Lufthansa_company@gmail.com',2],\
                        ['United_airlines_company','123456789','United_airlines_company@gmail.com',2]]
administrators_list = [['Ofir8','Ben David8', 1 ],['Kobe','Bryant', 6 ]]
customers_list = [['Ofir','Ben David','Atlit',"972548105702", "5465-8776-5476-7643", 3],['Ofir66','Ben David66','Atlit66',"97254810570266", "5465-8776-6676-7643", 4]]
countries_list = ['Israel', 'Marocco', 'USA', 'Lebanon']
airlines_list = [['El-Al', 1, 7], ['Ryanair',2,8], ['Lufthansa',3,9], ['United_airlines',4,10]]
flights_list = [[1,1,2,2022,2,21,3,50,2022,2,22,4,30,100],[1,1,3,2022,2,21,3,50,2022,2,22,4,30,100],[2,2,3,2023,4,21,5,45,2023,4,26,4,30,100]]
tickets_list = [[1,1],[2,2]]

if __name__ == '__main__':
    with app.app_context():
        db.drop_all()
        db.create_all()
        for i in range(len(user_roles_list)):
            try:
                db.session.add(UserRoles(role_name=user_roles_list[i]))
                db.session.commit()
            except Exception as e:
                print(f"Error: {e}")

        for i in range(len(users_list)):
            try:
                # usr_role = UserRoles.query.filter_by(role_name='Customer').first()
                # print(usr_role.id)
                # db.session.add(Users(username=users_list[i][0],password=users_list[i][1],email=users_list[i][2],user_role=usr_role.id))
                user = Users(username=users_list[i][0],password=users_list[i][1],email=users_list[i][2],user_role=users_list[i][3])
                db.session.add(user)
                db.session.commit()
            except Exception as e:
                print(f"Error: {e}")

        for i in range(len(administrators_list)):
            try:
                admin = Administrators(first_name=administrators_list[i][0],last_name=administrators_list[i][1],user_id=administrators_list[i][2])
                # print(admin)
                db.session.add(admin)
                db.session.commit()
            except Exception as e:
                print(f"Error: {e}")

        for i in range(len(customers_list)):
            try:
                customer = Customers(first_name=customers_list[i][0],last_name=customers_list[i][1],address=customers_list[i][2],phone_no=customers_list[i][3],credit_card_no=customers_list[i][4],user_id=customers_list[i][5])
                # print(customer)
                db.session.add(customer)
                db.session.commit()
            except Exception as e:
                print(f"Error: {e}")
        
        for country in countries_list:
            try:
                # print(Countries(name=country))
                db.session.add(Countries(name=country))
                db.session.commit()
            except Exception as e:
                print(f"Error: {e}")
        
        for i in range(len(airlines_list)):
            try:
                airline_company = AirlineCompanies(name=airlines_list[i][0],country_id=airlines_list[i][1],user_id=airlines_list[i][2])
                # print(airline_company)
                db.session.add(airline_company)
                db.session.commit()
            except Exception as e:
                print(f"Error: {e}")

        for i in range(len(flights_list)):
            try:
                flight = Flights(airline_company_id=flights_list[i][0],
                                origin_country_id=flights_list[i][1],
                                destination_country_id=flights_list[i][2],
                                departure_time=datetime(flights_list[i][3],flights_list[i][4],flights_list[i][5],flights_list[i][6],flights_list[i][7]),
                                landing_time=datetime(flights_list[i][8],flights_list[i][9],flights_list[i][10],flights_list[i][11],flights_list[i][12]),
                                remaining_tickets=flights_list[i][13])
                # print(flight)
                db.session.add(flight)
                db.session.commit()
            except Exception as e:
                print(f"Error: {e}")
        
        for i in range(len(tickets_list)):
            try:
                ticket = Tickets(flight_id=tickets_list[i][0],customer_id=tickets_list[i][1])
                
                db.session.add(ticket)
                db.session.commit()
                # print(ticket)
            except Exception as e:
                print(f"Error: {e}")

print("Tables created and data inserted")



    


