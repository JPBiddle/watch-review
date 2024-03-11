import os
from flask import render_template
from reviews import app
from .models import reviews

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
