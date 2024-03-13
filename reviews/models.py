from reviews import db
from werkzeug.security import generate_password_hash, check_password_hash
from datetime import datetime, time

class Reviews(db.Model):
    # schema for new posted reviews
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(60))
    subtitle = db.Column(db.String(50))
    author = db.Column(db.String(30))
    date = db.Column(db.Date)
    content = db.Column(db.Text)

    def __repr__(self):
        return self.title


class Users(db.Model):
    # schema for new user created
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(150), nullable=False)
    emailaddress = db.Column(db.String(150), nullable=False, unique=True)
    password_hash = db.Column(db.String(128))


    def __repr__(self):
        return self.username
