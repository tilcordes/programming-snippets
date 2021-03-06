from datetime import datetime
from flask import current_app
from flaskblog import db, login_manager
from flask_login import UserMixin
from itsdangerous import TimedJSONWebSignatureSerializer as Serializer

@login_manager.user_loader # is needed for flask_login
def load_user(user_id):
    return User.query.get(int(user_id))

class User(db.Model, UserMixin): # 'db.Model' creates the SQLAlchemy Model; UserMixin is important for flask_login to make the login system work (UserMixin provides funcions like 'is_authenticated' for flask_login)
    id = db.Column(db.Integer, primary_key=True) # 'primary_key' provides a unique id for each column
    username = db.Column(db.String(20), unique=True, nullable=False) # 'unique' makes sure that the username is only one time stored in the database; 'nullable' ensures that the entry is not null
    email = db.Column(db.String(120), unique=True, nullable=False)
    image_file = db.Column(db.String(20), nullable=False, default='default.jpg') # 'default' sets a default entry if nothing was submitted in the form
    password = db.Column(db.String(60), nullable=False)
    posts = db.relationship('Post', backref='author', lazy=True) # relationship with another model (in this case 'Post'; 'Post' need to be spelled like the class); 'backref' creates a kind of column in the related model; 'lazy' ensures that the related data only gets loaded when needed

    def get_reset_token(self, expires_sec=1800):
        s = Serializer(current_app.config['SECRET_KEY'], expires_sec) # creates a Serializer object (token) which expires after a while
        return s.dumps({'user_id': self.id}).decode('utf-8') # puts the user_id variable to the token

    @staticmethod
    def verify_reset_token(token):
        s = Serializer(current_app.config['SECRET_KEY']) # creates a Serializer object
        try:
            user_id = s.loads(token)['user_id'] # tries to get the user_id variable out of the token
        except:
            return None # returns None if the token is invalid
        return User.query.get(user_id) # returns the user

    def __repr__(self): # specifies how the class gets printed out (only for testing)
        return f'User("{self.username}", "{self.email}", "{self.image_file}")'

class Post(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(100), nullable=False)
    date_posted = db.Column(db.DateTime, nullable=False, default=datetime.utcnow)
    content = db.Column(db.Text, nullable=False)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False) # ForeignKey creates a relationship to the user id who has written the post; ForeignKey needs to be written lowercase because it uses the tablename (in the SQLite database) and not the classname of the model

    def __repr__(self):
        return f'Post("{self.title}", "{self.date_posted}")'