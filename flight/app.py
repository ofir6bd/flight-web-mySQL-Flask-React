# Import required modules
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_bcrypt import Bcrypt
from flask_migrate import Migrate
from secrets_keys import *
from flask_cors import CORS
from flask_login import LoginManager

# Create instances of Flask extensions
login_manager = LoginManager()
db = SQLAlchemy()
migrate = Migrate()
bcrypt = Bcrypt()

# Set login manager configurations
login_manager.session_protection = "strong"
login_manager.login_view = "login"
login_manager.login_message_category = "info"

# Define function to create the Flask app
def create_app():
    # Create Flask app object
    app = Flask(__name__, static_folder='static')
    # Enable CORS for cross-origin resource sharing
    CORS(app)
    # Set Flask app configurations
    app.secret_key = SECRET_KEY
    # app.config['SQLALCHEMY_DATABASE_URI'] = f'mysql+mysqlconnector://root:{PASSWORD}@localhost/{DATABASE}'
    app.config['SQLALCHEMY_DATABASE_URI'] = f'mysql+mysqlconnector://root:{PASSWORD}@dockerdb/{DATABASE}'
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
    # Initialize Flask extensions with Flask app object
    login_manager.init_app(app)
    db.init_app(app)
    migrate.init_app(app, db)
    bcrypt.init_app(app)
    # Return Flask app object
    return app