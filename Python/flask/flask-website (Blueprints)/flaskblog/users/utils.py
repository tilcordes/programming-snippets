import os
import secrets
from PIL import Image
from flask import url_for, current_app
from flask_mail import Message
from flaskblog import mail

def save_picture(form_picture):
    random_hex = secrets.token_hex(8) # generates a random hex with 8 digits
    f_name, f_ext = os.path.splitext(form_picture.filename) # splits the filename to the name and the extension ('filename' + 'png')
    picture_filename = random_hex + f_ext # connects the extension to the random hex
    picture_path = os.path.join(current_app.root_path, 'static/profile_pics', picture_filename) # generates the path of the profile picture

    output_size = (50, 50)
    i = Image.open(form_picture) # opens the uploaded picture
    i.thumbnail(output_size) # resizes the picture

    i.save(picture_path) # saves the picture with the new filename
    return picture_filename # returns the filename

def send_reset_email(user):
    token = user.get_reset_token() # creates a token for the user
    msg = Message('Password Reset Request', sender='noreply@demo.com', recipients=[user.email]) # creates a mail
    msg.body = f'''To reset your password, visit the following link:
{url_for('users.reset_token', token=token, _external=True)}

If you did not make this request then simply ignore this email and no changes will be made.
''' # body of the mail in a multiline string
    mail.send(msg) # sends the mail