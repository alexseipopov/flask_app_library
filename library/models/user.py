from library import db
import sqlalchemy as sa


class User(db.Model):
    id = sa.Column(sa.Integer, primary_key=True)
    login = sa.Column(sa.String, nullable=False)
    password = sa.Column(sa.String, nullable=False)
