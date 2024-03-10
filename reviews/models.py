from reviews import db

class reviews(db.Model):
    # schema for new posted reviews
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.string(60))
    subtitle = db.Column(db.string(50))
    author = db.Column(db.string(30))
    date = db.column(db.Datetime)
    content = db.Column(Text)

    def __repr__(self):
        # __repr__ to represent itself in the form of a string
        return self.title


