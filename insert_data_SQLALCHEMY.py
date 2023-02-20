from flask import Flask
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)     

app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql://root:admin@localhost/flight_db'
db = SQLAlchemy(app)

class User_Roles(db.Model):
    # __tablename__ = 'user_roles'
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    role_name = db.Column(db.String(50), nullable=False)
    # users_table = db.relationship('Users_table', backref='User_Roles_table')

    def __init__(self, role_name):
        self.role_name = role_name

# class Users_table(db.Model):
#     id = db.Column(db.Integer, primary_key=True, autoincrement=True)
#     username = db.Column(db.String(50), nullable=False, unique=True)
#     password = db.Column(db.String(50), nullable=False)
#     email = db.Column(db.String(50), nullable=False, unique=True)
#     user_role = db.Column(db.Integer, db.ForeignKey('user_roles_table.id'))

def test():
    try:
        new_role = User_Roles('Administrator')
        db.session.add(new_role)
        db.session.commit()
    except Exception as e:
        print(f'error: {e}')


if __name__ == '__main__':
    db.create_all()
    test()
    app.run(debug=True)
