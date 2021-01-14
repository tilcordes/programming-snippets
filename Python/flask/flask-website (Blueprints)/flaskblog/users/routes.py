from flask import render_template, url_for, flash, redirect, request, Blueprint
from flask_login import login_user, current_user, logout_user, login_required
from flaskblog import db, bcrypt
from flaskblog.models import User, Post
from flaskblog.users.forms import RegistrationForm, LoginForm, UpdateAccountForm, RequestResetForm, ResetPasswordForm
from flaskblog.users.utils import save_picture, send_reset_email

users = Blueprint('users', __name__) # creates a blueprint for users

@users.route('/register', methods=['GET', 'POST']) # 'methods' makes sure that only allowed methods get submitted
def register():
    if current_user.is_authenticated: # gets executed when the user is already loged in
        return redirect(url_for('main.home'))
    form = RegistrationForm() # initiates the form
    if form.validate_on_submit(): # gets executed when the form gets submitted
        hashed_password = bcrypt.generate_password_hash(form.password.data).decode('utf-8') # hashes the password which was submitted in the form
        user = User(username=form.username.data, email=form.email.data, password=hashed_password) # creates the User
        db.session.add(user) # adds the User to the database
        db.session.commit() # commits the changes to the database
        flash('Your account has been created! You are now able to log in', 'success') # send a message to the template with the category 'success'
        return redirect(url_for('users.login'))
    return render_template('register.html', title='Register', form=form)

@users.route('/login', methods=['POST', 'GET'])
def login():
    if current_user.is_authenticated: # gets executed when the user is already loged in
        return redirect(url_for('main.home'))
    form = LoginForm() # initiates the form
    if form.validate_on_submit(): # gets executed when the form gets submitted
        user = User.query.filter_by(email=form.email.data).first()
        if user and bcrypt.check_password_hash(user.password, form.password.data): # checks if the user exists and the password is valid
            login_user(user, remember=form.remember.data) # logs the user in if everything went right
            next_page = request.args.get('next')
            return redirect(next_page) if next_page else redirect(url_for('main.home')) # if next_page is given it redirects to it else it redirects to home
        else:
            flash('Login Unsuccessful. Please check email and password!', 'danger') # if something went wrong a message gets flashed to the template
    return render_template('login.html', title='Login', form=form)

@users.route('/logout')
def logout():
    logout_user() # logs the user out
    return redirect(url_for('main.home'))

@users.route('/account', methods=['POST', 'GET'])
@login_required # route can only be accesed when the user is logged in
def account():
    form = UpdateAccountForm()
    if form.validate_on_submit(): # gets executed when the form gets submitted
        if form.picture.data: # only gets executed if profile picture was uploaded
            picture_file = save_picture(form.picture.data) # saves the profile picture
            current_user.image_file = picture_file # updates the profile picture
        current_user.username = form.username.data # updates the username
        current_user.email = form.email.data # updates the email
        db.session.commit() # commits the changes to the database
        flash('Your account has been updated!', 'success') # send a message to the template with the category 'success'
        return redirect(url_for('users.account'))
    elif request.method == 'GET': # is needed to put in the current values into the form
        form.username.data = current_user.username # puts the current username into the form
        form.email.data = current_user.email # puts the current email into the form
    image_file = url_for('static', filename='profile_pics/' + current_user.image_file) # profil picture of the user
    return render_template('account.html', title='Account', image_file=image_file, form=form)

@users.route('/user/<string:username>') # dynamic url with the variable 'username'
def user_posts(username):
    page = request.args.get('page', 1, type=int) # gets the current page (default is 1)
    user = User.query.filter_by(username=username).first_or_404() # gets the user if it exists or it shows 404 error if it doesnt exist
    posts = Post.query.filter_by(author=user)\
        .order_by(Post.date_posted.desc())\
        .paginate(page=page, per_page=5) # gets the posts of the user, oders them by the date and paginates them (\ can be used to split a command)
    return render_template('user_posts.html', title='User', posts=posts, user=user)

@users.route('/reset_password', methods=['POST', 'GET'])
def reset_request():
    if current_user.is_authenticated: # gets executed when the user is already loged in
        return redirect(url_for('main.home'))
    form = RequestResetForm()
    if form.validate_on_submit(): # gets executed when the form gets submitted
        user = User.query.filter_by(email=form.email.data).first() # gets the user by the email
        send_reset_email(user) # sends a reset mail to the user
        flash('An email has been sent with instructions to reset your password.', 'info')
        return redirect(url_for('users.login'))
    return render_template('reset_request.html', title='Reset Password', form=form)

@users.route('/reset_password/<token>', methods=['POST', 'GET'])
def reset_token(token):
    if current_user.is_authenticated: # gets executed when the user is already loged in
        return redirect(url_for('main.home'))
    user = User.verify_reset_token(token) # gets the user out of the token
    if user is None: # gets executed when token was invalid
        flash('That is an invalid or expired token', 'warning')
        return redirect(url_for('users.reset_request'))
    form = ResetPasswordForm()
    if form.validate_on_submit(): # gets executed when the form gets submitted
        hashed_password = bcrypt.generate_password_hash(form.password.data).decode('utf-8') # generates the password hash
        user.password = hashed_password # changes the password of the user to the new one
        db.session.commit() # commits the changes to the database
        flash('Your password has been updated! You are now able to log in', 'success')
        return redirect(url_for('users.login'))
    return render_template('reset_token.html', title='Reset Password', form=form)