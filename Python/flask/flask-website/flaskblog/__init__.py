import os
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_bcrypt import Bcrypt
from flask_login import LoginManager
from flask_mail import Mail

app = Flask(__name__)
app.config['SECRET_KEY'] = '0e066fcc4927d09f2357bb5c5db69d6b' # is necessary to make sessions work
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///site.db' # path to the SQLite database
db = SQLAlchemy(app) # initiating SQLAlchemy
bcrypt = Bcrypt(app) # initiating Bcrypt
login_manager = LoginManager(app) # initiating login_manager
login_manager.login_view = 'login' # specifies the route where the user can log in (has to be the exact function name); is important for login_required!
login_manager.login_message_category = 'info' # specifies the kind of message which gets flashed
app.config['MAIL_SERVER'] = 'smtp.ewe.net'
app.config['MAIL_PORT'] = '587'
app.config['MAIL_USE_TLS'] = 'True'
app.config['MAIL_PASSWORD'] = os.environ.get('EMAIL_PASSWORD')
app.config['MAIL_USERNAME'] = os.environ.get('EMAIL_USERNAME')
mail = Mail(app)

from flaskblog import routes # needs to be imported so that the app can use the routes; needs to be imported after the app gets created (important!)