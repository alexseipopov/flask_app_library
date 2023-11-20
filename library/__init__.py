from flask import Flask
from flask_sqlalchemy import SQLAlchemy


app = Flask(__name__)

app.config["SECRET_KEY"] = "your_secret_key"
app.config["SQLALCHEMY_DATABASE_URI"] = "postgresql://postgres:postgres@localhost:5432/library"

db = SQLAlchemy(app)

from library.handlers import books

app.register_blueprint(books)

from library.auth import auth

app.register_blueprint(auth)
