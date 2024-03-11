import os
from flask import render_template, request, redirect
from reviews import app, db
from .models import Reviews

app.static_folder = 'static'

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


@app.route("/addpost", methods=['POST'])
def addpost():
    title =  request.form['title']
    subtitle = request.form['subtitle']
    author = request.form['author']
    content = request.form['content']

    post = Reviews(title=title, subtitle=subtitle, author=author, content=content)

    db.session.add(post)
    db.session.commit()

    return redirect(url_for('home'))
