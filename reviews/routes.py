import os
from flask import render_template, request, redirect, url_for
from reviews import app, db
from .models import Reviews, Users
from werkzeug.security import generate_password_hash, check_password_hash
from flask_login import UserMixin, login_user, login_required, logout_user, current_user, LoginManager

app.static_folder = 'static'

# Routes for navigation

@app.route("/")
def index():
    return render_template("base.html")

@app.route("/home")
def home():
    return render_template("home.html")

@app.route("/about")
def about():
    return render_template("about.html")

@app.route("/review")
def review():
    return render_template("review.html")

@app.route("/signup")
def signup():
    return render_template("signup.html")

@app.route("/signin")
def signin():
    return render_template("signin.html")


@app.route("/dashboard", methods=['GET', 'POST'])
@login_required
def dashboard():
    return render_template("dashboard.html")

# Post a new review


@app.route("/addpost", methods=['GET', 'POST'])
@login_required
def addpost():
    title =  request.form['title']
    subtitle = request.form['subtitle']
    author = request.form['author']
    content = request.form['content']

    post = Reviews(title=title, subtitle=subtitle, author=author, content=content)

    db.session.add(post)
    db.session.commit()

    return render_template("home.html")

@app.route("/posts/<string:id>")
def posts(id):
    posts = Reviews.query.filter_by(id=id).one()

    return render_template("posts.html", posts=posts)


# Sign up to be a new user
    
@app.route("/newuser", methods=['GET', 'POST'])
def newuser():
    username =  request.form['username']
    password = request.form['password']
    hashed_password = generate_password_hash(password, "sha256")
    user = Users(username=username, password=hashed_password)

    db.session.add(user)
    db.session.commit()

    return render_template("home.html", user=user)

@app.route("/login", methods=['GET', 'POST'])
def login():
    username =  request.form['username']
    password = request.form['password']

    user = Users.query.filter_by(username=username).first()

    if not user:
        return "<h3>User doesn't exist</h3>"
    
    login_user(user)
    return "<h3>You are now logged in</h3>"


login_manager = LoginManager()
login_manager.init_app(app)
login_manager.login_view = "login"

@login_manager.user_loader
def load_user(user_id):
    return Users.query.get(int(user_id))

