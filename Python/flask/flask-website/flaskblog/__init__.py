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
bcrypt = Bcrypt(app)
login_manager = LoginManager(app)
login_manager.login_view = 'login'
login_manager.login_message_category = 'info'
app.config['MAIL_SERVER'] = 'smtp.ewe.net'
app.config['MAIL_PORT'] = '587'
app.config['MAIL_USE_TLS'] = 'True'
app.config['MAIL_PASSWORD'] = os.environ.get('EMAIL_PASSWORD')
app.config['MAIL_USERNAME'] = os.environ.get('EMAIL_USERNAME')
mail = Mail(app)

from flaskblog import routes