import os
from flask import render_template
from watchreviews import app, db

@app.route("/")
def home():
    return render_template("base.html")
