from flask import render_template, request, Blueprint
from flaskblog.models import Post

main = Blueprint('main', __name__) # creates a blueprint for main

@main.route('/')
@main.route('/home')
def home():
    page = request.args.get('page', 1, type=int) # gets the current page (default is 1)
    posts = Post.query.order_by(Post.date_posted.desc()).paginate(page=page, per_page=5) # orders the posts by the date and paginates them
    return render_template('home.html', title='Home', posts=posts) # renders the template 'home.html' and provides the variables 'title' and 'posts' for the template

@main.route('/about')
def about():
    return render_template('about.html', title='About')