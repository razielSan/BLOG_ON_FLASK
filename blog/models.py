from blog import db
from flask_login import UserMixin


class User(db.Model, UserMixin):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(20), unique=True, nullable=False)
    email = db.Column(db.String(), unique=True, nullable=False)
    image_file = db.Column(db.String(20), nullable=False, default='default.jpg')
    password = db.Column(db.String(), nullable=False)
    post = db.relationship('Post', backref='author', lazy=True)


    def __repr__(self):
        return f'User({self.username}, {self.email}, {self.image_file})'