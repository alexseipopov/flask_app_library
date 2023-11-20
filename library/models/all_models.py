from library import db
import sqlalchemy as sa


class User(db.Model):
    id = sa.Column(sa.Integer, primary_key=True)
    login = sa.Column(sa.String, nullable=False)
    password = sa.Column(sa.String, nullable=False)


class Book(db.Model):
    id = sa.Column(sa.Integer, primary_key=True)
    title = sa.Column(sa.String, nullable=False)
    author = sa.Column(sa.String, nullable=False)
    is_stock = sa.Column(sa.Boolean, default=True)
    user_id = sa.Column(sa.Integer, sa.ForeignKey('user.id'), nullable=False)
