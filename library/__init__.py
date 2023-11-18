from flask import Flask, render_template

app = Flask(__name__)

books = {
    "name": "author",
    "name 2": "author 2"
}

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


@app.route("/")
def index():
    return render_template("index.html", title="We have many books")


@app.route("/books")
def get__all_books():
    return render_template("all_books.html", title="All Books", books=all_books)


@app.route("/books/<int:id>")
def get_book(id):

    if id < len(all_books):
        return render_template("book.html", title=all_books[id])
    return "None"
