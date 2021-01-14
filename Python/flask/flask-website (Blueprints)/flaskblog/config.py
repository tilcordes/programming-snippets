import os

class Config:
   SECRET_KEY = os.environ.get('SECRET_KEY') # is necessary to make sessions work (secret key is '0e066fcc4927d09f2357bb5c5db69d6b')
   SQLALCHEMY_DATABASE_URI = 'sqlite:///site.db' # path to the SQLite database
   MAIL_SERVER = os.environ.get('MAIL_SERVER')
   MAIL_PORT = 587
   MAIL_USE_TLS = True
   MAIL_PASSWORD = os.environ.get('EMAIL_PASSWORD')
   MAIL_USERNAME = os.environ.get('EMAIL_USERNAME')