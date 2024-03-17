from reviews import db
from datetime import datetime, time
from flask_login import UserMixin


class Users(UserMixin, db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(150), nullable=False)
    password = db.Column(db.String(250), nullable=False)
    poster = db.relationship('Reviews', backref='users')

class Reviews(db.Model):
    # schema for new posted reviews
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(60))
    subtitle = db.Column(db.String(50))
    author = db.Column(db.String(30))
    date = db.Column(db.Date)
    content = db.Column(db.Text)
    review_id = db.Column(db.Integer, db.ForeignKey('users.id'))