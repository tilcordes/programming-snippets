from datetime import datetime
from flaskblog import db, login_manager, app
from flask_login import UserMixin
from itsdangerous import TimedJSONWebSignatureSerializer as Serializer

@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))

class User(db.Model, UserMixin):
    id = db.Column(db.Integer, primary_key=True) # 'primary_key' provides a unique id for each column
    username = db.Column(db.String(20), unique=True, nullable=False) # 'unique' makes sure that the username is only one time stored in the database; 'nullable' ensures that the entry is not null
    email = db.Column(db.String(120), unique=True, nullable=False)
    image_file = db.Column(db.String(20), nullable=False, default='default.jpg') # 'default' sets a default entry if nothing was submitted in the form
    password = db.Column(db.String(60), nullable=False)
    posts = db.relationship('Post', backref='author', lazy=True) # relationship with another model (in this case 'Post'; 'Post' need to be spelled like the class); 'backref' creates a kind of column in the related model; 'lazy' ensures that the related data only gets loaded when needed

    def get_reset_token(self, expires_sec=1800):
        s = Serializer(app.config['SECRET_KEY'], expires_sec)
        return s.dumps({'user_id': self.id}).decode('utf-8')

    @staticmethod
    def verify_reset_token(token):
        s = Serializer(app.config['SECRET_KEY'])
        try:
            user_id = s.loads(token)['user_id']
        except:
            return None
        return User.query.get(user_id)

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