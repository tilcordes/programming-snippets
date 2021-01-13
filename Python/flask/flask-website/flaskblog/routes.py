import os
import secrets
from PIL import Image
from flask import render_template, url_for, flash, redirect, request, abort
from flaskblog import app, db, bcrypt, mail
from flaskblog.forms import RegistrationForm, LoginForm, UpdateAccountForm, PostForm, RequestResetForm, ResetPasswordForm
from flaskblog.models import User, Post
from flask_login import login_user, current_user, logout_user, login_required
from flask_mail import Message

@app.route('/')
@app.route('/home')
def home():
    page = request.args.get('page', 1, type=int)
    posts = Post.query.order_by(Post.date_posted.desc()).paginate(page=page, per_page=5)
    return render_template('home.html', title='Home', posts=posts) # renders the template 'home.html' and provides the variables 'title' and 'posts' for the template

@app.route('/about')
def about():
    return render_template('about.html', title='About')

@app.route('/register', methods=['GET', 'POST']) # 'methods' makes sure that only allowed methods get submitted
def register():
    if current_user.is_authenticated: # gets executed when the user is already loged in
        return redirect(url_for('home'))
    form = RegistrationForm() # initiates the form
    if form.validate_on_submit(): # gets executed when the form gets submitted
        hashed_password = bcrypt.generate_password_hash(form.password.data).decode('utf-8') # hashes the password which was submitted in the form
        user = User(username=form.username.data, email=form.email.data, password=hashed_password) # creates the User
        db.session.add(user) # adds the User to the database
        db.session.commit() # commits the changes to the database
        flash('Your account has been created! You are now able to log in', 'success') # send a message to the template with the category 'success'
        return redirect(url_for('login'))
    return render_template('register.html', title='Register', form=form)

@app.route('/login', methods=['POST', 'GET'])
def login():
    if current_user.is_authenticated: # gets executed when the user is already loged in
        return redirect(url_for('home'))
    form = LoginForm() # initiates the form
    if form.validate_on_submit(): # gets executed when the form gets submitted
        user = User.query.filter_by(email=form.email.data).first()
        if user and bcrypt.check_password_hash(user.password, form.password.data): # checks if the user exists and the password is valid
            login_user(user, remember=form.remember.data) # logs the user in if everything went right
            next_page = request.args.get('next')
            return redirect(next_page) if next_page else redirect(url_for('home')) # if next_page is given it redirects to it else it redirects to home
        else:
            flash('Login Unsuccessful. Please check email and password!', 'danger') # if something went wrong a message gets flashed to the template
    return render_template('login.html', title='Login', form=form)

@app.route('/logout')
def logout():
    logout_user() # logs the user out
    return redirect(url_for('home'))

def save_picture(form_picture):
    random_hex = secrets.token_hex(8) # generates a random hex with 8 digits
    f_name, f_ext = os.path.splitext(form_picture.filename) # splits the filename to the name and the extension ('filename' + 'png')
    picture_filename = random_hex + f_ext # connects the extension to the random hex
    picture_path = os.path.join(app.root_path, 'static/profile_pics', picture_filename) # generates the path of the profile picture

    output_size = (50, 50)
    i = Image.open(form_picture) # opens the uploaded picture
    i.thumbnail(output_size) # resizes the picture

    i.save(picture_path) # saves the picture with the new filename
    return picture_filename # returns the filename

@app.route('/account', methods=['POST', 'GET'])
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
        return redirect(url_for('account'))
    elif request.method == 'GET': # is needed to put in the current values into the form
        form.username.data = current_user.username # puts the current username into the form
        form.email.data = current_user.email # puts the current email into the form
    image_file = url_for('static', filename='profile_pics/' + current_user.image_file) # profil picture of the user
    return render_template('account.html', title='Account', image_file=image_file, form=form)

