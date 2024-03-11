from reviews import db

class reviews(db.Model):
    # schema for new posted reviews
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(60))
    subtitle = db.Column(db.String(50))
    author = db.Column(db.String(30))
    date = db.column(db.Date)
    content = db.Column(db.Text)

    def __repr__(self):
    #     # __repr__ to represent itself in the form of a string
        return self.title


