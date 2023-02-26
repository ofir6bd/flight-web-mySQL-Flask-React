from flask import Flask, redirect, url_for,request, render_template, session, flash
# from flask_mysqldb import MySQL
# import mysql.connector
# from flask_sqlalchemy import SQLAlchemy
from flask_login import UserMixin, login_user, LoginManager,login_required, logout_user,current_user
from Facades.AnonymousFacade import AnonymousFacade

app = Flask(__name__)          
app.secret_key = 'your_secret_key_here'

# app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql://root:admin@localhost/flight_db'
# db = SQLAlchemy(app)

# class User_Roles_table(db.Model):
#     # __tablename__ = 'user_roles'
#     id = db.Column(db.Integer, primary_key=True, autoincrement=True)
#     role_name = db.Column(db.String(50), nullable=False)
#     users_table = db.relationship('Users_table', backref='User_Roles_table')

# class Users_table(db.Model):
#     id = db.Column(db.Integer, primary_key=True, autoincrement=True)
#     username = db.Column(db.String(50), nullable=False, unique=True)
#     password = db.Column(db.String(50), nullable=False)
#     email = db.Column(db.String(50), nullable=False, unique=True)
#     user_role = db.Column(db.Integer, db.ForeignKey('user_roles_table.id'))
    

# @app.route('/create_user',methods=['POST'])
# def create_user():
#     # print('start')
#     if request.method == 'POST':
#         print('here')
#         data = request.args.get('username')      # can use also - get_or_404
#         print(data)
#         try: 
#             user_role = User_Roles_table.query.filter_by(role_name='Administrator').first()
#             print(user_role)
#         except Exception as e:
#             print(f"Error: {e}")
        
#         # print(user_role)
#         # user = Users(username=data['username'], password=data['password'], email=data['email'], user_role=user_role)
#         # db.session.add(user)
#         # db.session.commit()
#         return 'User created successfully!'


@app.route('/',methods=['GET','POST'])                   # 1st option to create view - the home route http://127.0.0.1:5000
def hello():   
    print('**********Starting main route')               				             # this function is the name of the route
    if request.method == 'GET':
        print('**********Starting GET main route')
        return render_template('home.html')        # render a template
     
    if request.method == 'POST':
        print('**********Starting POST at main route')
        print(request)
        
        return render_template('flight.html')
        
@app.route('/Countries',methods=['GET','POST'])                   # 1st option to create view - the home route http://127.0.0.1:5000
def countriesFunc():       
    if request.method == 'GET':
        print('**********Starting GET Countries route')
        return render_template('home.html')      
     
    if request.method == 'POST':
        print('**********Starting POST at main route')
        print(request.args)
        return render_template('flight.html')      

@app.route('/flights',methods=['GET','POST'])
def flights_func():
    print('start flights_func')
    if request.method=='POST':
        print(request.form.get('destination'))
        destination = request.form.get('destination')
        print(destination)
    return render_template('flights.html', destination=destination)

@app.route('/login',methods=['GET','POST'])
def login():
    if request.method=="GET":
        return render_template('login.html')
    elif request.method=="POST":
        username = request.form['username']
        password = request.form['password']
        user =AnonymousFacade(username=username,password=password)
        user_exists = user.login()
        if user_exists:
            # If user exists, set session variable and redirect to home page
            # session.permanent = True
            try:
                session["username"] = username 
            except Exception as e:
                print(f"Error: {e}")
            flash("Login Succesfuly!")
            return redirect(url_for("home"))
        else:
            error = 'Invalid username or password'
            return render_template('login.html', error=error)


if __name__ == "__main__":
    app.debug = True
    app.run()
