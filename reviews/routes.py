import os
from flask import render_template, request, redirect, url_for
from reviews import app, db
from .models import Reviews, Users
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, PasswordField
from wtforms.validators import DataRequired, ValidationError


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


@app.route("/signup", methods=['GET', 'POST'])
def signup():
    username = None
    form = SignUp()
    return render_template("signup.html", name=username, form=form)


# Routes to post a review

@app.route("/posts/<string:id>")
def posts(id):
    posts = Reviews.query.filter_by(id=id).one()

    return render_template('posts.html', posts=posts)
    
# Route for add post form

@app.route("/addpost", methods=['GET', 'POST'])
def addpost():
    title =  request.form['title']
    subtitle = request.form['subtitle']
    author = request.form['author']
    content = request.form['content']

    post = Reviews(title=title, subtitle=subtitle, author=author, content=content)

    db.session.add(post)
    db.session.commit()

    return redirect(url_for('home'))


# Routes to register as a new user

class SignUp(FlaskForm):
    username = StringField("Username", validators=[DataRequired()])
    password = PasswordField("Password", validators=[DataRequired()])
    submit = SubmitField("Sign Up")

    def validate_user(self, username):
        existing_user_username = Users.query.filter_by(username=username.data).first()

        if existing_user_username:
            raise ValidationError("User already exists.")