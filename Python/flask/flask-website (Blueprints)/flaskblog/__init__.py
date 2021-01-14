from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_bcrypt import Bcrypt
from flask_login import LoginManager
from flask_mail import Mail
from flaskblog.config import Config

db = SQLAlchemy() # initiating SQLAlchemy
bcrypt = Bcrypt() # initiating Bcrypt
login_manager = LoginManager() # initiating login_manager
login_manager.login_view = 'users.login' # specifies the route where the user can log in (has to be the exact function name); is important for login_required!
login_manager.login_message_category = 'info' # specifies the kind of message which gets flashed
mail = Mail()

def create_app(config_class=Config):
    app = Flask(__name__)
    app.config.from_object(Config) # imports all configurations set in the config file

    db.init_app(app) # puts the app to the db object
    bcrypt.init_app(app) # puts the app to the bcrypt object
    login_manager.init_app(app) # puts the app to the login_manager object
    mail.init_app(app) # puts the app to the mail object

    from flaskblog.posts.routes import posts # needs to be imported so that the app can use the routes; needs to be imported after the app gets created (important!)
    from flaskblog.users.routes import users # needs to be imported so that the app can use the routes; needs to be imported after the app gets created (important!)
    from flaskblog.main.routes import main # needs to be imported so that the app can use the routes; needs to be imported after the app gets created (important!)

    app.register_blueprint(posts) # registers the blueprint of posts
    app.register_blueprint(users) # registers the blueprint of users
    app.register_blueprint(main) # registers the blueprint of main

    return app