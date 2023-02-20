from flask import Flask
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql://root:admin@localhost/flight_db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)

class User_Roles(db.Model):
    __tablename__ = 'user_roles'
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    role_name = db.Column(db.String(50), nullable=False)
    users_table = db.relationship('Users', backref='User_Roles')
    
    def __repr__(self): # for print option
        return f'<Table: "User_Roles", role_name:"{self.role_name}">'

class Users(db.Model):
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    username = db.Column(db.String(50), nullable=False, unique=True)
    password = db.Column(db.String(50), nullable=False)
    email = db.Column(db.String(50), nullable=False, unique=True)
    user_role = db.Column(db.Integer, db.ForeignKey('user_roles.id'))
    administrators_table = db.relationship('Administrators', backref='Users')
    customers_table = db.relationship('Customers', backref='Users')
    airline_companies_table = db.relationship('Airline_Companies', backref='Users')

    def __repr__(self):
        return f'<Table: "Users", username:"{self.username}, password:"{self.password}, email:"{self.email}, user_role:"{self.user_role}">'

class Administrators(db.Model):
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    first_name = db.Column(db.String(50), nullable=False)
    last_name = db.Column(db.String(50), nullable=False)
    user_id = db.Column(db.Integer, db.ForeignKey('users.id'))

    def __repr__(self):
        return f'<Table: "Administrators", first_name:"{self.first_name}, last_name:"{self.last_name}, user_id:"{self.user_id}">'

class Customers(db.Model):
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    first_name = db.Column(db.String(50), nullable=False)
    last_name = db.Column(db.String(50), nullable=False)
    address = db.Column(db.String(50), nullable=False)
    phone_no = db.Column(db.String(50), nullable=False, unique=True)
    credit_card_no = db.Column(db.String(50), nullable=False, unique=True)
    user_id = db.Column(db.Integer, db.ForeignKey('users.id'))

    def __repr__(self):
        return f'<Table: "Customers", first_name:"{self.first_name}, last_name:"{self.last_name}, address:"{self.address},phone_no:"{self.phone_no}, credit_card_no:"{self.credit_card_no}, user_id:"{self.user_id} ">'

class Countries(db.Model):
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    name = db.Column(db.String(50), nullable=False)
    flights_table = db.relationship('Flights', backref='Countries')

    def __repr__(self):
        return f'<Table: "Countries", name:"{self.name}">'

class Airline_Companies(db.Model):
    __tablename__ = 'airline_companies'
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    name = db.Column(db.String(50), nullable=False, unique=True)
    country_id = db.Column(db.Integer, db.ForeignKey('countries.id'))
    user_id = db.Column(db.Integer, db.ForeignKey('users.id'))
    flights_table_origin_country = db.relationship('Flights', backref='Airline_Companies')
    
    def __repr__(self):
        return f'<Table: "Airline_Companies", name:"{self.name}, country_id:"{self.country_id}, user_id:"{self.user_id}">'

class Flights(db.Model):
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    airline_company_id = db.Column(db.Integer, db.ForeignKey('airline_companies.id'))
    origin_country_id = db.Column(db.Integer, db.ForeignKey('countries.id'))
    # destination_country_id = db.Column(db.Integer, db.ForeignKey('countries.id'))

    def __repr__(self):
        return f'<Table: "Flights", airline_company_id:"{self.airline_company_id}, origin_country_id:"{self.origin_country_id}">'


user_roles_list = ['Administrator', 'Airline_Company', 'Customer', 'Anonymous']
users_list = [['Ofir6bd','123456789','Ofir6bd@gmail.com',1],['Ofir7bd','123456789','Ofir7bd@gmail.com',2],['Ofir8bd','123456789','Ofir8bd@gmail.com',3],['Ofir9bd','123456789','Ofir9bd@gmail.com',4],['Kobe24','123456789','Kobe24@gmail.com',3]]
administrators_list = [['John','Travolta', 1 ]]
customers_list = [['Kobe','Bryant','Phili USA',"+1 (123) 456–7890", "5465-8776-5476-7643", 5]]
countries_list = ['Israel', 'Marocco', 'USA', 'Lebanon']
airlines_list = [['El-Al', 1, 1], ['Ryanair',2,2], ['Lufthansa',3,3], ['united airlines',4,4]]
flights_list = [[1,1,1]]

if __name__ == '__main__':
    with app.app_context():
        db.drop_all()
        db.create_all()
        for i in range(len(user_roles_list)):
            try:
                db.session.add(User_Roles(role_name=user_roles_list[i]))
                db.session.commit()
            except Exception as e:
                print(f"Error: {e}")

        for i in range(len(users_list)):
            try:
                # usr_role = User_Roles.query.filter_by(role_name='Customer').first()
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
                airline_company = Airline_Companies(name=airlines_list[i][0],country_id=airlines_list[i][1],user_id=airlines_list[i][2])
                # print(airline_company)
                db.session.add(airline_company)
                db.session.commit()
            except Exception as e:
                print(f"Error: {e}")

        for i in range(len(flights_list)):
            try:
                flight = Flights(airline_company_id=flights_list[i][0],origin_country_id=flights_list[i][1])
                print(flight)
                db.session.add(flight)
                db.session.commit()
            except Exception as e:
                print(f"Error: {e}")



    


