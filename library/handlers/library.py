from . import books
from library import db
from flask import render_template, redirect
from flask_wtf import FlaskForm
from wtforms import StringField, BooleanField, SubmitField
from wtforms.validators import DataRequired
from library.models.all_models import User, Book


all_books = [{
        "name": "Гарри Поттер",
        "author": "Джоан Роулинг",
        "isStock": False
    }, {
        "name": "Flask Documentation",
        "author": "PalettsProject",
        "isStock": True
    }, {
        "name": "Евгений Онегин",
        "author": "Александр Пушкин",
        "isStock": True
    }]


class AddBookForm(FlaskForm):
    name = StringField("Name of Book", validators=[DataRequired()])
    author = StringField("Author", validators=[DataRequired()])
    isStock = BooleanField("Is stock?", default=True)
    submit = SubmitField("Add book")


@books.route("/")
def index():
    user = User.query.all()
    print(user)
    return render_template("index.html", title="We have many books")


@books.route("/books")
def get__all_books():
    all_books = Book.query.all()
    return render_template("all_books.html", title="All Books", books=all_books)


@books.route("/books/<int:id>")
def get_book(id):
    book = Book.query.filter_by(id=id).first()
    if book:
        return render_template("book.html", title=book.title, book=book)
    return redirect("/books")


@books.route("/add_book", methods=["GET", "POST"])
def add_book():
    form = AddBookForm()
    if form.validate_on_submit():
        name = form.name.data
        author = form.author.data
        isStock = form.isStock.data
        user_id = 1
        book = Book(title=name, author=author, is_stock=isStock, user_id=user_id)
        db.session.add(book)
        db.session.commit()
        return redirect("/books")
    return render_template("add_book.html", title="Add Book", form=form)
