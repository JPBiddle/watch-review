import os
from flask import Flask, render_template, request, redirect, url_for, session, flash
from reviews import app, db
from .models import Reviews, Users
from sqlalchemy import desc, asc
from werkzeug.security import generate_password_hash, check_password_hash
from flask_login import UserMixin, login_user, login_required, logout_user, current_user, LoginManager
from flask_ckeditor import CKEditor

app.static_folder = 'static'

login_manager = LoginManager()
login_manager.init_app(app, db)
login_manager.login_view = "login"
ckeditor = CKEditor(app)

@login_manager.user_loader
def load_user(user_id):
    user = user_id
    print("User id: ", user)
    return Users.query.get(user_id)

# Routes for navigation

@app.route("/")
def index():
    return redirect(url_for('home'))

@app.route("/home")
def home():
    # Get all posts from db
    posts = Reviews.query.order_by(Reviews.date.desc())
    return render_template("home.html", posts=posts)

@app.route("/about")
def about():
    return render_template("about.html")

@app.route("/review")
@login_required
def review():
    return render_template("review.html")


@app.route("/signup")
def signup():
        return render_template("signup.html")


@app.route("/dashboard", methods=['GET', 'POST'])
@login_required
def dashboard():
    posts = current_user.poster
    return render_template("dashboard.html", user=current_user, posts=posts)

# Post a new review

@app.route("/addpost", methods=['GET', 'POST'])
def addpost():
    poster = current_user
    title =  request.form['title']
    subtitle = request.form['subtitle']
    content = request.form['ckeditor']

    post = Reviews(title=title, subtitle=subtitle, content=content, poster=poster)

    db.session.add(post)
    db.session.commit()
    flash("Review posted!")
    return redirect(url_for('dashboard'))

# Populate page with a review

@app.route("/posts/<string:id>")
def posts(id):
    posts = Reviews.query.get_or_404(id)
    return render_template("posts.html", posts=posts)


# Sign up to be a new user
    
@app.route("/newuser", methods=['GET', 'POST'])
def newuser():
    username = request.form['username'].lower()
    password = request.form['password']
    existuser = Users.query.filter_by(username=username).first()
    if existuser:
        flash("Username exists, please choose a different username.")
        redirect(url_for('newuser'))
    else:
        hashed_password = generate_password_hash(password, "sha256")
        user = Users(username=username, password=hashed_password)
        db.session.add(user)
        db.session.commit()
        flash("User created, you can now sign in!")
        return render_template("signin.html", user=user)
    return render_template("signup.html")

# Login user

@app.route("/signin", methods=['GET', 'POST'])
def login():
    if request.method == "POST":
        username =  request.form['username'].lower()
        password =  request.form['password']
        printuser = username
        user = Users.query.filter_by(username=username).first()
        if user and check_password_hash(user.password, password):
            login_user(user)
            flash("Logged in successfully")
            return redirect(url_for('dashboard'))
        if not user:
            flash("User doesn't exist, please sign up.")
            return render_template("signin.html")
        else:
            flash("Password incorrect.")
            return render_template("signin.html")
    return render_template("signin.html")

# Logout user

@app.route("/signout", methods=['GET', 'POST'])
@login_required
def signout():
    logout_user()
    flash("Logged out successfully")
    return render_template("signin.html")

# Delete user posts
@app.route("/posts/delete/<string:id>")
def delete_review(id):
    review_to_delete = Reviews.query.get_or_404(id)
    try:
        db.session.delete(review_to_delete)
        db.session.commit()
        flash("Review deleted.")
        return redirect(url_for('dashboard'))
    except:
        flash("Error, review not deleted.")
        return redirect(url_for('dashboard'))


# Edit users review
@app.route("/posts/edit/<int:id>", methods=['GET', 'POST'])
def edit_review(id):
    editpost = Reviews.query.get_or_404(id)
    if request.method == "POST":
        poster = current_user
        editpost.title =  request.form['title']
        editpost.subtitle = request.form['subtitle']
        editpost.content = request.form['ckeditor']

        db.session.add(editpost)
        db.session.commit()

        flash("Review updated!")
    return render_template("edit.html", editpost=editpost)