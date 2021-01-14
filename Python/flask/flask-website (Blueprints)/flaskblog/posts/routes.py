from flask import render_template, url_for, flash, redirect, request, abort, Blueprint
from flask_login import current_user, login_required
from flaskblog import db
from flaskblog.models import Post
from flaskblog.posts.forms import PostForm

posts = Blueprint('posts', __name__) # creates a blueprint for posts

@posts.route('/post/new', methods=['POST', 'GET'])
@login_required # route can only be accesed when the user is logged in
def new_post():
    form = PostForm()
    if form.validate_on_submit(): # gets executed when the form gets submitted
        post = Post(title=form.title.data, content=form.content.data, author=current_user) # creates a new post
        db.session.add(post) # adds the User to the database
        db.session.commit() # commits the changes to the database
        flash('Your post has been created!', 'success')
        return redirect(url_for('main.home'))
    return render_template('create_post.html', title='New Post', form=form, legend='New Post')

@posts.route('/post/<int:post_id>') # dynamic url with the variable 'post_id'
def post(post_id):
    post = Post.query.get_or_404(post_id) # shows the post if it exists or it shows 404 error if it doesnt exist
    return render_template('post.html', title=post.title, post=post)

@posts.route('/post/<int:post_id>/update', methods=['POST', 'GET']) # dynamic url with the variable 'post_id'
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
        return redirect(url_for('posts.post', post_id=post.id))
    elif request.method == 'GET': # is needed to put in the current values into the form
        form.title.data = post.title # puts the current username into the form
        form.content.data = post.content # puts the current email into the form
    return render_template('create_post.html', title='Update Post', form=form, legend='Update Post')

@posts.route('/post/<int:post_id>/delete', methods=['POST']) # dynamic url with the variable 'post_id'
@login_required
def delete_post(post_id):
    post = Post.query.get_or_404(post_id) # gets the post if it exists or it shows 404 error if it doesnt exist
    if post.author != current_user: # gets executed when the current user is not the author of the post
        abort(403) # returns an error (403 = forbidden route)
    db.session.delete(post) # deletes the post
    db.session.commit() # commits the changes to the database
    flash('Your post has been deleted!', 'success')
    return redirect(url_for('main.home'))