@app.route('/post/new', methods=['POST', 'GET'])
@login_required # route can only be accesed when the user is logged in
def new_post():
    form = PostForm()
    if form.validate_on_submit(): # gets executed when the form gets submitted
        post = Post(title=form.title.data, content=form.content.data, author=current_user) # creates a new post
        db.session.add(post) # adds the User to the database
        db.session.commit() # commits the changes to the database
        flash('Your post has been created!', 'success')
        return redirect(url_for('home'))
    return render_template('create_post.html', title='New Post', form=form, legend='New Post')

@app.route('/post/<int:post_id>')
def post(post_id):
    post = Post.query.get_or_404(post_id) # shows the post if it exists or it shows 404 error if it doesnt exist
    return render_template('post.html', title=post.title, post=post)

@app.route('/post/<int:post_id>/update', methods=['POST', 'GET'])
@login_required
def update_post(post_id):
    post = Post.query.get_or_404(post_id) # gets the post if it exists or it shows 404 error if it doesnt exist
    if post.author != current_user: # gets executed when the current user is not the author of the post
        abort(403) # returns an error (403 = forbidden route)
    form = PostForm()
    if form.validate_on_submit(): # gets executed when the form gets submitted
        post.title = form.title.data # updates the title
        post.content = form.content.data # updates the content
        db.session.commit() # commits the changes to the database
        flash('Your post has been updatad!', 'success')
        return redirect(url_for('post', post_id=post.id))
    elif request.method == 'GET': # is needed to put in the current values into the form
        form.title.data = post.title # puts the current username into the form
        form.content.data = post.content # puts the current email into the form
    return render_template('create_post.html', title='Update Post', form=form, legend='Update Post')

@app.route('/post/<int:post_id>/delete', methods=['POST'])
@login_required
def delete_post(post_id):
    post = Post.query.get_or_404(post_id) # gets the post if it exists or it shows 404 error if it doesnt exist
    if post.author != current_user: # gets executed when the current user is not the author of the post
        abort(403) # returns an error (403 = forbidden route)
    db.session.delete(post) # deletes the post
    db.session.commit() # commits the changes to the database
    flash('Your post has been deleted!', 'success')
    return redirect(url_for('home'))

@app.route('/user/<string:username>')
def user_posts(username):
    page = request.args.get('page', 1, type=int)
    user = User.query.filter_by(username=username).first_or_404()
    posts = Post.query.filter_by(author=user)\
        .order_by(Post.date_posted.desc())\
        .paginate(page=page, per_page=5)
    return render_template('user_posts.html', title='User', posts=posts, user=user)

def send_reset_email(user):
    token = user.get_reset_token()
    msg = Message('Password Reset Request', sender='noreply@demo.com', recipients=[user.email])
    msg.body = f'''To reset your password, visit the following link:
{url_for('reset_token', token=token, _external=True)}

If you did not made this request then simply ignore this email and no changes will be made.
'''
    mail.send(msg)

@app.route('/reset_password', methods=['POST', 'GET'])
def reset_request():
    if current_user.is_authenticated:
        return redirect(url_for('home'))
    form = RequestResetForm()
    if form.validate_on_submit():
        user = User.query.filter_by(email=form.email.data).first()
        send_reset_email(user)
        flash('An email has been sent with instructions to reset your password.', 'info')
        return redirect(url_for('login'))
    return render_template('reset_request.html', title='Reset Password', form=form)

@app.route('/reset_password/<token>', methods=['POST', 'GET'])
def reset_token(token):
    if current_user.is_authenticated:
        return redirect(url_for('home'))
    user = User.verify_reset_token(token)
    if user is None:
        flash('That is an invalid or expired token', 'warning')
        return redirect(url_for('reset_request'))
    form = ResetPasswordForm()
    if form.validate_on_submit():
        hashed_password = bcrypt.generate_password_hash(form.password.data).decode('utf-8')
        user.password = hashed_password
        db.session.commit()
        flash('Your password has been updated! You are now able to log in', 'success')
        return redirect(url_for('login'))
    return render_template('reset_token.html', title='Reset Password', form=form)